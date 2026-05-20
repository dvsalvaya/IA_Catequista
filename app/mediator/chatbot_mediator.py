# app/mediator/chatbot_mediator.py
from agno.agent import Agent
from app.services.llm_service import get_llm_model
from app.ai.retriever import get_knowledge_base
from app.core import config

class ChatbotMediator:
    def __init__(self):
        self.agent = Agent(
            id="Cat",
            name="Cat",
            model=get_llm_model(),
            role=config.SYSTEM_PROMPT,
            tools=[],
            add_context=True,        # Faz o Python buscar no banco de dados automaticamente
            search_knowledge=False,  # Desativa a ferramenta para a IA não se confundir mais
            knowledge=get_knowledge_base(),
            markdown=True
        )

    def chat(self, message: str, user_id: str):
        # Executa a resposta via stream diretamente no terminal
        self.agent.print_response(message, stream=True, id=user_id)