# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 18:03:55 2020

@author: markm
"""

#Not currently used, but may one day be implemented. It would return mp3's instead of url's. I
#am unsure if I want to offer that functionality or not.
from __future__ import unicode_literals
import youtube_dl


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=CvFH_6DNRCY'])