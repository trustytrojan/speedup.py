# speedup.py
A simple script to speedup your music/audio

## Installation
Make sure you're not installing in a virtual environment.
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

## Building from source
Clone the repository:
```
git clone https://github.com/trustytrojan/speedup.py
```
Setup the development environment:
```
sh devsetup.sh
```
Build the wheel:
```
python -m build
```
