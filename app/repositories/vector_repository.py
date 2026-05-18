# app/repositories/vector_repository.py
from agno.vectordb.chroma import ChromaDb
from app.ai.embeddings import get_ollama_embedder
from app.core import config

def get_vector_db():
    return ChromaDb(
        name=config.DB_NAME,
        embedder=get_ollama_embedder(),
        persistent_client=True,
        path=config.DB_PATH
    )