from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.rag import build_index, search

app = FastAPI(title="NCERT RAG Backend")

# ✅ CORS configuration (needed for frontend-backend integration)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ Use specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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