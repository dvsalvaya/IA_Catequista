# app/api/chat_routes.py
from app.mediator.chatbot_mediator import ChatbotMediator

class ChatRoutes:
    def __init__(self):
        self.mediator = ChatbotMediator()

    def send_message(self, text: str, user_id: str):
        self.mediator.chat(text, user_id=user_id)