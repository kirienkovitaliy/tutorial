import re
import sys
import shutil
from pathlib import Path

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}

for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


def normalize(name):
    t_name = name.translate(TRANS)
    t_name = re.sub(r'\W', '_', t_name)
    return t_name.translate(TRANS)


CATEGORIES = {
    "images": [".jpeg", ".png", ".jpg", ".svg"],
    "video": [".avi", ".mp4", ".mov", ".mkv"],
    "documents": [".doc", ".docx", ".txt", ".pdf", ".xlsx", ".pptx"],
    "audio": [".mp3", ".ogg", ".wav", ".amr"],
    "archives": [".zip", ".gz", ".tar"],
    "others": [""],
}


def create_folders(path: Path):
    for name in CATEGORIES.keys():
        if not path.joinpath(name).exists():
            path.joinpath(name).mkdir()


def sort_files(path: Path):

    known_extensions = []
    unknow_extensions = []

    for file in path.glob("**/*"):
        new_name = file.with_name(
            normalize(file.stem)).with_suffix(file.suffix)
        if file.is_file():
            if file.suffix in CATEGORIES["images"]:
                file.rename(new_name)
                new_name.replace(path / "images" / new_name.name)
                known_extensions.append(file.suffix)

            elif file.suffix in CATEGORIES["video"]:
                file.rename(new_name)
                new_name.replace(path / "video" / new_name.name)
                known_extensions.append(file.suffix)

            elif file.suffix in CATEGORIES["documents"]:
                file.rename(new_name)
                new_name.replace(path / "documents" / new_name.name)
                known_extensions.append(file.suffix)

            elif file.suffix in CATEGORIES["audio"]:
                file.rename(new_name)
                new_name.replace(path / "audio" / new_name.name)
                known_extensions.append(file.suffix)

            elif file.suffix in CATEGORIES["archives"]:
                file.rename(new_name)
                new_name.replace(path / "archives" / new_name.name)
                known_extensions.append(file.suffix)

            else:
                file.rename(new_name)
                new_name.replace(path / "others" / new_name.name)
                unknow_extensions.append(file.suffix)

    return known_extensions, unknow_extensions


def del_folders(path: Path):
    for f in list(path.glob("*/**"))[::-1]:
        if f.is_dir:
            try:
                f.rmdir()
            except OSError:
                pass


def unpack_archives(path: Path):
    path_folder = path / "archives"
    for f in path_folder.iterdir():
        shutil.unpack_archive(f, path / "archives" / f.stem)


def get_path():
    try:
        return Path(sys.argv[1])
    except IndexError:
        print("Path is not valid, try again ")
        return None


def main(path: Path):
    create_folders(path)
    sort_files(path)
    del_folders(path)
    unpack_archives(path)


if __name__ == "__main__":
    path = get_path()

    if path:
        main(path)
