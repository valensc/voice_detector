# Voice Detector

This is a desktop application that detects voice activity in audio files and allows you to export only the segments containing voice.

## Features

- Import MP3 or WAV audio files
- Detect voice activity and display it on a timeline
- Export a new MP3 file containing only the voice segments

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/voice_detector.git
   cd voice_detector
   ```

2. Ensure you have Python 3.7+ installed on your system.

3. Run the build script:
   ```
   python build.py
   ```

   This script will create a virtual environment, install all necessary dependencies, and build the executable using PyInstaller.

## Usage

After building, you can find the executable in the `dist` directory. Run it to start the application.

Alternatively, you can run the application directly with Python:

1. Activate the virtual environment:
   ```
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

2. Run the application:
   ```
   python src/main.py
   ```

## Development

If you want to modify the code and run it directly:

1. Activate the virtual environment as shown above.
2. Make your changes to the code.
3. Run `python src/main.py` to test your changes.

## License

This project is licensed under the MIT License.