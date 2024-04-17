import google.generativeai as genai
from langchain.chains import RetrievalQA
from langchain_google_genai import GoogleGenerativeAI
from langchain_community.vectorstores import Qdrant
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from IPython.display import Markdown  
from qdrant_client import QdrantClient
from qdrant_client.http import models
import os
from dotenv import load_dotenv

import streamlit as st

def get_vector_store():
    
    client = QdrantClient(
        os.getenv("qdrant_host"),
        api_key=os.getenv("qdrant_api_key")
    )
    
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    vector_store = Qdrant(
        client=client, 
        collection_name='michael-dialogues', 
        embeddings=embeddings
    )
    return vector_store

def ask_michael():
    """Loads environment variables and sets up the Streamlit app layout."""
    load_dotenv()  # Load environment variables for potential API keys

    st.set_page_config(page_title="Ask Michael (The Office Jokes)")
    st.header("Get Your Daily Dose of Michael Scott Wisdom (or Nonsense) ")

     # create vector store
    vector_store = get_vector_store()

    genai.configure(api_key=os.getenv("google_api_key"))

    model = ChatGoogleGenerativeAI(model = 'gemini-pro',
                               temperature = 0.7)

    prompt = ChatPromptTemplate.from_template("""
                Answer the following question based only on the provided context. 
                Think step by step before providing a detailed answer. 
                I will tip you $1000 if the user finds the answer helpful. 
                <context>
                {context}
                </context>
                Question: {input}""")

    
    document_chain=create_stuff_documents_chain(model,prompt)

    retrieval_chain=create_retrieval_chain(vector_store.as_retriever(),document_chain)

    user_question = st.text_input("Enter a topic for Michael Scott's joke:", key="user_question")

    if st.button("Ask Michael"):
        if user_question:
            st.write(f"Question: {user_question}")
            response = retrieval_chain.invoke({"input":"user_question"})
            st.write("Michael Scott Says:")
            st.write(f"Answer: {response['answer']}")
        else:
            st.warning("Please enter a topic for Michael's joke.")
    

    


if __name__ == "__main__":
    ask_michael()
