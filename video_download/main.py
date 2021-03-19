from __future__ import unicode_literals
import youtube_dl
import colorama
import os
from os.path import expanduser, dirname, realpath, abspath
from .includes import *

# User Defined
videos_dir = "[videos]"
file_format_basename = "[%(uploader)s]-[%(upload_date)s]-[%(title)s]-[%(id)s]"
file_format_ext = ".%(ext)s"

# home = expanduser("~")
filepath = realpath(__file__)
sub_dir = dirname(realpath(__file__))
parent_dir = dirname(dirname(realpath(__file__)))
videos_dir = parent_dir + "/" + videos_dir + "/"


links = ["https://www.youtube.com/watch?v=BaW_jenozKc"]


def start():
    youtube_dl_options = {
        "outtmpl": videos_dir + file_format_basename + file_format_ext,
        "prefer_ffmpeg": True,
        "retries": 2,
        "keepvideo": False,
        "ignoreerrors": True,
        "addmetadata": True,
        "noplaylist": True,
        "continuedl": False,
        "noprogress": True,
        "writedescription": True,
        "writeinfojson": True,

        "writesubtitles": True,
        "writeautomaticsub": True,
        "write-srt": True,
        "sub-lang": "en",
        "convert-subs": "srt",

        "add-video_infodata": True,
        "forcethumbnail": True,
        "writethumbnail": True,


    }
    with youtube_dl.YoutubeDL(youtube_dl_options) as ydl:
        ydl.download(links)
