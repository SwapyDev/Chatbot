def detect_language(user_input):
    if any(word in user_input.lower() for word in ["hola", "cómo", "adiós", "clima", "dato curioso", "noticia"]):
        return "es"
    return "en"
