import os
import shutil


def organize_screenshots_static():
    target_dir = "/home/user/Downloads"
    screenshots_dir = "/home/user/Downloads/Screenshots"

    try:
        # Create Screenshots folder if it doesn't exist
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
            print("Created folder:", screenshots_dir)

        # Loop through files in Downloads
        for filename in os.listdir(target_dir):
            source_path = os.path.join(target_dir, filename)

            # Check if it's a file and contains 'screenshot'
            if os.path.isfile(source_path) and "screenshot" in filename.lower():
                dest_path = os.path.join(screenshots_dir, filename)

                shutil.move(source_path, dest_path)
                print(f"Moved: {filename}")

        print("Screenshot organization completed.")

    except Exception as e:
        print("Error occurred:", str(e))


# Main execution
if __name__ == "__main__":
    organize_screenshots_static()
