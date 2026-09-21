from nlp import NLPUtility
from voice_assistant import VoiceAssistant
from utils import Utility

def main():
    nlp = NLPUtility()
    va = VoiceAssistant()
    utils = Utility()

    user_input = input("User: ")
    intent, entities = nlp.process_input(user_input)

    response = va.get_response(intent, entities)

    print("Assistant:", response)

    utils.save_response(response)

if __name__ == "__main__":
    main()
