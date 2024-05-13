import streamlit as st
import pandas as pd
from pinecone import Pinecone
from langchain_community.embeddings import OllamaEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
import matplotlib.pyplot as plt
import re


def extract_answer(embedded_query, embeddings):
    pc = Pinecone(api_key='14480b48-5f50-4277-814b-f5e011641821')
    index_name = "10k-2"
    index = pc.Index(index_name)
    result = index.query(vector=embedded_query, top_k=3)
    ids = [match['id'] for match in result['matches']]
    texts = []
    for id in ids:
        # Fetch the metadata for each ID
        metadata = index.fetch(ids=[id])['vectors'][id]['metadata']
        text = metadata.get('text', '')
        texts.append(text)
    return texts


def generate_response(context, query):
    PROMPT_TEMPLATE = """
    Answer the question based only on the following context:

    {context}

    ---

    Answer the question based on the above context: {question}
    """
    context_text = ",".join(str(element) for element in context)
    print("Context", context_text)
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query)
    print("Prompt", prompt)
    model = Ollama(model="mistral")
    response = model.invoke(prompt)
    print(response)
    return response


def get_embeddings(articles, embeddings):
    return embeddings.embed_documents(texts=articles)


def extract_values(content):
    pattern = r"\|(.+?)\|(.+?)\|(.+?)\|"

    # Using regex to find all matches of the pattern in the text
    matches = re.findall(pattern, content)

    # Create a DataFrame from the matches
    df = pd.DataFrame(matches)

    # Remove leading and trailing whitespace from column values
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    df = df.dropna()

    numeric_columns = df.columns[df.dtypes.apply(pd.api.types.is_numeric_dtype)]
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors="ignore")
    return df


def analyze_and_visualize_data(data, graph_type):
    if graph_type == "SFD":
        df_numeric = data.dropna(subset=[2], how='any')
        # Convert values to string and remove non-numeric characters
        df_numeric[2] = df_numeric[2].str.replace(',''').str.replace('$', '')
        # Convert values to numeric
        df_numeric[2] = pd.to_numeric(df_numeric[2], errors='coerce')
        # Plot the data
        st.subheader("Principal Amounts Over Time")
        fig, ax = plt.subplots()
        ax.plot(df_numeric[0], df_numeric[2], marker='o')
        ax.set_xlabel('Year')
        ax.set_ylabel('Principal (in $)')
        ax.set_title('Principal Amounts Over Time')
        ax.tick_params(axis='x', rotation=45)
        ax.grid(True)
        st.pyplot(fig)
    elif graph_type == 'FR':
        df = data.replace({'\$': '', ',': ''}, regex=True)
        df = df.apply(pd.to_numeric, errors='coerce')
        # Plotting
        for column in df.columns[1:]:
            plt.plot(df['Year'], df[column], marker='o', label=column)
        plt.title('Financial Data Over Time')
        plt.xlabel('Year')
        plt.ylabel('Dollars in millions except per share amounts')
        plt.grid(True)
        plt.legend()
        st.pyplot()


def main():
    embeddings = OllamaEmbeddings(model="nomic-embed-text", show_progress=True)
    st.title('Financial Analysis of 10-k Filings')
    st.subheader('Ask questions about T-mobile, AT&T and Verizon!')
    query = st.text_input('Enter your query:')
    if st.button('Get Query Answer'):
        embed = get_embeddings([query], embeddings)
        query_context = extract_answer(embed, embeddings)
        query_answer = generate_response(query_context, query)
        st.write("Query answer:", query_answer)

    company_name = st.selectbox('Select Company:', ['AT&T', 'Verizon', 'T-Mobile'])
    visualization_prompts = {"SDG": f"In a tabular format, return selected financial data of {company_name}",
                             "FR": f"In a tabular format, extract financial and operating data in Dollars in millions "
                                   f"for {company_name}"}

    for graph_type, queries in visualization_prompts.items():
        embed = get_embeddings([queries], embeddings)
        query_context = extract_answer(embed, embeddings)
        query_answer = generate_response(query_context, queries)
        visualization_data = extract_values(query_answer)
        analyze_and_visualize_data(visualization_data, graph_type)


if __name__ == '__main__':
    main()
