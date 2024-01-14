# VisualizerModule.py

import matplotlib.pyplot as plt

class VisualizerModule:
    def __init__(self):
        plt.ion()
        self.figure, self.ax = plt.subplots()

    def update_visualizer(self, freqs, fft_data):
        if plt.fignum_exists(self.figure.number):
            self.ax.clear()
            self.ax.plot(freqs, fft_data)
            self.ax.set_xlabel('Frequency (Hz)')
            self.ax.set_ylabel('Amplitude')
            self.ax.set_title('Real-time Audio Spectrum Analyzer')
            plt.pause(0.1)
        else:
            raise SystemExit

