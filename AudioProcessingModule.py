# AudioProcessingModule.py

import numpy as np

class AudioProcessingModule:
    def __init__(self, rate=44100, chunk_size=1024, history_size=10):
        self.rate = rate
        self.chunk_size = chunk_size
        self.history_size = history_size
        self.intensity_history = [0.00618161, 0.09442594, 0.00082522, 0.03450482, 0.04812154, 0.03486955,
 0.10446531, 0.03288749, 0.05521018, 0.0307204,  0.07338482, 0.06539492,
 0.04874922, 0.05289328, 0.0606789,  0.06465606, 0.12414987, 0.03878504,
 0.02105016, 0.07611307, 0.08375977, 0.03840607, 0.01227502, 0.05788375,
 0.08794484]
        self.frequency_history = [
            7.90519536e-01, 1.11488473e+00, 1.10655141e+00, 1.09320283e+00,
            1.07485294e+00, 1.05181265e+00, 1.02409422e+00, 9.92094755e-01,
            9.56107855e-01, 9.16331589e-01, 8.73052776e-01, 8.26681495e-01,
            7.77644753e-01, 4.07435425e+02, 5.65569397e+02, 5.36172058e+02,
            4.92062347e+02, 4.36444275e+02, 3.72547821e+02, 3.02411224e+02,
            2.26317688e+02, 1.44714935e+02, 5.97071686e+01, -2.49627285e+01,
            -1.04742912e+02, -1.75892807e+02
        ]

    def process_data(self, audio_data):
        fft_data = np.fft.fft(audio_data)
        freqs = np.fft.fftfreq(len(fft_data)) * self.rate
        intensity = np.mean(np.abs(fft_data))
        
        self._update_history(intensity, fft_data)

        return freqs, np.abs(fft_data)

    def _update_history(self, intensity, fft_data):
        if len(self.intensity_history) >= self.history_size:
            self.intensity_history.pop(0)
            self.frequency_history.pop(0)

        self.intensity_history.append(intensity)
        self.frequency_history.append(fft_data)

    def detect_baby_cry(self, freqs, fft_data, intensity_threshold=10, freq_threshold=10):
        if len(self.intensity_history) < self.history_size:
            return False

        current_intensity = np.mean(fft_data)
        intensity_variation = np.var(self.intensity_history)

        # Check for significant intensity and frequency variation
        if current_intensity > intensity_threshold and intensity_variation > some_intensity_variation_threshold:
            return self._check_frequency_variation(freqs, fft_data, freq_threshold)
        return False

    def _check_frequency_variation(self, freqs, fft_data, freq_threshold):
        # Implement frequency variation check
        # Example: Check if certain frequencies are consistently above a threshold
        freq_variation = False
        for freq_range in typical_baby_cry_freq_ranges:
            if np.all([np.any((freqs > freq_range[0]) & (freqs < freq_range[1]) & (frame > freq_threshold)) for frame in self.frequency_history]):
                freq_variation = True
                break

        return freq_variation

# Example frequency ranges typical for baby cries (these values are placeholders)
typical_baby_cry_freq_ranges = [(300, 600), (600, 1000)]

