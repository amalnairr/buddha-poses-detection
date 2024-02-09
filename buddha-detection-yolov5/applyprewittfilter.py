import cv2
import os
import numpy as np

def apply_prewitt_filter(input_folder, output_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Prewitt kernels for horizontal and vertical edges
    prewitt_kernel_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float32)
    prewitt_kernel_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]], dtype=np.float32)

    # Iterate through each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(input_folder, filename)

            # Read the image
            original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            # Apply Prewitt filter
            prewitt_x = cv2.filter2D(original_image, cv2.CV_64F, prewitt_kernel_x)
            prewitt_y = cv2.filter2D(original_image, cv2.CV_64F, prewitt_kernel_y)

            # Combine the x and y gradients to get the magnitude
            magnitude = np.sqrt(prewitt_x**2 + prewitt_y**2)

            # Normalize the magnitude to the range [0, 255]
            magnitude = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)

            # Convert to uint8 for display and saving
            magnitude = np.uint8(magnitude)

            # Save the Prewitt-filtered image to the output folder
            output_path = os.path.join(output_folder, f"prewitt_{filename}")
            cv2.imwrite(output_path, magnitude)

def duplicate_labels(input_labels_folder, output_labels_folder, num_duplicates):
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
            duplicated_labels = original_labels * num_duplicates

            # Save the duplicated labels to the output folder with a new filename
            output_path = os.path.join(output_labels_folder, f"prewitt_{filename}")
            with open(output_path, 'w') as file:
                file.write(duplicated_labels)

if __name__ == "__main__":
    # Set your input and output folders
    train_images_folder = "version8-original/valid/images"
    train_labels_folder = "version8-original/valid/labels"
    train_output_images_folder = "version8-prewitt-only/valid/images"
    train_output_labels_folder = "version8-prewitt-only/valid/labels"

    # Apply Prewitt filter to train images
    apply_prewitt_filter(train_images_folder, train_output_images_folder)

    # Duplicate train labels for the corresponding Prewitt-filtered images
    num_train_images = len(os.listdir(train_images_folder))
    duplicate_labels(train_labels_folder, train_output_labels_folder, 2)

    # Repeat the process for test and val sets if needed
    # ...

    print("Processing complete.")
