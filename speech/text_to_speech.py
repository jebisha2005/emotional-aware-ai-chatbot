import pyttsx3
from utils.logger import logger

class TextToSpeech:

    def __init__(self):
        self.engine = pyttsx3.init()

    def speak(self, text):
        logger.info("Speaking response...")
        self.engine.say(text)
        self.engine.runAndWait()