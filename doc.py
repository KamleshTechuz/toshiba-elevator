from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import streamlit as st
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader

st.cache_data.clear()
st.cache_resource.clear()

st.title("TOSHIBA Standard Type Elevator: Q&A ")

def vectorEmbedding():
    if "vector" not in st.session_state:
        st.session_state.loader = PyPDFLoader('elevator.pdf')
        st.session_state.documents = st.session_state.loader.load()
        st.session_state.textSplitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        st.session_state.docText = st.session_state.textSplitter.split_documents(st.session_state.documents)
        st.session_state.embeddings=OpenAIEmbeddings()
        st.session_state.vector=FAISS.from_documents(st.session_state.docText, st.session_state.embeddings)

query = st.text_input("Ask anything regarding the Elevator")

if st.button("Document Embeddings"):
    vectorEmbedding()
    st.write("Vector Store BD is available")

if query:
    retriever = st.session_state.vector.as_retriever()
    docs = retriever.invoke(query)
    for doc in docs:
        st.write(doc.page_content)
        st.write("--------------------------------")
