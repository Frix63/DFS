import os
import pathlib
from pathlib import Path

downloads_path = str(Path.home() / "Downloads")

img_type = ('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif', 'raw', '.heif', '.jfif', '.exif', '.webp', '.svg', '.ico', '.psd', '.arw')

txt_type = ('.txt', '.docx', '.doc', '.pdf', '.pptx', '.ppt', '.xlsx', '.xls', '.csv', '.xml', '.json', '.html', '.htm', '.md', '.odt', '.ods', '.odp', '.odg', '.odf', '.rtf', '.tex', '.wpd', '.wps', '.xps', '.key', '.pages', '.numbers', '.c', '.cpp', '.py', '.java', '.class', '.cs', '.vb', '.js', '.ts', '.css', '.scss', '.less', '.php', '.sql', '.swift', '.go', '.rb', '.pl', '.m', '.h', '.vb', '.vbs', '.bat', '.cmd', '.ps1', '.psm1', '.sh', '.bash', '.bashrc', '.bash_profile', '.zsh', '.zshrc', '.zprofile', '.zlogin', '.zlogout', '.zshenv', '.zsh-theme', '.zshrc', '.zsh-update', '.zwc', '.zcompdump', '.zcompdump.zwc', '.zsh_history', '.zshrc', '.zshrc.local', '.zshrc~', '.zshrc-e', '.zshrc.pre-oh-my-zsh', '.zshrc.pre-oh-my-zsh~', '.zshrc.pre-oh-my-zsh-e', '.zshrc.pre-oh-my-zsh-e~', '.zshrc.pre-oh-my-zsh~', '.zshrc.pre-oh-my-zsh-e', '.zshrc.pre-oh-my-zsh-e~', '.zshrc.pre-oh-my-zsh', '.zshrc.pre-oh-my-zsh~', '.zshrc.pre-oh-my-zsh-e', '.zshrc.pre-oh-my-zsh-e~', '.zshrc.pre-oh-my-zsh', '.zshrc.pre-oh-my-zsh~', '.zshrc.pre-oh-my-zsh-e', '.zshrc.pre-oh-my-zsh-e~', '.zshrc.pre-oh-my-zsh', '.zshrc.pre-oh-my-zsh~', '.zshrc.pre-oh-my-zsh-e', '.zshrc.pre-oh-my-zsh-e~', '.zshrc.pre')

sound_type = ('.mp3', '.flac',  '.wav', '.wma', '.aac', '.aiff', '.alac', '.dsd', '.mp2', '.m4a', '.m4p', '.m4b', '.m4r', '.ogg', '.oga', '.opus', '.webm', '.3gp', '.midi', '.mka', '.mks', '.ra', '.ram', '.rm', '.rv', '.ts', '.vob', '.m3u', '.m3u8', '.pls', '.asx', '.xspf', '.wpl', '.zpl', '.flp')

video_type = ('.mp4', '.mov', '.wmv', '.flv', '.avi', '.avchd', '.webm', '.mkv', '.m4v', '.m4p', '.m4b', '.m4r', '.m4a', '.ogg', '.oga', '.ogv', '.ogx', '.qt', '.rm', '.rmvb', '.vob', '.3gp', '.3g2', '.mxf', '.roq', '.nsv', '.f4v', '.f4p', '.f4a', '.f4b')

program_type = ('.exe', '.msi', '.apk', '.app', '.bat', '.bin', '.cgi', '.com', '.gadget', '.jar', '.w')

compressed_file_type = ('.rar', '.zip', '.7z', '.tar', '.gz', '.bz2', '.xz', '.lz', '.lzma', '.cab', '.iso', '.dmg', '.vhd', '.vmdk', '.vdi', '.hfs', '.wim', '.swm', '.z', '.zpaq', '.zz', '.zst', '.zstd', '.tzst', '.zfp', '.zbf', '.zab', '.zlib', '.zst', '.zstd', '.tzst', '.zfp', '.zbf', '.zab', '.zlib', '.z', '.zpaq', '.zz', '.zst', '.zstd', '.tzst', '.zfp', '.zbf', '.zab', '.zlib', '.z', '.zpaq', '.zz', '.zst', '.zstd', '.tzst', '.zfp', '.zbf', '.zab', '.zlib', '.z', '.zpaq', '.zz', '.zst', '.zstd', '.tzst', '.zfp', '.zbf', '.zab', '.zlib', '.z', '.zpaq', '.zz', '.zst', '.zstd', '.tzst', '.zfp', '.zbf', '.zab', '.zlib', '.z', '.zpaq', '.zz', '.zst', '.zstd', '.tzst', '.zfp', '.zbf', '.zab', '.zlib', '.z', '.zpaq', '.zz', '.zst', '.zstd', '.tzst', '.zfp', '.zbf', '.zab', '.zlib', '.z', '.zpaq', '.zz', '.zst', '.zstd', '.tzst', '.zfp', '.zbf', '.zab', '.zlib', '.z', '.zpaq', '.zz', '.zst', '.zstd', '.tzst', '.zfp', '.zbf', '.zab', '.zlib')

if not os.path.exists(downloads_path + '\\downloaded_images'):
    os.mkdir(downloads_path + '\\downloaded_images')
if not os.path.exists(downloads_path + '\\downloaded_text_files'):
    os.mkdir(downloads_path + '\\downloaded_text_files')
if not os.path.exists(downloads_path + '\\downloaded_sounds'):
    os.mkdir(downloads_path + '\\downloaded_sounds')
if not os.path.exists(downloads_path + '\\downloaded_videos'):
    os.mkdir(downloads_path + '\\downloaded_videos')
if not os.path.exists(downloads_path + '\\downloaded_programs'):
    os.mkdir(downloads_path + '\\downloaded_programs')
if not os.path.exists(downloads_path + '\\downloaded_compressed_files'):
    os.mkdir(downloads_path + '\\downloaded_compressed_files')

for files in os.listdir(downloads_path):
    files = files.lower()
    if files.endswith(img_type):
        old_path = os.path.join(downloads_path, files)
        new_path = os.path.join(downloads_path, 'downloaded_images', files)
        pathlib.Path(old_path).rename(new_path)
    elif files.endswith(txt_type):
        old_path = os.path.join(downloads_path, files)
        new_path = os.path.join(downloads_path, 'downloaded_text_files', files)
        pathlib.Path(old_path).rename(new_path)
    elif files.endswith(sound_type):
        old_path = os.path.join(downloads_path, files)
        new_path = os.path.join(downloads_path, 'downloaded_sounds', files)
        pathlib.Path(old_path).rename(new_path)
    elif files.endswith(video_type):
        old_path = os.path.join(downloads_path, files)
        new_path = os.path.join(downloads_path, 'downloaded_videos', files)
        pathlib.Path(old_path).rename(new_path)
    elif files.endswith(program_type):
        old_path = os.path.join(downloads_path, files)
        new_path = os.path.join(downloads_path, 'downloaded_programs', files)
        pathlib.Path(old_path).rename(new_path)
    elif files.endswith(compressed_file_type):
        old_path = os.path.join(downloads_path, files)
        new_path = os.path.join(downloads_path, 'downloaded_compressed_files', files)
        pathlib.Path(old_path).rename(new_path)
    else:
        continue
