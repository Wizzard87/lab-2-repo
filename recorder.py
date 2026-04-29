import subprocess
import os
import from os *
ffmpeg_path = r"D:\ffmpeg\ffmpeg.exe"

# 📁 Папка для сохранения
save_folder = r"D:\Recordings\new"

# создаём папку если её нет
os.makedirs(save_folder, exist_ok=True)

# имя файла
output_file = os.path.join(save_folder, "record.mp4")

command = [
    ffmpeg_path,
    "-f", "gdigrab",
    "-framerate", "30",
    "-video_size", "1920x1080",
    "-i", "desktop",
    "-c:v", "h264_nvenc",
    "-preset", "p5",
    "-b:v", "20M",
    "-pix_fmt", "yuv420p",
    output_file
]

subprocess.run(command)