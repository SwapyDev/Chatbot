from responses import generate_response
from language_detection import detect_language

def chatbot():
    print("Chatbot: ¡Hola! / Hello! Ask me about the weather, a fun fact, or the news.")
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
