import os
import json
from pathlib import Path

downloads_path = Path.home() / "Downloads"
json_path = Path('filetypes.json')

# Check if the json file exists
if not json_path.exists():
    raise FileNotFoundError("The 'filetypes.json' file is missing. Please make sure it exists.")

# Use context managers to read the json data
with json_path.open('r') as json_file:
    data = json.load(json_file)

soundarray = tuple(data.get('sound_type', ()))
videoarray = tuple(data.get('video_type', ()))
programarray = tuple(data.get('program_type', ()))
compressedarray = tuple(data.get('compressed_file_type', ()))
imgarray = tuple(data.get('img_type', ()))
txtarray = tuple(data.get('txt_type', ()))

# Define file type mappings to target directories
file_type_mapping = {
    imgarray: 'downloaded_images',
    txtarray: 'downloaded_text_files',
    soundarray: 'downloaded_sounds',
    videoarray: 'downloaded_videos',
    programarray: 'downloaded_programs',
    compressedarray: 'downloaded_compressed_files',
}

# Create directories if they don't exist
for directory in file_type_mapping.values():
    dir_path = downloads_path / directory
    dir_path.mkdir(parents=True, exist_ok=True)

# Move files to appropriate directories
for file in downloads_path.iterdir():
    if not file.is_file():
        continue

    lower_filename = file.name.lower()
    for file_type, target_directory in file_type_mapping.items():
        if lower_filename.endswith(file_type) or lower_filename == file_type:
            new_path = downloads_path / target_directory / file.name
            file.rename(new_path)
            break
    else:
        # If no match found, the file type is not in the JSON data, move it to a default directory
        default_directory = downloads_path / 'other_files'
        default_directory.mkdir(exist_ok=True)
        new_path = default_directory / file.name
        file.rename(new_path)
