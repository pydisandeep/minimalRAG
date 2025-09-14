from vectorstores.vectorstore import VectorStore
from llm_setup.simple_llm import SimpleLLM

def rag_answer(user_query: str, vs: VectorStore):
    results = vs.query(user_query, n_results=10)

    retrieved_chunks = results['documents'][0]
    retrieved_metas = results['metadatas'][0]

    llm = SimpleLLM()
    answer, sources = llm.generate_answer(user_query, retrieved_chunks, retrieved_metas)

    return answer, sources