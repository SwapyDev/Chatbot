import random

# Diccionario de respuestas
responses = {
    "en": {
        "hi": "Hello! How can I help you?",
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

def detect_language(text):
    # Dummy implementation for language detection
    if any(word in text.lower() for word in ["hola", "cómo", "adiós", "clima", "dato", "noticia", "más"]):
        return "es"
    return "en"

def get_weather_response(language):
    weather_options = {
        "en": ["It's sunny!", "It's raining!", "It's cloudy!", "It's snowing!"],
        "es": ["¡Está soleado!", "¡Está lloviendo!", "¡Está nublado!", "¡Está nevando!"]
    }
    return random.choice(weather_options[language])

def get_fact_response(language):
    facts = {
        "en": [
            "Did you know? Bananas are berries, but strawberries aren't!",
            "An octopus has three hearts.",
            "Hot water can freeze faster than cold water, known as the Mpemba effect.",
            "Humans and giraffes have the same number of neck vertebrae."
        ],
        "es": [
            "¿Sabías que? ¡Los plátanos son bayas, pero las fresas no!",
            "Un pulpo tiene tres corazones.",
            "El agua caliente puede congelarse más rápido que el agua fría, conocido como el efecto Mpemba.",
            "Los humanos y las jirafas tienen el mismo número de vértebras en el cuello."
        ]
    }
    return random.choice(facts[language])

def get_news_response(language):
    news = {
        "en": [
            "Scientists discovered a potential new planet!",
            "New advancements in space technology allow for faster travel.",
            "AI is now being used in medicine to diagnose diseases more accurately.",
            "Renewable energy is becoming more accessible and affordable."
        ],
        "es": [
            "¡Científicos descubrieron un posible nuevo planeta!",
            "Nuevos avances en tecnología espacial permiten viajes más rápidos.",
            "La IA ahora se usa en medicina para diagnosticar enfermedades con mayor precisión.",
            "La energía renovable se está volviendo más accesible y asequible."
        ]
    }
    return random.choice(news[language])

def generate_response(user_input):
    language = detect_language(user_input)
    user_input = user_input.lower()

    if "clima" in user_input or "weather" in user_input:
        return get_weather_response(language)
    elif "dato curioso" in user_input or "fact" in user_input:
        return get_fact_response(language)
    elif "noticia" in user_input or "news" in user_input:
        return get_news_response(language)
    else:
        for keyword, response in responses[language].items():
            if keyword in user_input:
                return response
    
    return "Lo siento, no entiendo. / I'm sorry, I don't understand."