import os
import shutil
from datetime import datetime
from PIL import Image, ImageOps

def copy_folder_with_timestamp(input_folder):
    """Copy the input folder to a new folder with a timestamped name."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    new_folder = f"Resized_{timestamp}"
    shutil.copytree(input_folder, new_folder)
    return new_folder
def resize_images_to_fixed_size(folder, target_size=(340, 340)):
    """Resize images to a fixed size (16:16 aspect ratio) with a background color."""
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue

        try:
            with Image.open(file_path) as img:
                # Resize the image to the target size (340x340)
                resized_img = img.resize(target_size, Image.Resampling.LANCZOS)

                # Save the resized image
                resized_img.save(file_path)
                print(f"Resized and saved: {file_path}")

        except Exception as e:
            print(f"Error processing {filename}: {e}")

def resize_images_with_background_no_ar(folder, target_size=(340, 340)):
    """Resize images to fit within a fixed size (16:16 aspect ratio) by adding a background color."""
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue

        try:
            with Image.open(file_path) as img:
                # Calculate the new size while maintaining the aspect ratio
                img.thumbnail(target_size, Image.Resampling.LANCZOS)

                # Create a new image with the target size and background color
                background = Image.new("RGB", target_size, img.getpixel((0, 0)))
                offset = ((target_size[0] - img.width) // 2, (target_size[1] - img.height) // 2)
                background.paste(img, offset)

                # Save the resized image
                background.save(file_path)
                print(f"Resized and saved: {file_path}")

        except Exception as e:
            print(f"Error processing {filename}: {e}")
def resize_images_with_background(folder, target_width=340):
    """Resize images to the target width and extend with background color if needed."""
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue

        try:
            with Image.open(file_path) as img:
                # Calculate new dimensions while maintaining aspect ratio
                aspect_ratio = img.height / img.width
                new_width = target_width
                new_height = int(new_width * aspect_ratio)

                # Resize the image
                resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

                # Extend the image with background color if needed
                if new_height < new_width:
                    background = Image.new("RGB", (new_width, new_width), img.getpixel((0, 0)))
                    background.paste(resized_img, (0, (new_width - new_height) // 2))
                    resized_img = background

                # Save the resized image
                resized_img.save(file_path)
                print(f"Resized and saved: {file_path}")

        except Exception as e:
            print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    input_folder = "OutputCells_Exp1_Correct"  # Replace with your input folder path
    new_folder = copy_folder_with_timestamp(input_folder)
    resize_images_with_background_no_ar(new_folder)