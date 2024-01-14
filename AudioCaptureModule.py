# AudioCaptureModule.py

import sounddevice as sd
import numpy as np

class AudioCaptureModule:
    def __init__(self, rate=44100, chunk_size=1024):
        self.rate = rate
        self.chunk_size = chunk_size
        self.stream = sd.InputStream(samplerate=self.rate, channels=1, blocksize=self.chunk_size, dtype=np.float32)

    def start_stream(self):
        self.stream.start()

    def get_audio_data(self):
        audio_data, overflowed = self.stream.read(self.chunk_size)
        if overflowed:
            print("Audio buffer has overflowed!")
        return audio_data.flatten()

    def cleanup(self):
        self.stream.stop()
        self.stream.close()
