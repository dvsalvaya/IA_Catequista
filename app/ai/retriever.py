# app/ai/retriever.py
from agno.knowledge import Knowledge
from app.repositories.vector_repository import get_vector_db

def get_knowledge_base():
    return Knowledge(vector_db=get_vector_db())