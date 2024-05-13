## Project README

### Project Overview

This project leverages Jupyter Notebook and PyCharm with Python and Streamlit to analyze data from T-Mobile, AT&T, and Verizon. These companies are pivotal players in the telecommunications industry, maintaining significance throughout technological evolution. The analysis delves into how these companies respond to risk, evaluating the effectiveness of their strategies. Understanding these responses not only fosters trust in the company's decision-making but also enables users to gauge the efficacy of their teams and decisions. Allowing users to understand risk factors, companies response and performace of their response will help users understand make an informed decision before investing and a greater perspective on a companies setback and strategies. 

## Versions
This repository contains 2 versions of the implementation: 

fsil_assignment: Submitted on May 7th, with complete code of RAG with Mistral, Pinecone for vectorization, and Ollama's enviornment, however, I lost the vectors due to disconnection of my GPU and couldn't finish the UI implementation. While the project demonstrates my coding capabilities, unforeseen time constraints hindered its completion. Despite near-perfect execution, an unexpected GPU disconnection prevented the visualization of insights and further insights extraction and also led toloss of my already executed code. To run everything again, especially vectorization would have taken me 2/3 hours more, which will exceed the dealine. If my exams didn't just end around 14 hours ago, I would have gotten a headstart. Given more time, I am confident in my ability to showcase the full potential of the project requirements and beyond.

updated-and-finished: Submitted May 12th, with same code as submitted previously with vectors stored in Pinecone to avoid loss due to GPU constraints of google colab, and finished implementation with the UI. It's be my humble request if you could consider this implementation as it shows my complete project, working of the RAG model with Pinecone database and visualization techniques. 

## Features

1. **Automatic Downloading of SEC-Edgar 10K Files:**
   - The system automatically retrieves SEC-Edgar 10K files from the Securities and Exchange Commission (SEC) website.
  
2. **Preprocessing and Saving of Files:**
   - The downloaded 10K files undergo preprocessing to clean and organize the data, and then they are saved for further analysis.

3. **Text Chunking and Embedding:**
   - The preprocessed files are split into text chunks, which are then embedded using the Ollama Nomic embedding technique.
  
4. **Metadata Extraction and Storage:**
   - Metadata is extracted from the text chunks and stored along with the chunks in a Pinecone database.

5. **Exploratory Data Analysis (EDA):**
   - The Jupyter notebook includes exploratory steps to illustrate the data processing flow and provide insights into the dataset.

6. **Query-Based Information Retrieval:**
   - In the `app.py` file, users can input queries to search for information related to T-Mobile, AT&T, and Verizon.
   
7. **Semantic Search and Contextual Understanding:**
   - The system retrieves similar embeddings from the Pinecone database based on the user's query and uses them as context for the Ollama Mistral model to provide relevant information.
   - 
8. **Ticker-based Table Extraction and Plotting:**
   - Users can input a ticker to retrieve relevant information, and the system extracts tables using regular expressions (regex) and plots the data for visualization.
  
## Pinecone Database
![image](https://github.com/shahtvisha/fsil-application/assets/91308439/cc8a8df9-26b0-4337-b8d9-1a1e9fb03f7c)
![image](https://github.com/shahtvisha/fsil-application/assets/91308439/440d8cf1-b59d-46a7-bbef-c78e5697c370)

## Streamlit User Interface
![Screenshot (675)](https://github.com/shahtvisha/fsil-application/assets/91308439/df03426e-269e-42a1-9251-ab18a0678b3b)
![Screenshot (676)](https://github.com/shahtvisha/fsil-application/assets/91308439/3c06a511-5df3-46c1-937b-36248416a197)
![Screenshot (677)](https://github.com/shahtvisha/fsil-a![Screenshot (679)](https://github.com/shahtvisha/fsil-application/assets/91308439/6a0b18a4-2c58-4abc-a700-a4623dbf80e1)
pplication/assets/91308439/b294ec2f-6b56-4672-bef8-db52cb7a5834)


### Acknowledgement

Thank you for considering my project. I assure you of my diligence and commitment to maximizing my capabilities given the opportunity.

Code to google colab: https://colab.research.google.com/drive/1LK4ZmaZ5GBS82rdYA7M4oPNRSHSvXjQm?usp=sharing
