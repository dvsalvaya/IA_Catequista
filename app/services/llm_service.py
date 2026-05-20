# app/services/llm_service.py
from agno.models.ollama import Ollama
from app.core import config

def get_llm_model():
    return Ollama(id=config.MODEL_LLM)