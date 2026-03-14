"""
Level 3 Task 3: Automation Script
Automatically organizes files into folders based on extension.
"""

import os
import shutil


def organize_files(folder):

    for filename in os.listdir(folder):

        file_path = os.path.join(folder, filename)

        if os.path.isfile(file_path):

            extension = filename.split(".")[-1].lower()

            folder_map = {
                "jpg": "Images",
                "pdf": "Documents",
                "txt": "Text",
                "csv": "Data"
            }

            if extension in folder_map:

                new_folder = os.path.join(folder, folder_map[extension])

                os.makedirs(new_folder, exist_ok=True)

                shutil.move(file_path, os.path.join(new_folder, filename))


def main():

    folder = input("Enter folder path to organize: ")

    organize_files(folder)

    print("Files organized successfully!")


if __name__ == "__main__":
    main()