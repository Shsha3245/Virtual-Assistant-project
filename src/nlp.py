import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

class NLPUtility:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()

    def process_input(self, user_input):
        tokens = word_tokenize(user_input)
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens]

        intent = self.detect_intent(tokens)
        entities = self.extract_entities(tokens)

        return intent, entities

    def detect_intent(self, tokens):
        # Basit örnek: selamlama kontrolü
        if any(token.lower() in ["hello", "hi", "selam"] for token in tokens):
            return "greeting"
        elif any(token.lower() in ["bye", "goodbye", "görüşürüz"] for token in tokens):
            return "farewell"
        else:
            return "unknown"

    def extract_entities(self, tokens):
        # Basit örnek: özel isimleri yakala
        entities = [token for token in tokens if token.istitle()]
        return entities
