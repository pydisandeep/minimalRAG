from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.minimal_rag import main_app

app = FastAPI(title="Minimal RAG API", version="1.0")

# ✅ Allow React frontend (localhost:3000) to access FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question: str
    n_results: int = 3

class QueryResponse(BaseModel):
    answer: str
    sources: list[str]

@app.post("/ask", response_model=QueryResponse)
def ask(request: QueryRequest):
    answer, sources = main_app(request.question)
    return QueryResponse(answer=answer, sources=list(sources))

# Optional root endpoint
@app.get("/")
def root():
    return {"status": "✅ RAG API is running"}
