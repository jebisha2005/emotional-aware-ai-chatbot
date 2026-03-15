def build_prompt(user_text, emotion):

    tone_map = {
        "Happy": "Respond in an enthusiastic and cheerful tone.",
        "Sad": "Respond in a supportive and comforting tone.",
        "Angry": "Respond calmly and try to de-escalate.",
        "Fear": "Respond reassuringly.",
        "Surprise": "Respond with excitement.",
        "Neutral": "Respond professionally.",
        "Disgust": "Respond politely and neutrally."
    }

    instruction = tone_map.get(emotion, "Respond professionally.")

    prompt = f"""
    User Emotion: {emotion}
    Instruction: {instruction}

    User said: {user_text}

    Generate a helpful response:
    """

    return prompt