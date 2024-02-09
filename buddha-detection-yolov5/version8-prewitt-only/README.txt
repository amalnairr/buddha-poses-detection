
Buddha Poses Detection - v8 Prewitt ONLY
==========================================

The dataset includes 441 images.
The dataset is split into train-test-validation subsets in the proportion 70-15-15%.
The images from version8 - original were treated with Prewitt filter
Buddha-poses are annotated in YOLO v5 PyTorch format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 416x416 (Stretch)
* Prewitt Filtering


