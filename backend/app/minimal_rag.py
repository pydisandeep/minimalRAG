from vectorstores.vectorstore import VectorStore
from helper_functions.answer_rag import rag_answer

# Load vectorstore once
vs = VectorStore(persist_directory="./vector_db")

def main_app(user_query: str):
    """Run RAG pipeline for a single user query."""
    answer, sources = rag_answer(user_query, vs)
    return answer, sources
