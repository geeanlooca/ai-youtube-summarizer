# AI Youtube summarizer

A Python project that uses AI models to summarize the content of YouTube videos.


## Technology
At the moment, `yt-dlp` is used to download the subtitles and audio track of YouTube videos, `ffmpeg` is used to convert the audio track,
`whisper.cpp` is used to transcribe the audio track locally, and OpenAI's API are used to summarize the transcription.


