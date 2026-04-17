import os
import shutil
import logging
import config


# Configure logging
logging.basicConfig(
    filename=config.LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def organize_screenshots(target_dir):
    logging.info(f"Starting screenshot organization in '{target_dir}'...")

    try:
        if not os.path.exists(config.SCREENSHOTS_DIR):
            os.makedirs(config.SCREENSHOTS_DIR)
            logging.info(f"Created directory: {config.SCREENSHOTS_DIR}")

        files_moved = 0

        for filename in os.listdir(target_dir):
            source_path = os.path.join(target_dir, filename)

            if os.path.isfile(source_path) and "screenshot" in filename.lower():
                dest_path = os.path.join(config.SCREENSHOTS_DIR, filename)

                shutil.move(source_path, dest_path)
                logging.info(f"Moved screenshot '{filename}'")
                files_moved += 1

        logging.info(f"Screenshot organization complete. Moved {files_moved} files.")

    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")


# Main execution
if __name__ == "__main__":
    organize_screenshots(config.BASE_DIR)
