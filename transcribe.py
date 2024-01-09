import subprocess
import wave
import argparse
import convert_audio

WHISPER_EXE = "/home/gianluca/Documents/repos/ytwhisper/whisper/main-blas"
WHISPER_MODEL = (
    "/home/gianluca/Documents/repos/ytwhisper/whisper/models/ggml-base.en.bin"
)


def transcribe(filename: str, output_file: str):
    """Transcribe audio using whisper.cpp, locally"""

    with wave.open(filename, "r") as file:
        framerate = file.getframerate()
        nframes = file.getnframes()

        duration = nframes / framerate
        print(f"Duration: {duration} seconds")

    subprocess.run(
        [
            WHISPER_EXE,
            "-m",
            WHISPER_MODEL,
            "-f",
            filename,
            "-np",
            "-otxt",
            "-of",
            output_file,
        ]
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transcribe audio")
    parser.add_argument("filename", metavar="filename", type=str, help="the filename")
    args = parser.parse_args()
    filename = args.filename

    if not filename.lower().endswith(".wav"):
        converted_filename = "output.wav"
        convert_audio.convert_audio(filename, converted_filename)
        filename = converted_filename

    output_file = "output.txt"
    transcribe(filename, output_file)
