from openai import OpenAI
from openai import APIError, RateLimitError
import config


class LLMEngine:
    """
    Emotion-aware conversational LLM engine using Groq (OpenAI-compatible API).
    Maintains short-term memory for continuous conversation.
    """

    def __init__(self):
        self.client = OpenAI(
            api_key=config.GROQ_API_KEY,
            base_url=config.GROQ_BASE_URL
        )

        # Initial system personality
        self.system_prompt = {
            "role": "system",
            "content": (
                "You are a warm, friendly, emotionally intelligent AI assistant. "
                "Talk naturally like a real human friend. "
                "Be supportive and engaging. "
                "Maintain conversation continuity."
            )
        }

        # Conversation memory
        self.messages = [self.system_prompt]

        # Limit memory length to prevent token overflow
        self.max_history_length = 20

    def generate_response(self, user_text: str, emotion: str) -> str:
        """
        Generates a friendly chatbot response based on user text and detected emotion.
        Maintains conversational memory.
        """

        try:
            # Add user message with emotion context
            self.messages.append({
                "role": "user",
                "content": f"(User emotion: {emotion}) {user_text}"
            })

            # Trim conversation if too long
            if len(self.messages) > self.max_history_length:
                self.messages = [self.system_prompt] + self.messages[-(self.max_history_length - 1):]

            # API call
            response = self.client.chat.completions.create(
                model=config.MODEL_NAME,
                messages=self.messages,
                temperature=config.TEMPERATURE,
                max_tokens=config.MAX_TOKENS
            )

            assistant_reply = response.choices[0].message.content.strip()

            # Store assistant reply in memory
            self.messages.append({
                "role": "assistant",
                "content": assistant_reply
            })

            return assistant_reply

        except RateLimitError:
            return "I'm receiving too many requests right now. Please try again in a moment."

        except APIError as e:
            return f"API Error: {str(e)}"

        except Exception as e:
            return f"Unexpected error: {str(e)}"