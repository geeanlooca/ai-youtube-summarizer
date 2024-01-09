import os
from dataclasses import dataclass
from typing import List


@dataclass
class VideoUrlInfo:
    url: str
    comment: str


# define new exception
class SkippedVideoUrl(Exception):
    def __init__(self, line: str):
        self.line = line

    def __str__(self):
        return f"Line {self.line} is skipped"


def parse_video_line(line: str) -> VideoUrlInfo:
    """Parse URL and comment from a line"""

    comment_separator = "#"
    line = line.strip()

    if line.startswith(comment_separator):
        raise SkippedVideoUrl(line)

    try:
        if comment_separator in line:
            url, comment = line.split(comment_separator)
        else:
            url = line
            comment = ""

        return VideoUrlInfo(url.strip(), comment.strip())
    except ValueError:
        print(f"Invalid line: {line}")


def read_videos(filename: str) -> List[str]:
    """Read the videos from the file"""
    videos = []
    if os.path.exists(filename):
        file = open(filename, "r")
        for line in file:
            line = line.strip()
            try:
                info = parse_video_line(line)
                videos.append(info.url)
            except SkippedVideoUrl:
                pass
        file.close()
    return videos
