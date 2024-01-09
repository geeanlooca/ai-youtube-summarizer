import argparse

import convert_audio
import yt_handling
import transcribe
import summarize
import os
import tqdm
import read_videos


def pipeline(url: str):
    info = yt_handling.get_video_info(url)
    subtitle_file = "./data/subs/" + info["title"] + ".vtt"
    transcription_file = "./data/transcriptions/" + info["title"] + ".txt"
    audio_file = "./data/audio/" + info["title"] + "-original"
    converted_audio_file = "./data/audio/" + info["title"] + "-converted.wav"
    summary_file = "./data/summaries/" + info["title"] + ".txt"

    new_transcription = False

    if not os.path.exists(transcription_file):
        new_transcription = True
        if yt_handling.has_english_subs(info):
            yt_handling.download_subs(info, subtitle_file)

            with open(subtitle_file, "r") as file:
                lines = file.readlines()
            cleaned_subs = yt_handling.clean_downloaded_subs(lines)

            with open(transcription_file, "w") as file:
                file.writelines(cleaned_subs)

        else:
            yt_handling.download_audio(info, audio_file)
            convert_audio.convert_audio(audio_file, converted_audio_file)

            if transcription_file.endswith(".txt"):
                transcription_output_file = transcription_file[:-4]
            else:
                transcription_output_file = transcription_file

            transcribe.transcribe(converted_audio_file, transcription_output_file)

    if not os.path.exists(summary_file) or new_transcription:
        with open(transcription_file, "r") as file:
            transcription = file.read()

        summary = summarize.summarize(transcription)
        with open(summary_file, "w") as file:
            file.writelines(summary)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Perfom the entire pipeline for the given video URL"
    )
    parser.add_argument(
        "input", type=str, help="the video URL or the file containing the video URLs"
    )
    args = parser.parse_args()

    input_arg = args.input

    try:
        if os.path.isfile(input_arg):
            urls = read_videos.read_videos(input_arg)
            for url in tqdm.tqdm(urls):
                try:
                    pipeline(url)
                except Exception as e:
                    print(f"Encountered exception: {e}")
        else:
            pipeline(input_arg)
    except Exception as e:
        print(f"Encountered exception: {e}")
