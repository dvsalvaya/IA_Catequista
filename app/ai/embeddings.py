# app/ai/embeddings.py
from agno.knowledge.embedder.ollama import OllamaEmbedder
from app.core import config

def get_ollama_embedder():
    return OllamaEmbedder(
        id=config.MODEL_EMBEDDING, 
        dimensions=config.EMBEDDING_DIMENSIONS
    )