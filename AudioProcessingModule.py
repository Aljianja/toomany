# AudioProcessingModule.py

import numpy as np

class AudioProcessingModule:
    def __init__(self, rate=44100, chunk_size=1024, noise_threshold_factor=1.5):
        self.rate = rate
        self.chunk_size = chunk_size
        self.noise_levels = []
        self.noise_threshold_factor = noise_threshold_factor

    def process_data(self, audio_data):
        # Perform FFT to convert the audio to the frequency domain
        fft_data = np.fft.fft(audio_data)
        freqs = np.fft.fftfreq(len(fft_data)) * self.rate

        # Calculate and store the current noise level
        current_noise_level = np.mean(np.abs(audio_data))
        self.noise_levels.append(current_noise_level)
        if len(self.noise_levels) > 100:  # Keep the last 100 noise level readings
            self.noise_levels.pop(0)

        return freqs, np.abs(fft_data)

    def average_noise_level(self):
        if self.noise_levels:
            return sum(self.noise_levels) / len(self.noise_levels)
        return 0

    def detect_baby_cry(self, freqs, fft_data, threshold=10):
        # Example range for a baby's cry
        baby_cry_freq_range = (300, 600)

        # Check if the frequencies in the baby cry range are significantly higher than the threshold
        cry_detected = np.any((freqs > baby_cry_freq_range[0]) & (freqs < baby_cry_freq_range[1]) & (fft_data > threshold))

        # Check if the current sound level significantly exceeds the average noise level
        current_level = np.mean(fft_data)
        if current_level > self.average_noise_level() * self.noise_threshold_factor and cry_detected:
            return True
        return False
