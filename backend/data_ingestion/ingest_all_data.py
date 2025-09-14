# ingest_all_data.py
import os
from typing import List, Tuple

def load_txt_files(directory: str) -> List[Tuple[str, str]]:
    documents = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            path = os.path.join(directory, filename)
            with open(path, "r", encoding="utf-8") as file:
                content = file.read()
                documents.append((filename, content))
    return documents

if __name__ == "__main__":
    docs = load_txt_files("../docs")
    for filename, content in docs:
        print(f"{filename}:\n{content}\n")
