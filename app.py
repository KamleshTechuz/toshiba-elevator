from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import streamlit as st
from langchain_groq import ChatGroq

from langchain_community.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader

st.title("TOSHIBA Standard Type Elevator: Q&A ")

def vectorEmbedding():
    if "vector" not in st.session_state:
        st.session_state.loader = PyPDFLoader('elevator.pdf')
        st.session_state.documents = st.session_state.loader.load()
        st.session_state.textSplitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        st.session_state.docText = st.session_state.textSplitter.split_documents(st.session_state.documents)
        st.session_state.embeddings=OpenAIEmbeddings()
        st.session_state.vector=FAISS.from_documents(st.session_state.docText, st.session_state.embeddings)

prompt=ChatPromptTemplate.from_template(
"""
Answer the questions based on the provided context only.
Please provide the most accurate response based on the question
<context>
{context}
<context>
Questions:{input}
"""
)

llm=ChatGroq(model="llama3-8b-8192")
# llm=ChatGroq(model="gemma-7b-it")

query = st.text_input("Ask anything regarding the Elevator")

if st.button("Document Embeddings"):
    vectorEmbedding()
    st.write("Vector Store BD is available")

if query:
    docChain = create_stuff_documents_chain(llm, prompt)
    retriver = st.session_state.vector.as_retriever()
    retriverChain = create_retrieval_chain(retriver, docChain)
    response = retriverChain.invoke({"input": query})
    st.write(response['answer'])

    with st.expander("Document Similarity Search"):
        for i, doc in enumerate(response['context']):
            st.write(doc.page_content)
            st.write("--------------------------------")