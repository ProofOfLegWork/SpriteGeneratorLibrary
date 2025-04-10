# FileSplitter

## Overview
FileSplitter is a Python-based tool designed to extract multiple sprites from a single sprite sheet. By utilizing a grid-based separation approach, this tool simplifies the process of breaking down sprite sheets into individual sprite images for use in game development or other creative projects.

## Features
- Automatically splits sprite sheets into individual sprites.
- Supports grid-based separation for consistent sprite dimensions.
- Easy-to-use and customizable for various sprite sheet configurations.

## How It Works
1. **Input Sprite Sheet**: Provide the sprite sheet image file.
2. **Grid Configuration**: Define the number of rows and columns or the dimensions of each sprite.
3. **Sprite Extraction**: The tool processes the sprite sheet and extracts individual sprites based on the grid configuration.
4. **Output**: Extracted sprites are saved as separate image files in the specified output directory.

## Usage
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/FileSplitter.git
    cd FileSplitter
    ```
2. Install dependencies (if any):
    ```bash
    pip install -r requirements.txt
    ```
3. Run the script:
    ```bash
    python splitter.py --input sprite_sheet.png --rows 4 --columns 5 --output ./sprites
    ```
    Replace `sprite_sheet.png` with your sprite sheet file, and adjust the `--rows` and `--columns` arguments as needed.

## Example
For a sprite sheet with 4 rows and 5 columns:
- Input: `sprite_sheet.png`
- Command:
  ```bash
  python splitter.py --input sprite_sheet.png --rows 4 --columns 5 --output ./sprites
  ```
- Output: 20 individual sprite images saved in the `./sprites` directory.

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve the tool.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
Special thanks to the open-source community for inspiration and resources.
