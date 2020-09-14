from __future__ import unicode_literals
import youtube_dl
import ffmpeg
from emotracks import tracks

for i in range(0, len(tracks)):
    ydl_opts = {
        "format": "bestaudio",
        "outtmpl": "tmp/%(id)s"
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([tracks[i]['id']])

    stream = ffmpeg.input("tmp/{}".format(tracks[i]['id']))
    stream = stream.filter(
        'atrim', start=tracks[i]['start'], end=tracks[i]['end'])
    stream = ffmpeg.output(stream, "clips/__{}.mp3".format(tracks[i]['name']))
    ffmpeg.run(stream)
