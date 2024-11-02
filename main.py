from responses import generate_response

def chatbot():
    print("Chatbot: ¡Hola! Preguntame algo sobre el clima, un dato curioso o algo sobre noticias. / Hello! Ask me about the weather, a fun fact, or the news.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "salir"]:
            print("Chatbot: ¡Hasta luego! / Goodbye!")
            break

        response = generate_response(user_input)
        print("Chatbot:", response)

# Inicia el chatbot
if __name__ == "__main__":
    chatbot()
