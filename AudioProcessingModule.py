# AudioProcessingModule.py

import numpy as np

class AudioProcessingModule:
    def __init__(self, rate=44100, chunk_size=1024):
        self.rate = rate
        self.chunk_size = chunk_size

    def process_data(self, audio_data):
        try:
            fft_data = np.fft.fft(audio_data)
            freqs = np.fft.fftfreq(len(fft_data)) * self.rate
            return freqs, np.abs(fft_data)
        except Exception as e:
            print(f"Error processing audio data: {e}")
            return np.zeros(len(audio_data)), np.zeros(len(audio_data))

    def detect_baby_cry(self, freqs, fft_data, threshold=10):
        baby_cry_freq_range = (300, 600)  # Example range
        cry_detected = np.any((freqs > baby_cry_freq_range[0]) & (freqs < baby_cry_freq_range[1]) & (fft_data > threshold))
        return cry_detected
