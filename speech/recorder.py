import sounddevice as sd
import numpy as np
import wave
import logging


def record_audio(filename="input.wav", duration=5, fs=16000):
    logging.info("Recording audio... Speak now.")

    recording = sd.rec(
        int(duration * fs),
        samplerate=fs,
        channels=1,
        dtype=np.int16
    )

    sd.wait()

    # Save properly formatted WAV file
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)   # 16-bit
        wf.setframerate(fs)
        wf.writeframes(recording.tobytes())

    logging.info("Recording complete.")
    return filename