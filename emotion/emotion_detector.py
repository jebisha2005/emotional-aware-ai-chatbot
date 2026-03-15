import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(
    BASE_DIR,
    "..",
    "face_classification",
    "trained_models",
    "emotion_models",
    "fer2013_mini_XCEPTION.110-0.65.hdf5"
)

MODEL_PATH = os.path.abspath(MODEL_PATH)

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")

model = load_model(MODEL_PATH, compile=False)
print("Loading model from:", MODEL_PATH)
print("Model loaded successfully")
print("Model input shape:", model.input_shape)

emotion_labels = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]


def detect_emotion():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot access camera")
        return "Neutral"

    ret, frame = cap.read()
    cap.release()

    if not ret:
        return "Neutral"

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_gray = cv2.resize(roi_gray, (48, 48))
        roi_gray = roi_gray / 255.0
        roi_gray = np.reshape(roi_gray, (1, 48, 48, 1))

        prediction = model.predict(roi_gray, verbose=0)
        emotion_index = np.argmax(prediction)

        return emotion_labels[emotion_index]

    return "Neutral"