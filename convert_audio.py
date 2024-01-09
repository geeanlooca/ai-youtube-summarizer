import subprocess


def convert_audio(filename: str, output_file: str):
    """Convert audio to wav format compatible with whisper.cpp"""
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-i",
            filename,
            "-ar",
            "16000",
            "-ac",
            "1",
            "-c:a",
            "pcm_s16le",
            output_file,
        ]
    )
