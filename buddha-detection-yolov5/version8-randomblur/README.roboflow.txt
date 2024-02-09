
Buddha Poses Detection - v8 RandomBlurred
==============================

This dataset was annotated via roboflow.com 

The dataset includes 1013 images.
The dataset was split into train-test-validation in a 70-15-15 ration.
Buddha-poses are annotated in YOLO v5 PyTorch format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 416x416 (Stretch)
* Auto-contrast via histogram equalization - with minimal effect on the images

The following augmentation was applied to create 3 versions of each source image:
* Random Gaussian blur of between 0 and 2.8 pixels
