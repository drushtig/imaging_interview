# Image Comparison Project

This project contains a set of scripts for finding and moving similar images from a source folder to a destination folder.

## Requirements

Python 3.7+
OpenCV
PyYAML
imaging_interview

## Data Format

The images are in PNG format. Each image file is named following the pattern: c%camera_id%-%timestamp%.png. The timestamp is in either of two formats.


## Installation

1. Install the necessary packages by running `pip install -r requirements.txt`.
2. Update the `source_folder` and `destination_folder` variables in `config.yaml` with the paths to your source and destination folders.
3. Run `python main.py` to start the image processing script.

This script will process all images in the source folder, compare each image with the next one, and move similar images to the destination folder. The similarity of images is determined by a threshold value. If the score of the comparison is less than the threshold, the images are considered similar.


## Additional information

This project uses the Black code formatter to ensure consistent and readable code style. To format your code with Black, run:

```bash

black main.py utilities.py

