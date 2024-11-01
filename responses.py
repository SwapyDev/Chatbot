import random

# Diccionario de respuestas
responses = {
    "en": {
        "hello": "Hello! How can I help you?",
        "how are you": "I'm just a bot, but I'm here to help!",
        "bye": "Goodbye! Have a great day!",
        "weather": "I can tell you about the weather in general terms! Where are you asking about?",
        "fact": "Did you know? The honeybee is the only insect that produces food eaten by humans.",
        "news": "Today's news is: New discoveries in AI are advancing quickly!",
        "more news": "Here’s another one: Scientists are working on making biofuel from algae."
    },
    "es": {
        "hola": "¡Hola! ¿Cómo puedo ayudarte?",
        "cómo estás": "Soy un bot, pero estoy aquí para ayudar.",
        "adiós": "¡Adiós! ¡Que tengas un buen día!",
        "clima": "Puedo contarte sobre el clima en términos generales. ¿De qué ciudad estás preguntando?",
        "dato curioso": "¿Sabías que las abejas son los únicos insectos que producen alimentos consumidos por humanos?",
        "noticia": "La noticia de hoy es: ¡Nuevos descubrimientos en IA avanzan rápidamente!",
        "más noticias": "Aquí va otra: Los científicos están trabajando en crear biocombustible a partir de algas."
    }
}

# Funciones para temas específicos
def get_weather_response():
    weather_options = [
        "It's sunny and warm today!",
        "Looks like rain is on the way!",
        "It's cloudy with a chance of showers.",
        "Clear skies tonight with a cool breeze."
    ]
    return random.choice(weather_options)

def get_fact_response():
    facts = [
        "Did you know? Bananas are berries, but strawberries aren't!",
        "An octopus has three hearts.",
        "Hot water can freeze faster than cold water, known as the Mpemba effect.",
        "Humans and giraffes have the same number of neck vertebrae."
    ]
    return random.choice(facts)

def get_news_response():
    news = [
        "Scientists discovered a potential new planet!",
        "New advancements in space technology allow for faster travel.",
        "AI is now being used in medicine to diagnose diseases more accurately.",
        "Renewable energy is becoming more accessible and affordable."
    ]
    return random.choice(news)

def generate_response(user_input):
    from language_detection import detect_language
    language = detect_language(user_input)
    user_input = user_input.lower()

    if "clima" in user_input or "weather" in user_input:
        return get_weather_response()
    elif "dato curioso" in user_input or "fact" in user_input:
        return get_fact_response()
    elif "noticia" in user_input or "news" in user_input:
        return get_news_response()
    else:
        for keyword, response in responses[language].items():
            if keyword in user_input:
                return response
    
    return "Lo siento, no entiendo. / I'm sorry, I don't understand."
