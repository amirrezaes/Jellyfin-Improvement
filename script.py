import os
import subprocess
import psutil
import time

def check_cpu_idle(threshold=10):
    cpu_percent = psutil.cpu_percent(interval=1)
    return cpu_percent < threshold

def convert_to_hevc(input_dir, output_dir):

    # Get a list of all video files in the input directory
    video_files = [
        file for file in os.listdir(input_dir)
        if file.lower().endswith(('.mp4', '.avi', '.mkv', '.mov'))
    ]

    # Iterate over each video file and convert it to HEVC
    for file in video_files:
        while not check_cpu_idle(threshold=10):
            time.sleep(100)  # Wait for 100 seconds before checking CPU usage again

        input_path = os.path.join(input_dir, file)
        output_path = os.path.join(output_dir, f"{os.path.splitext(file)[0]}.hevc.mp4")


        command = [
            "ffmpeg",
            "-i", input_path,
            "-c:v", "libx265",
            "-crf", "23",
            "-preset", "medium",
            "-c:a", "copy",
            output_path
        ]


        subprocess.run(command)

    print("Conversion complete.")


input_directory = "/path/to/input/directory"
output_directory = "/path/to/output/directory"

convert_to_hevc(input_directory, output_directory)