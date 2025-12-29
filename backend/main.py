from fastapi import FastAPI
from backend.rag import build_index, search


app = FastAPI(title="NCERT RAG Backend")

@app.get("/")
def root():
    return {"status": "Backend running"}

@app.post("/ingest")
def ingest():
    msg = build_index()
    return {"message": msg}

@app.post("/ask")
def ask(question: str):
    answers = search(question)
    return {
        "question": question,
        "answers": answers
    }
