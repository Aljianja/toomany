# main.py

from AudioCaptureModule import AudioCaptureModule
from AudioProcessingModule import AudioProcessingModule
from VisualizerModule import VisualizerModule

def main():
    audio_capture = AudioCaptureModule()
    audio_processor = AudioProcessingModule()
    visualizer = VisualizerModule()

    audio_capture.start_stream()

    try:
        while True:
            audio_data = audio_capture.get_audio_data()
            freqs, fft_data = audio_processor.process_data(audio_data)

            if audio_processor.detect_baby_cry(freqs, fft_data):
                print("Baby cry detected!")

            try:
                visualizer.update_visualizer(freqs, fft_data)
            except SystemExit:
                break

    except KeyboardInterrupt:
        pass
    finally:
        audio_capture.cleanup()

if __name__ == "__main__":
    main()
