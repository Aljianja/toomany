# toomany
Baby Cry detector 

# Sound Visualizer Project

## Overview
This Sound Visualizer Project is a Python-based tool that captures audio input, processes it to detect specific frequency ranges (like baby cries), and visualizes the audio data in real-time. The project is structured into modular components for audio capture, processing, and visualization.

## Getting Started

### Prerequisites
- Python 3.x
- Pip (Python package installer)

### Installation

1. **Clone the Repository**  
   Clone this repository to your local machine, or download the source code.

`git clone git@github.com:Aljianja/toomany.git`


2. **Install Required Libraries**  
Navigate to the project directory and install the required libraries using:

`pip install -r requirements.txt`


This will install the following libraries:
- PyAudio
- NumPy
- Matplotlib

### Running the Project

1. **Navigate to the Project Directory**  
Open a terminal and navigate to the directory where you cloned the project.

2. **Execute the Main Script**  
Run the following command:

`python main.py`


This will start capturing audio from your microphone and display the visualizations in real-time. If a baby cry (or a sound within the defined frequency range) is detected, it will be indicated in the terminal.

## Modules

- **AudioCaptureModule**: Handles the audio input from the microphone.
- **AudioProcessingModule**: Processes the audio data and detects specific frequency ranges.
- **VisualizerModule**: Visualizes the audio data in real-time.
- **main.py**: Integrates all modules and runs the application.

### Troubleshooting PyAudio Installation

- **For Linux (Ubuntu/Debian):**
    
    1. Install PortAudio with: `sudo apt-get install portaudio19-dev`
    2. Reinstall PyAudio: `pip install pyaudio`
- **For macOS:**
    
    1. Install PortAudio using Homebrew: `brew install portaudio`
    2. Reinstall PyAudio: `pip install pyaudio`
- **For Windows:**
    
    - Try installing PyAudio using a pre-built wheel from Unofficial Windows Binaries for Python Extension Packages.
    - Alternatively, use an Anaconda environment to install PyAudio.

## Customization

You can modify the frequency range for detection in `AudioProcessingModule.py` according to your needs. The visualization style can also be customized in `VisualizerModule.py`.

## License

This project is licensed under the Apache License 2.0. See the LICENSE section below for more details.

---

Feel free to contribute to this project or suggest improvements!
