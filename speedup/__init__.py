from typing import Callable, Optional
from numpy.typing import ArrayLike
import soundfile as sf
import numpy as np
import scipy.signal

speedup: Callable[[ArrayLike, float], ArrayLike]
speedup = lambda audio, multiplier: scipy.signal.resample(audio, int(np.size(audio) * (1 / multiplier)))

def speedup_file(
	input_file: str,
	multiplier: float,
	file_ext = "mp3",
	output_file: Optional[str] = None
) -> None:
	if file_ext not in ("wav", "mp3"):
		raise ValueError("file_ext is not one of ('wav', 'mp3')")
	input_filename = input_file[:input_file.index('.')]
	if output_file is None:
		output_file = f"{input_filename}-spedup-{multiplier}x.{file_ext}"
	audio, samplerate = sf.read(input_file)
	spedup_audio = speedup(audio, multiplier)
	sf.write(output_file, spedup_audio, samplerate)

def main() -> None:
	from sys import argv, stderr

	bold: Callable[[str], str]
	bold = lambda s: f"\x1b[1m{s}\x1b[0m"

	USAGE = f"""{bold('Usage:')} {argv[0]} <audio_file> <multiplier> [file_ext]
	audio_file:
		the file containing audio to speed up
	multiplier:
		the speed multiplier, aka multiply the audio's speed by <multiplier>
	file_ext:
		must be one of ('mp3', 'wav')
		default: 'mp3'"""

	if len(argv) < 2:
		print(USAGE, file=stderr)
		exit(1)

	input_file = argv[1]
	multiplier = float(argv[2])
	try:
		file_ext = argv[3]
	except IndexError:
		file_ext = "mp3"

	try:
		speedup_file(input_file, multiplier, file_ext)
	except ValueError as err:
		print(f"{bold('Error:')} {err}", file=stderr)
		print(USAGE, file=stderr)

if __name__ == "__main__":
	main()
