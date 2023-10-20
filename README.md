# speedup.py
A simple script to speedup your music/audio

## Installation
```
pip install speedup.py
```

## Usage
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

## Build from source
```
git clone https://github.com/trustytrojan/speedup.py
cd speedup.py
sh devsetup.sh
python -m build
```
