from transformers import pipeline

def answer_question(vector_store,question):
    """
    Answers a question based on the document stored in the vector store.

    Args:
        vector_store (FAISS): The vector store containing document chunks.
        question (str): The user's question.

    Returns:
        str: The answer to the question.
    """
    # Retrieve relevant chunks
    relevant_chunks = vector_store.similarity_search(question,k=5)
    context = " ".join([chunk.page_content for chunk in relevant_chunks])

    # Generate Answer
    qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")
    result = qa_pipeline(question=question,context=context)

    # Ensure the answer is not too short
    if len(result["answer"].split()) < 5:  # If the answer is too short, provide more context
        return f"{result['answer']}. For more details: {context[:500]}..."  # Truncate context to avoid overwhelming the user
    else:
        return result["answer"]