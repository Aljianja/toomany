# AudioCaptureModule.py

import pyaudio
import numpy as np

class AudioCaptureModule:
    def __init__(self, rate=44100, chunk_size=1024):
        self.rate = rate
        self.chunk_size = chunk_size
        self.pyaudio_instance = pyaudio.PyAudio()
        try:
            self.stream = self.pyaudio_instance.open(
                format=pyaudio.paFloat32,
                channels=1,
                rate=self.rate,
                input=True,
                frames_per_buffer=self.chunk_size
            )
        except Exception as e:
            print(f"Error opening audio stream: {e}")
            self.cleanup()

    def get_audio_data(self):
        try:
            audio_data = np.fromstring(self.stream.read(self.chunk_size, exception_on_overflow=False), dtype=np.float32)
            return audio_data
        except Exception as e:
            print(f"Error reading audio data: {e}")
            return np.zeros(self.chunk_size)

    def cleanup(self):
        try:
            self.stream.stop_stream()
            self.stream.close()
            self.pyaudio_instance.terminate()
        except Exception as e:
            print(f"Error closing audio stream: {e}")
