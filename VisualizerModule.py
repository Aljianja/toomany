# VisualizerModule.py

import matplotlib.pyplot as plt

class VisualizerModule:
    def __init__(self):
        plt.ion()

    def update_visualizer(self, freqs, fft_data):
        try:
            plt.clf()
            plt.plot(freqs, fft_data)
            plt.pause(0.1)
        except Exception as e:
            print(f"Error updating visualizer: {e}")
