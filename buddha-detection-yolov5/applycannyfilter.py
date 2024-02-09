import cv2
import os
import numpy as np

def apply_canny_filter(input_folder, output_folder, low_threshold, high_threshold):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png')):  # Assuming images are in these formats
            image_path = os.path.join(input_folder, filename)

            # Read the image
            original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            # Apply Canny edge detection
            edges = cv2.Canny(original_image, low_threshold, high_threshold)

            # Save the Canny-filtered image to the output folder
            output_path = os.path.join(output_folder, f"canny_{filename}")
            cv2.imwrite(output_path, edges)

def duplicate_labels(input_labels_folder, output_labels_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_labels_folder, exist_ok=True)

    # Iterate through each file in the input labels folder
    for filename in os.listdir(input_labels_folder):
        if filename.endswith('.txt'):
            label_path = os.path.join(input_labels_folder, filename)

            # Read the original label file
            with open(label_path, 'r') as file:
                original_labels = file.read()

            # Duplicate the labels for the specified number of times
            duplicated_labels = original_labels

            # Save the duplicated labels to the output folder with a new filename
            output_path = os.path.join(output_labels_folder, f"canny_{filename}")
            with open(output_path, 'w') as file:
                file.write(duplicated_labels)

if __name__ == "__main__":
    # Set your input and output folders
    train_images_folder = "buddha-detection-yolov5\\version8-original\\train\images"
    train_labels_folder = "buddha-detection-yolov5\\version8-original\\train\labels"
    train_output_images_folder = "buddha-detection-yolov5\\version8-canny-high\\train\images"
    train_output_labels_folder = "buddha-detection-yolov5\\version8-canny-high\\train\labels"
    
    # Set Canny edge detection parameters
    low_threshold = 80
    high_threshold = 110

    # Apply Canny filter to train images
    apply_canny_filter(train_images_folder, train_output_images_folder, low_threshold, high_threshold)

    # Duplicate train labels for the corresponding Canny-filtered images
    duplicate_labels(train_labels_folder, train_output_labels_folder)
    # Repeat the process for test and val sets if needed
    # ...

    print("Processing complete.")
