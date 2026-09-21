import pyttsx3

class VoiceAssistant:
    def __init__(self):
        self.tts = pyttsx3.init()

    def get_response(self, intent, entities):
        # Basit intent kontrolü
        if intent == "greeting":
            response = "Merhaba! Size nasıl yardımcı olabilirim?"
        elif intent == "farewell":
            response = "Görüşmek üzere, kendinize iyi bakın!"
        else:
            response = "Bunu tam olarak anlayamadım ama yardımcı olmaya çalışabilirim."

        # Sesli okuma
        self.tts.say(response)
        self.tts.runAndWait()

        return response
