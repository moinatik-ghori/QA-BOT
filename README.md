# Document Q&A Chatbot

This is a **Document Q&A Chatbot** built using **Streamlit**, **Hugging Face Transformers**, and **FAISS** for efficient document retrieval. The chatbot allows users to upload text or PDF documents and ask questions about the content. It uses a pre-trained language model to generate accurate and detailed answers.

---

## Features
- **Document Support**: Upload text (`*.txt`) or PDF (`*.pdf`) files.
- **Question-Answering**: Ask questions about the document content.
- **Efficient Retrieval**: Uses FAISS for fast and accurate document retrieval.
- **User-Friendly Interface**: Built with Streamlit for a simple and intuitive UI.

---

## Sample Questions and Answers

Here are some sample questions you can ask the chatbot and the expected answers:

### Sample Document Content
```text
The company policy states that employees are entitled to 20 days of paid leave per year. Employees can carry forward up to 5 unused leave days to the next year. To apply for leave, employees must submit a leave request at least one week in advance. The HR department will review and approve the request within 3 business days.

The office working hours are from 9:00 AM to 6:00 PM, Monday to Friday. Employees are required to take a one-hour lunch break between 1:00 PM and 2:00 PM. Flexible working hours are available for employees who have prior approval from their manager.

The company provides health insurance for all employees. The insurance covers medical, dental, and vision expenses. Employees can add their dependents to the insurance plan by submitting a request to the HR department.

# Document Q&A Chatbot

This is a **Document Q&A Chatbot** built using **Streamlit**, **Hugging Face Transformers**, and **FAISS** for efficient document retrieval. The chatbot allows users to upload text or PDF documents and ask questions about the content. It uses a pre-trained language model to generate accurate and detailed answers.
```
---

## Sample Questions

### Question 1
**Question**: "How many days of paid leave are employees entitled to?"  
**Answer**: "Employees are entitled to 20 days of paid leave per year."

### Question 2
**Question**: "What are the office working hours?"  
**Answer**: "The office working hours are from 9:00 AM to 6:00 PM, Monday to Friday."

### Question 3
**Question**: "How can employees apply for leave?"  
**Answer**: "Employees must submit a leave request at least one week in advance."

### Question 4
**Question**: "What does the health insurance cover?"  
**Answer**: "The insurance covers medical, dental, and vision expenses."

### Question 5
**Question**: "Can employees carry forward unused leave days?"  
**Answer**: "Employees can carry forward up to 5 unused leave days to the next year."

---

## Installation

Follow these steps to install and run the Document Q&A Chatbot on your local machine.

### Step 1: Clone the Repository
Clone the repository to your local machine:
```bash
git clone git@github.com:moinatik-ghori/QA-BOT.git
cd document-qa-chatbot
```
### Step 2: Install Dependencies
Install the required Python packages using the requirements.txt file:

```
pip install -r requirements.txt
```


### Step 3: Run the Application
#### Start the Streamlit app:
```
streamlit run app.py
```
### Step 4: Access the Chatbot

Open your browser and navigate to the URL provided in the terminal (usually http://localhost:8501).

## How to Use the Chatbot

- Upload a Document:
- Click the "Upload a document" button and select a text (*.txt) or PDF (*.pdf) file.
- Enter your question in the text input box and press Enter.

View the Answer:

The chatbot will retrieve relevant information from the document and generate an answer.

File Structure
```
document-qa-chatbot/
├── app.py                  # Main Streamlit application
├── document_loader.py      # Handles document loading and preprocessing
├── vector_store.py         # Creates and manages the FAISS vector store
├── qa_model.py             # Handles question-answering logic
├── requirements.txt        # List of dependencies
├── README.md               # Project documentation
└── sample.txt              # Sample text file for testing
```

## Deployment
### Local Deployment

Follow the installation steps above.

Run the Streamlit app:

```
streamlit run app.py
```

## Cloud Deployment

You can deploy the app on cloud platforms like Streamlit Sharing, Heroku, or AWS. Here’s an example for Streamlit Sharing:

- Create a requirements.txt file (already included in the repository).
- Push your code to a GitHub repository.
- Go to Streamlit Sharing, log in with your GitHub account, and deploy the app by selecting your repository.

## Contributing

If you'd like to contribute to this project, follow these steps:

- Fork the repository.
- Create a new branch:
```
git checkout -b feature/your-feature-name
```
Make your changes and commit them:
```
git commit -m "Add your feature"
```
Push to the branch:
```
git push origin feature/your-feature-name
```
- Open a pull request on GitHub.



