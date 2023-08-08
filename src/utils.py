__author__      = "Drushti Gulhane"
__version__ = "1.0.1"
__maintainer__ = "Drushti Gulhane"
__email__ = "drushtimgulhane@gmail.com"
__status__ = "Dev"


import cv2
import os
import re
import shutil
from imaging_interview import (
    preprocess_image_change_detection,
    compare_frames_change_detection,
)


def extract_camera_id_and_timestamp(filename):
    """
    Extracts the camera ID and timestamp from a given filename.

    Args:
        filename (str): The filename to extract the camera ID and timestamp from.

    Returns:
        tuple: A tuple containing the camera ID and timestamp. If the filename does not match the expected format, returns (0, 0).
    """
    pattern = r"c(\d+)-(\d+).png"
    match = re.match(pattern, filename)
    if match:
        camera_id, timestamp = match.groups()
        return int(camera_id), int(timestamp)
    else:
        return 0, 0


def compare_images(image_path1, image_path2):
    """
    Compares two images and returns a score indicating their similarity.

    Args:
        image_path1 (str): The file path of the first image.
        image_path2 (str): The file path of the second image.

    Returns:
        tuple: A tuple containing the similarity score and two None values. If either image cannot be read, returns (0, None, None).
    """
    image1 = cv2.imread(image_path1)
    image2 = cv2.imread(image_path2)

    if image1 is None or image2 is None:
        print(f"Error: Failed to read images: {image_path1}, {image_path2}")
        return 0, None, None

    preprocessed_image1 = preprocess_image_change_detection(image1)
    preprocessed_image2 = preprocess_image_change_detection(image2)

    common_shape = (
        min(preprocessed_image1.shape[0], preprocessed_image2.shape[0]),
        min(preprocessed_image1.shape[1], preprocessed_image2.shape[1]),
    )
    preprocessed_image1 = cv2.resize(preprocessed_image1, common_shape)
    preprocessed_image2 = cv2.resize(preprocessed_image2, common_shape)

    return compare_frames_change_detection(
        preprocessed_image1, preprocessed_image2, min_contour_area=1000
    )


def process_images(source_folder, destination_folder, threshold=1000):
    """
    Processes all images in the source folder and moves similar images to the destination folder.

    Args:
        source_folder (str): The directory of the source folder containing the images.
        destination_folder (str): The directory of the destination folder where similar images will be moved to.
        threshold (int, optional): The similarity score threshold for considering images as similar. Defaults to 1000.

    Prints:
        The number of images moved to the destination folder.
    """
    image_files = [f for f in os.listdir(source_folder) if f.endswith(".png")]
    image_files.sort(key=lambda x: extract_camera_id_and_timestamp(x))
    num_moved = 0

    for i in range(len(image_files) - 1):
        img1_path = os.path.join(source_folder, image_files[i])
        img2_path = os.path.join(source_folder, image_files[i + 1])

        score, _, _ = compare_images(img1_path, img2_path)

        if score < threshold:
            shutil.move(img2_path, os.path.join(destination_folder, image_files[i + 1]))
            num_moved += 1

    print("Moved {} similar-looking images.".format(num_moved))
