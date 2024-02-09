import os
import shutil

def merge_folders(source_folders, destination_folder):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Iterate through the source folders
    for source_folder in source_folders:
        # Iterate through the files and subdirectories in each source folder
        for item in os.listdir(source_folder):
            source_path = os.path.join(source_folder, item)
            destination_path = os.path.join(destination_folder, item)

            # If it's a file, move it to the destination
            if os.path.isfile(source_path):
                shutil.move(source_path, destination_path)
            # If it's a directory, recursively merge its contents
            elif os.path.isdir(source_path):
                merge_folders([source_path], destination_path)

if __name__ == "__main__":
    # Replace these paths with the paths of your source folders and destination folder
    source_folders = ['buddha-detection-yolov5\\version8-multires1', 'buddha-detection-yolov5\\version8-multires2', 'buddha-detection-yolov5\\version8-multires3', 'buddha-detection-yolov5\\version8-multires4']
    destination_folder = 'buddha-detection-yolov5\\version8-multiresolution'

    merge_folders(source_folders, destination_folder)
    print("Folders merged successfully!")
