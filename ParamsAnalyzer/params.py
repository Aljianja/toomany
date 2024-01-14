import librosa
import numpy as np
import matplotlib.pyplot as plt
import glob

def analyze_audio(file_path):
    # Load the audio file
    audio, sr = librosa.load(file_path, sr=None)

    # Perform FFT to get frequency domain data
    fft_data = np.abs(np.fft.fft(audio))
    freqs = np.fft.fftfreq(len(fft_data), 1 / sr)

    # Calculate intensity
    intensity = np.mean(fft_data)

    # Compute the power spectrogram
    power_spec = np.abs(librosa.stft(audio))**2

    # Calculate MFCCs
    mfccs = librosa.feature.mfcc(S=power_spec, sr=sr, n_mfcc=13)

    if mfccs.shape[1] < 325:
        mfccs = np.pad(mfccs, ((0, 0), (0, 325 - mfccs.shape[1])), mode='constant')

    # Ensure that all MFCCs arrays have the same shape
    return {
        'intensity': intensity,
        'fft_data': fft_data,
        'freqs': freqs,
        'mfccs': mfccs
    }

def plot_frequency_data(freqs, fft_data, title):
    plt.figure(figsize=(12, 6))
    plt.plot(freqs, fft_data)
    plt.title(title)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.xlim(0, 2000)  # Limiting to 2000 Hz for better visibility
    plt.show()

def main():
    directory = '/home/terratany/labs/toomany/ParamsAnalyzer/files'  # Replace with your directory path
    pattern = '*.wav'  # Adjust the pattern if needed

    # Find all files in the directory that match the pattern
    file_paths = glob.glob(f"{directory}/{pattern}")

    all_intensities = []
    all_mfccs = []

    for file_path in file_paths:
        result = analyze_audio(file_path)
        all_intensities.append(result['intensity'])
        all_mfccs.extend(result['mfccs'])

        # Plot the frequency data for each file
        plot_frequency_data(result['freqs'], result['fft_data'], f"Frequency Analysis of {file_path}")

    # Calculate the mean intensity and MFCCs
    mean_intensity = np.mean(all_intensities)
    mean_mfccs = np.mean(all_mfccs, axis=1)

    print(f"Mean Intensity: {mean_intensity}")
    print(f"Mean MFCCs: {mean_mfccs}")

if __name__ == "__main__":
    main()