import cv2
import os
import numpy as np

'''
This script was written to apply Gaussian blur to a set of images 
and duplicate the corresponding labels for the blurred images.

Do not run, the script was used to create the folder "version8-gaussianblur"
'''
def apply_gaussian_blur(input_folder, output_folder, sigma=1.0):
    # Create output folders if they don't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png')):  # Assuming images are in these formats
            image_path = os.path.join(input_folder, filename)

            # Read the image
            multires1_image = cv2.imread(image_path)

            # Apply Gaussian blur
            blurred_image = cv2.GaussianBlur(multires1_image, (3, 3), sigma)

            # Save the blurred image to the output folder
            output_path = os.path.join(output_folder, f"blurred_{filename}")
            cv2.imwrite(output_path, blurred_image)

def duplicate_labels(input_labels_folder, output_labels_folder, num_duplicates):
    # Create output folder if it doesn't exist
    os.makedirs(output_labels_folder, exist_ok=True)

    # Iterate through each file in the input labels folder
    for filename in os.listdir(input_labels_folder):
        if filename.endswith('.txt'):
            label_path = os.path.join(input_labels_folder, filename)

            # Read the multires1 label file
            with open(label_path, 'r') as file:
                multires1_labels = file.read()

            # Duplicate the labels for the specified number of times
            duplicated_labels = multires1_labels * (num_duplicates - 1)

            # Save the duplicated labels to the output folder with a new filename
            output_path = os.path.join(output_labels_folder, f"blurred_{filename}")
            with open(output_path, 'w') as file:
                file.write(duplicated_labels)

if __name__ == "__main__":
    # Set your input and output folders
    train_images_folder = "buddha-detection-yolov5\\version8-original\\train\images"
    train_labels_folder = "buddha-detection-yolov5\\version8-original\\train\labels"
    train_output_images_folder = "buddha-detection-yolov5\\version8-multires1\\train\images"
    train_output_labels_folder = "buddha-detection-yolov5\\version8-multires1\\train\labels"

    # Apply Gaussian blur to train images
    apply_gaussian_blur(train_images_folder, train_output_images_folder)

    # Duplicate train labels for the corresponding blurred images
    num_train_images = len(os.listdir(train_images_folder))
    duplicate_labels(train_labels_folder, train_output_labels_folder, 2)

    print("Processing complete.")
