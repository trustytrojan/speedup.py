# speedup.py
A simple script to speedup your music/audio.

## Installation
To install `speedup.py` on either your system or a Python virtual environment, run:
```
pip install speedup.py
```

## Usage
General commandline usage of `speedup.py` is below. This is printed when not enough arguments are given.
```
speedup <audio_file> <multiplier> [file_ext]
	audio_file:
		the file containing audio to speed up
	multiplier:
		the speed multiplier, aka multiply the audio's speed by <multiplier>
	file_ext:
		must be one of ('mp3', 'wav')
		default: 'wav'
```

### Example usage
To speedup `audio.mp3` by a factor of `1.5`, run:
```
speedup audio.mp3 1.5
```
By default the sped up audio is saved as a `.wav` file. To save it as an `mp3` file, run:
```
speedup audio.mp3 1.5 mp3
```

## Build from source
To build the project from source into a `.whl` file, run the below commands in your terminal:
```
git clone https://github.com/trustytrojan/speedup.py
cd speedup.py
sh devsetup.sh
python -m build
```
