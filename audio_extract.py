#!/usr/bin/python3
import sys
import os
import subprocess

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'youtube_dl'])

def downloader(url):
    os.system(f"youtube-dl -f bestaudio --extract-audio --audio-format mp3 --audio-quality 0 {url}")

if __name__ == "__main__":
    url = (sys.argv[1])
    downloader(url)
