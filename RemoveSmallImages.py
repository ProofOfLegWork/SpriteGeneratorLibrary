import os
import cv2
import shutil
from datetime import datetime

def copy_folder_with_timestamp(source_folder):
    """
    Creates a copy of the source folder with a timestamp appended to its name.

    Args:
        source_folder (str): Path to the source folder.

    Returns:
        str: Path to the newly created folder.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    destination_folder = f"{source_folder}_{timestamp}"
    shutil.copytree(source_folder, destination_folder)
    print(f"✅ Folder copied to: {destination_folder}")
    return destination_folder

def remove_small_images(folder_path, size_threshold_ratio=0.5):
    """
    Removes images that are significantly smaller than the average size in the folder.

    Args:
        folder_path (str): Path to the folder containing images.
        size_threshold_ratio (float): Ratio of the average size below which images are removed.
    """
    # Get all image files in the folder
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    if not image_files:
        print("No image files found in the folder.")
        return

    # Calculate the area of each image
    areas = []
    image_dimensions = {}
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        image = cv2.imread(image_path)
        if image is None:
            print(f"Skipping invalid image file: {image_file}")
            continue
        height, width = image.shape[:2]
        area = width * height
        areas.append(area)
        image_dimensions[image_file] = area

    if not areas:
        print("No valid images found in the folder.")
        return

    # Calculate the average area
    average_area = sum(areas) / len(areas)
    size_threshold = average_area * size_threshold_ratio
    print(f"Average area: {average_area:.2f}")
    print(f"Size threshold (below which images will be removed): {size_threshold:.2f}")

    # Remove images smaller than the threshold
    removed_count = 0
    for image_file, area in image_dimensions.items():
        if area < size_threshold:
            image_path = os.path.join(folder_path, image_file)
            os.remove(image_path)
            removed_count += 1
            print(f"Removed small image: {image_file} (Area: {area})")

    print(f"✅ Process completed. {removed_count} images removed.")

# Example usage
source_folder = "OutputCells_Exp1"  # Replace with the path to your folder
backup_folder = copy_folder_with_timestamp(source_folder)
remove_small_images(backup_folder, size_threshold_ratio=0.5)