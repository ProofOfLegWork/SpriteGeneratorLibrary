import cv2
import numpy as np
import os
from datetime import datetime

def split_image_by_empty_space(image_path, output_folder, min_area=1000):
    # Load the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Threshold to binary: white = background, black = content
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

    # Optional: clean up small noise
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    cleaned = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

    # Find contours (connected components)
    contours, _ = cv2.findContours(cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Sort contours from top-left to bottom-right
    contours = sorted(contours, key=lambda c: (cv2.boundingRect(c)[1], cv2.boundingRect(c)[0]))

    os.makedirs(output_folder, exist_ok=True)

    for i, cnt in enumerate(contours):
        x, y, w, h = cv2.boundingRect(cnt)
        if w * h > min_area:  # Filter out noise
            sub_img = image[y:y+h, x:x+w]
            cv2.imwrite(f"{output_folder}/cell_{i+1:03d}.png", sub_img)

    print(f"✅ Done! Saved {len(contours)} cropped images to {output_folder}")

# Example usage
# Create a folder with the current time up to seconds
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_folder = f"output_cells_{current_time}"

split_image_by_empty_space("Images/NormalPeople_1.png", output_folder)
