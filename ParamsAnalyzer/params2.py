import os
import numpy as np
import librosa

# Function to calculate the mean intensity of an audio signal
def calculate_mean_intensity(audio):
    return np.mean(np.abs(audio))

# Function to calculate the mean MFCCs of an audio signal
def calculate_mean_mfccs(audio, sample_rate):
    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=13)
    return np.mean(mfccs, axis=1)

# Function to process audio files in a directory
def process_audio_directory(directory_path):
    # List of supported audio file extensions (add more if needed)
    supported_extensions = (".wav",)

    # Initialize lists to store results
    mean_intensity_values = []
    mean_mfccs_values = []

    # Iterate through files in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        # Check if the file has a supported extension
        if file_path.lower().endswith(supported_extensions):
            # Load the audio and perform mean intensity and mean MFCC analysis
            audio, sample_rate = librosa.load(file_path, sr=None)  # Load audio with original sample rate
            mean_intensity = calculate_mean_intensity(audio)
            mean_mfccs = calculate_mean_mfccs(audio, sample_rate)

            # Append the results to the lists
            mean_intensity_values.append(mean_intensity)
            mean_mfccs_values.append(mean_mfccs)

    return mean_intensity_values, mean_mfccs_values

# Provide the directory path containing WAV files
directory_path = "/home/terratany/labs/toomany/ParamsAnalyzer/files"

# Process audio files in the directory
intensity_values, mfccs_values = process_audio_directory(directory_path)

# Return arrays of all the values for mean intensity and mean MFCCs
intensity_values_array = np.array(intensity_values)
mfccs_values_array = np.array(mfccs_values)

# Print or use the arrays as needed
print("Mean Intensity Values Array:", intensity_values_array)
print("Mean MFCCs Values Array:")
print(mfccs_values_array)
