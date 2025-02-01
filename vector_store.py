from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

def create_vector_store(text):
    """
    Creates a vector store from the given text.

    Args:
        text (str): The document text.

    Returns:
        FAISS: A FAISS vector store for similarity search.
    """
    # Split text into chunks
    text_splitter = CharacterTextSplitter(chunk_size=500,chunk_overlap=100)
    chunk = text_splitter.split_text(text)

    # Create embeddings and vector store
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_texts(chunk,embedding)

    return vector_store