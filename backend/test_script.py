from data_ingestion.ingest_all_data import load_txt_files
from data_chunking.data_chunking import chunk_documents
from vectorstores.vectorstore import VectorStore
from llm_setup.simple_llm import SimpleLLM
import os

def run_full_pipeline():
    # Step 1: Load & chunk documents
    docs = load_txt_files("docs")
    chunks = chunk_documents(docs, chunk_size=500, chunk_overlap=50)

    # Step 2: Initialize vector store & add chunks
    vs = VectorStore(persist_directory="./vector_db")
    vs.add_chunks(chunks)

    # Step 3: Query
    test_query = "What is CRISPR Cas9 used for?"
    results = vs.query(test_query, n_results=3)

    retrieved_chunks = results['documents'][0]
    retrieved_metas = results['metadatas'][0]

    print("\n🔍 Top Retrieved Chunks:")
    for doc, meta in zip(retrieved_chunks, retrieved_metas):
        print(f"\nSource: {meta['source']} (Chunk ID: {meta['chunk_id']})")
        print(f"Content: {doc[:200]}...")

    # Step 4: Generate answer using LLM
    print("\nGenerating answer using HuggingFace LLM...")
    llm = SimpleLLM()
    answer, sources = llm.generate_answer(test_query, retrieved_chunks, retrieved_metas)

    # Step 5: Print answer + sources
    print("\n🧠 LLM Generated Answer:")
    print(answer)

    print("\n📄 Sources:", ", ".join(sources))

if __name__ == "__main__":
    run_full_pipeline()
