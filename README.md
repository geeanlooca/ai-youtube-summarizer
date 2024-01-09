# AI Youtube summarizer

A Python project that uses AI models to summarize the content of YouTube videos.


## Technology
At the moment, `yt-dlp` is used to download the subtitles and audio track of YouTube videos, `ffmpeg` is used to convert the audio track,
`whisper.cpp` is used to transcribe the audio track locally, and OpenAI's API are used to summarize the transcription.

You'll probably need to have `ffmpeg` installed, along with a C compiler for compiling `whisper.cpp`, and optionally OpenBLAS.


## Example
Take this [falafel sandwich recipe video](https://www.youtube.com/watch?v=9RGbr9m-uCY). Using the `gpt-3.5-turbo-16k` model, the resulting summary is the following:

>``` In this video, the host provides tips and tricks for making the most flavorful chickpea falafel in a regular home kitchen. The host discusses the mistakes that many home cooks make when preparing falafel and how to avoid them. They also explain the importance of using dried chickpeas instead of canned ones to ensure the falafel holds together and has the desired texture. The host goes on to demonstrate how to make the batter by blending fresh herbs, vegetables, and the hydrated chickpeas. They emphasize the importance of not over-processing the batter to maintain a light and fluffy texture.  The video also provides instructions on freezing parts of the batter for future use and seasoning the batter before frying. The host explains the process of deep-frying the falafel to achieve a crispy exterior while preventing them from falling apart or becoming too oily. They provide tips for achieving the correct frying temperature and cooking time. The host also suggests making a dimple in the falafel to ensure even cooking.  Additionally, the video includes instructions for making fresh pita bread and three different salads to accompany the falafel. The first salad is a quick pickled red cabbage for tanginess and crunch. The second salad consists of onions macerated with chili sauce for a spicy kick. The third salad is an Arabic salad made with diced cucumber, tomato, and red onion for freshness. The video concludes with a tutorial on making a creamy tahini sauce to drizzle over the falafel sandwich.  Overall, the video provides a comprehensive guide to making homemade falafel that matches the quality of restaurant falafel. It emphasizes the importance of using the right ingredients, techniques, and seasoning and demonstrates how to assemble the ultimate falafel sandwich.  ```