# 🎭 Emotion-Aware AI Chatbot  

An intelligent conversational AI system that understands the **user’s facial emotions** and dynamically adapts its responses to provide more natural and human-like interaction.

---

## 📌 Project Overview  

This project combines **Deep Learning, Computer Vision, and Natural Language Processing** to build an emotionally aware chatbot.  
The system captures facial expressions through a webcam, detects the user’s emotional state, and generates context-aware responses accordingly.

This approach improves user experience by enabling **emotion-adaptive conversations**, a key research area in modern AI known as **Affective Computing**.

---

## 🚀 Features  

✅ Real-time facial emotion detection using webcam  
✅ Emotion classification (Happy, Sad, Angry, Neutral, etc.)  
✅ Adaptive chatbot responses based on detected emotion  
✅ Speech input and audio response support  
✅ Modular AI architecture (Vision + NLP + Audio pipeline)  
✅ Secure API integration using environment variables  

---

## 🧠 Tech Stack  

### 🔹 Deep Learning  
- Convolutional Neural Networks (CNN)  
- Facial Expression Recognition (FER2013 dataset)

### 🔹 Computer Vision  
- OpenCV  
- Real-time face detection & preprocessing  

### 🔹 Natural Language Processing  
- Transformer-based LLM / GPT API  
- Emotion-aware response generation  

### 🔹 Audio Processing  
- Speech recognition  
- Text-to-speech synthesis  

### 🔹 Backend / Tools  
- Python  
- dotenv for secure API key management  

---

## ⚙️ How It Works  

1. Webcam captures the user’s facial expression  
2. CNN model predicts the current emotion  
3. Emotion signal is sent to the chatbot engine  
4. NLP model generates an emotion-adaptive response  
5. Response is delivered via text and speech  

---

## ▶️ How to Run  

```bash
git clone https://github.com/jebisha2005/emotional-aware-ai-chatbot.git
cd emotional-aware-ai-chatbot

pip install -r requirements.txt
