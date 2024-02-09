### **version8-randomblur**

This folder contains annotated images from the buddha-poses dataset, resized to 416x416 pixels.
- The dataset includes 1013 images.
- The dataset was split into train-test-validation in a 70-15-15 ratio following which the train set was augmented.
- Buddha-poses are annotated in YOLO v5 PyTorch format.


We used Roboflow to annotate and resize the image dataset, and hence the images can also be found on:
https://app.roboflow.com/warburg-buddha-poses/buddha-poses-detection/8

The following operations were done on the original images (uploaded by us):
- resize to 416x416 (Stretch)
- auto-contrast via histogram equalization - with minimal effect on the images
- Random Gaussian blur of between 0 and 2.8 pixels to create 3 copies of each train image.