import vlc  # Load the popular external library
from os import listdir
from os.path import isfile, join
from random import choice
from time import sleep
from mutagen.mp3 import MP3


def main():
    files = [f for f in listdir('clips') if isfile(
        join('clips', f))]
    files = list(filter(lambda x: x != 'blank', files))
    randomFile = choice(files)

    length = MP3('clips/{}'.format(randomFile)).info.length

    p = vlc.MediaPlayer('clips/{}'.format(randomFile))
    p.play()
    sleep(length+1)


if __name__ == "__main__":
    main()
