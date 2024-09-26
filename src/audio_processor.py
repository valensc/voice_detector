import librosa
from pydub import AudioSegment

def process_audio(file_path):
    # Load audio file
    y, sr = librosa.load(file_path)

    # Perform voice activity detection
    intervals = librosa.effects.split(y, top_db=20)

    # Normalize intervals to 0-1 range
    duration = librosa.get_duration(y=y, sr=sr)
    voice_segments = [(start/sr/duration, end/sr/duration) for start, end in intervals]

    return voice_segments

def export_audio(input_file, voice_segments, output_file):
    audio = AudioSegment.from_file(input_file)
    output = AudioSegment.empty()

    for start, end in voice_segments:
        start_ms = int(start * len(audio))
        end_ms = int(end * len(audio))
        output += audio[start_ms:end_ms]

    output.export(output_file, format="mp3")