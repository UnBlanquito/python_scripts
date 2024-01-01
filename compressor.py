import sys
from PIL import Image
import os


def compress_archive(path):
    path = str(path)
    folder_focus = os.path.join(os.path.expanduser("~"), f"{path}/")
    try:
        for file in os.listdir(folder_focus):
            print(file)
            name, extension = os.path.splitext(folder_focus + file)
            if extension in [".jpg", ".jpeg", ".png"]:
                pinture = Image.open(folder_focus + file)
                pinture.save(
                    folder_focus + "compressed_" + file, optimize=True, quality=60
                )
    except FileNotFoundError as e:
        sys.exit("Folder path does not exist!")


if __name__ == "__main__":
    compress_archive("prueba")
