import sys
import subprocess

if len(sys.argv) != 4:
    print("Usage: python wav2lip_runner.py <video_path> <audio_path> <output_path>")
    sys.exit(1)

video_path = sys.argv[1]
audio_path = sys.argv[2]
output_path = sys.argv[3]

command = [
    "conda", "run", "-n", "wave_env", "python", "Wav2Lip/inference.py",
    "--checkpoint_path", "Wav2Lip/checkpoints/wav2lip_gan.pth",
    "--face", video_path,
    "--audio", audio_path,
    "--outfile", output_path,
    "--pads", "0", "20", "0", "0",
    "--resize_factor", "4",
    "--nosmooth"
]

subprocess.run(command, check=True)
