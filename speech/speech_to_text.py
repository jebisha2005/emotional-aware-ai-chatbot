import whisper
import logging

class SpeechToText:

    def __init__(self):
        logging.info("Loading Whisper tiny.en model...")
        self.model = whisper.load_model("tiny.en", device="cpu")
        logging.info("Whisper model loaded successfully.")

    def transcribe(self, audio_path):
        logging.info("Transcribing audio...")
        result = self.model.transcribe(audio_path)
        return result["text"]