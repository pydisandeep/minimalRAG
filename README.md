# Minimal RAG Prototype

This is a minimal Retrieval-Augmented Generation (RAG) prototype.  
It loads text documents, stores their embeddings in a vector database, and answers user queries using a language model (LLM) with retrieved context.  

You can run it in two main ways:
1. **Backend (FastAPI) + Frontend (React)** → Recommended for UI
2. **CLI Mode** → Simple terminal chatbot

---

## 🚀 Features

- Load and embed `.txt` files
- Split documents into chunks (paragraph + recursive splitting)
- Store and query embeddings in a vector store
- Answer questions using an open-source Hugging Face LLM
- Return answers **with source document names**
- Simple **React frontend** and **FastAPI backend**

---

## 🛠️ Setup

1. Clone the repo and `cd` into the project folder. (git clone https://github.com/pydisandeep/minimalRAG.git)
2. Install dependencies:
**Backend (Python)**
```
cd backend
source venv/Scripts/activate
pip install -r requirements.txt


 **Frontend (React)**
```
cd frontend
npm install

▶️ Run with FastAPI + React (UI Mode)

👉 Open two terminal windows (one for backend, one for frontend).

🔹 Windows PowerShell / CMD

**Backend**
```
cd backend
python -m uvicorn app.fastapi:app --reload

**Frontend**
```
cd frontend
npm start

🔹 Git Bash / Linux / macOS

**Backend**
```
cd backend
uvicorn app.fastapi:app --reload

**Frontend**
```
cd frontend
npm start

▶️ Run in CLI Mode (Optional)

If you don’t want UI/API, you can run a simple chatbot directly in the terminal.

🔹 Windows PowerShell / CMD
```
cd backend
python app\minimal_rag.py

🔹 Git Bash / Linux / macOS
```
cd backend
python app/minimal_rag.py


