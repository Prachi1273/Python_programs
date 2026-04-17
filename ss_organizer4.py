import os
import shutil
import config


def organize_screenshots(target_dir):
    try:
        # Create Screenshots folder if it doesn't exist
        if not os.path.exists(config.SCREENSHOTS_DIR):
            os.makedirs(config.SCREENSHOTS_DIR)
            print("Created folder:", config.SCREENSHOTS_DIR)

        # Loop through files in target directory
        for filename in os.listdir(target_dir):
            source_path = os.path.join(target_dir, filename)

            # Check if it's a file and contains 'screenshot'
            if os.path.isfile(source_path) and "screenshot" in filename.lower():
                dest_path = os.path.join(config.SCREENSHOTS_DIR, filename)

                shutil.move(source_path, dest_path)
                print(f"Moved: {filename}")

        print("Screenshot organization completed.")

    except Exception as e:
        print("Error occurred:", str(e))


# Main execution
if __name__ == "__main__":
    target_directory = config.BASE_DIR
    organize_screenshots(target_directory)
