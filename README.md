# Warburg Institute Iconographic Database - YOLOv5 and YOLOv8 Pose Detection

## Overview

Welcome to the Warburg Institute Iconographic Database (IID) YOLOv5 and YOLOv8 Pose Detection Project! This project focuses on using YOLOv5 and YOLOv8 to detect poses of Buddha images within the extensive Warburg IID, specifically in the subset related to Buddhism and Lord Buddha's iconography.

## What is Iconography?

Iconography refers to the traditional or conventional images or symbols associated with a subject, especially religious or legendary subjects.

## [Warburg Institute Iconographic Database](https://iconographic.warburg.sas.ac.uk/home)

- The WI-ID hosts a rich collection of over 100,000 images.
- Our project specifically targets the subset related to [Buddhism and Lord Buddha's iconography](https://iconographic.warburg.sas.ac.uk/category/vpc-taxonomy-001747), which is a part of [Asian Iconography](https://iconographic.warburg.sas.ac.uk/category/vpc-taxonomy-000003).

## Dataset

The annotated dataset for this project contains images with various augmentations applied. They are organized as Separate Folders:

- Uniform Gaussian Blur
- Random Gaussian Blur
- Frewitt Filter
- Canny Edge Filter
- Multi-res Gaussian Filter

## Objectives

The primary goals of this project are to:

1. Evaluate the performance of YOLOv5 in detecting poses of Buddha in the Warburg IID.
2. Compare the performance of YOLOv8 with YOLOv5 in the same context.

## Project Structure

The project is organized as follows:

- **Dataset:** Contains annotated images with different augmentations.
- **Notebooks:** Holds Jupyter notebooks for YOLOv5 and YOLOv8 pose detection.
- **Results:** Stores the output and results of the detection process - Created at the end of each run. 
- **Documentation:** Any additional documents or reports related to the project.

## Getting Started with Colab Notebooks

1. **Open Colab Notebooks:**
   - Click on the Colab notebook links provided in the `Notebooks` folder.

2. **Run YOLOv5 Pose Detection:**
   - Open and run the `yolov5_pose_detection.ipynb` notebook.

3. **Run YOLOv8 Pose Detection:**
   - Open and run the `yolov8_pose_detection.ipynb` notebook.

## Results

Check the `Results` folder for the output of the detection process. Evaluate the performance and compare the results between YOLOv5 and YOLOv8.

## Contributions

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.

## License

This project is licensed under CC 4.0.

Feel free to reach out if you have any questions or need further assistance. Happy coding!
