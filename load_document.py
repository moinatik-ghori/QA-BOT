import PyPDF2
def load_document(file):
    """
    Loads a text document from the given file path.

    Args:
        file_path (str): Path to the text file.

    Returns:
        str: The content of the document as a string.
    """
    if file.type == "text/plain":
        text = file.read().decode("utf-8")
    elif file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
    else:
        raise ValueError(f"{file.type} - UnSupported File Type. Please Upload Text or PDF file Only.")

    return text
