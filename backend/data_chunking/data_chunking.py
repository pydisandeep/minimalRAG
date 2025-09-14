from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_documents(documents, chunk_size=500, chunk_overlap=50):
    """
    Splits documents into chunks.

    Parameters:
        documents (List[Tuple[str, str]]): List of tuples (filename, content).
        chunk_size (int): Size of each chunk.
        chunk_overlap (int): Overlap between chunks.

    Returns:
        List[Dict]: List of chunk dictionaries.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunked_docs = []

    for filename, content in documents:
        chunks = splitter.split_text(content)
        for idx, chunk in enumerate(chunks):
            chunked_docs.append({
                'doc': filename,
                'chunk_id': idx,
                'content': chunk
            })

    return chunked_docs

if __name__ == "__main__":
    # Simple test example
    sample_docs = [("example.txt", "This is a sample text used for testing document chunking.")]
    chunks = chunk_documents(sample_docs, chunk_size=20, chunk_overlap=5)
    print(chunks)
