import os
import shutil
import logging

logging.basicConfig(level=logging.INFO)

def organize_screenshots_static():
    target_dir = "/home/user/Downloads"
    screenshots_dir = "/home/user/Downloads/Screenshots"

    logging.info("Starting screenshot organization...")

    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)
        logging.info("Created Screenshots directory")

    files_moved = 0
    for filename in os.listdir(target_dir):
        source_path = target_dir + "/" + filename

        if os.path.isfile(source_path) and "screenshot" in filename.lower():
            dest_path = screenshots_dir + "/" + filename
            shutil.move(source_path, dest_path)
            files_moved += 1

    logging.info(f"Moved {files_moved} screenshot files")
