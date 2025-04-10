import os
import cv2
from collections import Counter

def process_images(folder_path, output_prefix="image"):
    # Get all image files in the folder
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    if not image_files:
        print("No image files found in the folder.")
        return

    # Store dimensions of all images
    dimensions = []
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        image = cv2.imread(image_path)
        if image is None:
            print(f"Skipping invalid image file: {image_file}")
            continue
        dimensions.append((image.shape[1], image.shape[0]))  # (width, height)
    print(dimensions)
    # Find the most common dimension
    most_common_dim = Counter(dimensions).most_common(1)[0][0]
    print(f"Most common dimension: {most_common_dim}")

    # Process images: remove cropped ones and rename valid ones
    valid_count = 0
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        image = cv2.imread(image_path)
        if image is None:
            continue
        if (image.shape[1], image.shape[0]) == most_common_dim:
            # Rename valid image
            valid_count += 1
            new_name = f"{output_prefix}_{valid_count:03d}.png"
            new_path = os.path.join(folder_path, new_name)
            os.rename(image_path, new_path)
        else:
            # Remove cropped image
            #os.remove(image_path)
            print(f"Removed cropped image: {image_file}")

    print(f"✅ Process completed. {valid_count} images renamed with prefix '{output_prefix}'.")

# Example usage
folder_path = "OutputCells_Exp1"  # Replace with the path to your folder
process_images(folder_path, output_prefix="character")