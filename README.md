# Emo Button!

The desktop-based emo delivery system. Still VERY much a work-in-progress

## Preparing

### Prerequisites

You'll need to have `ffmpeg`, `python`, and `pip` installed.

### Install the necessary python packages

This will install the necessary python packages.

```Shell
pip install -r requirements.txt
```

### Configure `emotracks.py`

Set up the `tracks` array in the `emotracks.py` file with objects like this:

```JSON
{
    "id": "<the youtube id of the song>",
    "name": "<will be used as the file name>",
    "start": "<start time of the clip in the format HH:MM:SS>",
    "end": "<end time of the clip in the format HH:MM:SS>"
}
```

### Prep the clips

This will create mp3 clips of just the choruses of the songs in the `clips` folder.

```Shell
python prepare_clips.py
```

## TODO

- [ ] Random playback of the songs
- [ ] Trigger random playback on button push

