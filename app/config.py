import os
import torch
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

VIDEO_PATH = r'D:\AI\AI_projects\graduate_project\videos\before\test22.mp4'
OUTPUT_VIDEO_PATH = r"D:/AI/AI_projects/graduate_project/after/translated_output.mp4"
SPEAKER_AUDIO_PATH = r"D:\AI\AI_projects\graduate_project\videos\audio\extracted_audio.mp3"
XTTS_AUDIO_OUTPUT = r"D:\AI\AI_projects\graduate_project\after\xtts_output.wav"

DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"
TORCH_DTYPE = torch.float16 if torch.cuda.is_available() else torch.float32
