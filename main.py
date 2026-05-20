# main.py
from app.api.chat_routes import ChatRoutes

def main():
    # Inicializa a rota da API
    chat_api = ChatRoutes()
    
    text = "Se apresente"
    while text != "bye":
        chat_api.send_message(text, user_id="davi")
        text = input("\n-> ")

if __name__ == "__main__":
    main()