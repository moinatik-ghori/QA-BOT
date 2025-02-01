import streamlit as st
from load_document import load_document
from vector_store import create_vector_store
from qa_model import answer_question
def print_hi(name):

    print(f'Hi, {name}')
    st.title("Document Q&A ChatBot")
    st.write("Upload your Text Document and ask any question")

    # Upload Document
    uploaded_file = st.file_uploader("Upload PDF File", type=["txt", "pdf"])
    if uploaded_file:
        text = load_document(uploaded_file)
        vector_store = create_vector_store(text)

        # Ask Question
        question = st.text_input("Ask your Question about the document")
        if question:
            answer = answer_question(vector_store,question)
            st.write(f"Answer : {answer}")




if __name__ == '__main__':
    print_hi('My First AI Bot Program')

