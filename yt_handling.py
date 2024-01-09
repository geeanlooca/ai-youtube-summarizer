import os
import yt_dlp
import logging
from typing import List


class loggerOutputs:
    def error(msg):
        print("Captured Error: " + msg)

    def warning(msg):
        print("Captured Warning: " + msg)

    def debug(msg):
        print("Captured Log: " + msg)


def clean_downloaded_subs(subtitle_lines: List[str]) -> List[str]:
    """Clean the downloaded subtitles"""

    # first divide the lines into chunks separated by empty lines
    chunks = []
    current_chunk = []
    for line in subtitle_lines:
        if line == "\n":
            chunks.append(current_chunk)
            current_chunk = []
        else:
            current_chunk.append(line)

    # throw away the first chunk (metadata)
    chunks = chunks[1:]

    # throw away the first line of each chunk (timestamp)
    chunks = [chunk[1:] for chunk in chunks]

    # join the chunks into a single list
    lines = []
    for chunk in chunks:
        lines.extend(chunk)

    # remove the newlines
    lines = [line.strip() for line in lines]

    return lines


def download_audio(video_info: dict, output_filename: str):
    """Download audio for a video"""

    formats = video_info["formats"]
    audio_formats = [f for f in formats if f["resolution"] == "audio only"]

    # remove entries without filesize
    audio_formats = [f for f in audio_formats if "filesize" in f]

    audio_format = sorted(audio_formats, key=lambda f: f["filesize"])

    selected_format = audio_format[0]
    selected_id = selected_format["format_id"]

    opts = {"format": selected_id, "outtmpl": output_filename, "quiet": True}

    with yt_dlp.YoutubeDL(opts) as ydl:
        err = ydl.download([video_info["webpage_url"]])
        print(err)


def has_english_subs(video_info: dict) -> bool:
    if video_info["subtitles"] is None:
        logging.warning("No subtitles")
        return False

    return any(lang.startswith("en") for lang in video_info["subtitles"])


def download_subs(video_info: dict, output_filename: str):
    yt_opts = {
        "skip_download": True,
        "writesubtitles": True,
        "subtitlesformat": "vtt",
        "quiet": True,
        "outtmpl": "tmp_sub",
    }

    """Download subtitles for a video"""
    with yt_dlp.YoutubeDL(yt_opts) as ydl:
        info = ydl.extract_info(video_info["webpage_url"], download=False)
        err = ydl.download([info["webpage_url"]])

        # find the file with name starting with the template
        files = os.listdir()
        for file in files:
            if file.startswith("tmp_sub"):
                os.rename(file, output_filename)
                break


def get_video_info(url: str):
    """Get video info from YouTube"""
    yt_opts = {
        "quiet": True,
    }
    with yt_dlp.YoutubeDL(yt_opts) as ydl:
        return ydl.extract_info(url, download=False)
