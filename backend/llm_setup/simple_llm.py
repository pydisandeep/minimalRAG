import os
from huggingface_hub import InferenceClient

class SimpleLLM:
    def __init__(self, 
                 model_name="mistralai/Mistral-7B-Instruct-v0.2", 
                 hf_api_token=None):
        
        if hf_api_token is None:
            hf_api_token = os.getenv("HF_API_TOKEN")

        if hf_api_token is None:
            raise ValueError("⚠️ HF_API_TOKEN is not set. Please export it before running.")

        self.client = InferenceClient(model=model_name, token=hf_api_token)

    def generate_answer(self, query, retrieved_chunks, retrieved_metas):
        # Combine chunk texts into context
        context = "\n\n".join(retrieved_chunks)

        # Collect unique doc names
        sources = {meta['source'] for meta in retrieved_metas}

        messages = [
            {"role": "system", "content": "You are a helpful assistant. Use only the provided context to answer."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"}
        ]

        response = self.client.chat.completions.create(
            messages=messages,
            max_tokens=1000,
        )

        answer = response.choices[0].message["content"].strip()
        return answer, sources
