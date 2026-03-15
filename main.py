import logging
from brain.llm_engine import LLMEngine
from emotion.emotion_detector import detect_emotion
from speech.speech_to_text import SpeechToText
from speech.text_to_speech import TextToSpeech
from speech.recorder import record_audio

# ---------------------------------
# LOGGING CONFIGURATION
# ---------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


# ---------------------------------
# MAIN APPLICATION LOOP
# ---------------------------------
def main():
    logger.info("Starting Emotion-Aware AI Assistant...")

    llm = LLMEngine()
    stt = SpeechToText()
    tts = TextToSpeech()

    print("AI Assistant is ready. Say something!")
    print("Say 'exit', 'quit', or 'bye' to stop.\n")

    while True:
        try:
            # 1️⃣ Detect Emotion
            emotion = detect_emotion()
            logger.info(f"Detected Emotion: {emotion}")
            audio_path = record_audio(filename="input.wav", duration=5)
            user_text = stt.transcribe(audio_path)
            if not user_text:
                logger.warning("No speech detected. Listening again...")
                continue

            print(f"\nYou: {user_text}")

            # 3️⃣ Exit Condition
            if user_text.lower().strip() in ["exit", "quit", "bye"]:
                farewell = "It was really nice talking with you. See you soon!"
                print(f"\nAI: {farewell}")
                tts.speak(farewell)
                break

            # 4️⃣ Generate AI Response
            response = llm.generate_response(user_text, emotion)

            print(f"\nAI: {response}")

            # 5️⃣ Speak Response
            tts.speak(response)

        except KeyboardInterrupt:
            print("\n\nAI: Goodbye! 👋")
            break

        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            print("Something went wrong. Restarting loop...\n")


# ---------------------------------
# RUN APPLICATION
# ---------------------------------
if __name__ == "__main__":
    main()