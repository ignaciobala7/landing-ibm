import urllib.request
import zipfile
import os
import subprocess
import shutil

url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
zip_path = "ffmpeg.zip"

if not os.path.exists("ffmpeg.exe"):
    print("Downloading ffmpeg...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(zip_path, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        
        print("Extracting ffmpeg...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            for file_info in zip_ref.infolist():
                if file_info.filename.endswith('ffmpeg.exe'):
                    file_info.filename = 'ffmpeg.exe'
                    zip_ref.extract(file_info, '.')
                    break
    except Exception as e:
        print(f"Error downloading ffmpeg: {e}")

input_video = r"C:\Users\ibala\Downloads\IBM Intitucional Corto 4k.mp4"
output_dir = r"Recursos\Videos"
os.makedirs(output_dir, exist_ok=True)
output_video = os.path.join(output_dir, "IBM_Comprimido.mp4")

if not os.path.exists(input_video):
    print(f"Error: Could not find input video at {input_video}")
    exit(1)

print(f"Compressing video from {input_video} to {output_video}...")
cmd = [
    'ffmpeg.exe', '-y', '-i', input_video, 
    '-vcodec', 'libx264', '-crf', '32', '-preset', 'fast', 
    '-vf', 'scale=-2:720', '-acodec', 'aac', '-b:a', '128k', 
    output_video
]

process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1, universal_newlines=True)
count = 0
for line in process.stdout:
    if 'time=' in line:
        count += 1
        if count % 20 == 0:
            print(line.strip(), flush=True)

process.wait()

print("Done! Cleaning up...")
try:
    if os.path.exists(zip_path):
        os.remove(zip_path)
except Exception as e:
    print(e)
print("Compression finished successfully!")
