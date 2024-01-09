import argparse
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

SYSTEM_ROLE = """You are a summarization assistant, skilled in summarizing potentially complex text generated from audio. 
Be careful not to exclude important concepts and ideas in favor of irrelevant details. Make the text as long as you deem necessary.
If you see some products or services being advertised, you must ignore them from the summary."""


def summarize(transcription: str):
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": SYSTEM_ROLE},
            {"role": "user", "content": f"{transcription}"},
        ],
        stream=True,
    )

    summary = []

    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            portion = chunk.choices[0].delta.content
            print(portion, end="")
            summary.append(portion)

    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Summarize text")
    parser.add_argument(
        "transcription_file",
        metavar="transcription_file",
        type=str,
        help="the transcription file",
    )
    args = parser.parse_args()
    transcription_file = args.transcription_file

    with open(transcription_file, "r") as file:
        transcription = file.read()
        summarize(transcription)
