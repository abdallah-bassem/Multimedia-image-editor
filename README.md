# Multimedia Image Editor

A desktop application built with Python, Tkinter, and `ttkbootstrap` for basic image viewing, editing, and drawing. It provides a user-friendly interface to apply various transformations and filters to images.

## Features

*   **Image Loading & Saving:**
    *   Open common image formats (JPG, JPEG, PNG, GIF, BMP).
    *   Save edited images in PNG, JPG, or BMP formats.
*   **Image Display:**
    *   Displays images on a canvas, fitting them while maintaining aspect ratio.
    *   Placeholder text when no image is loaded.
*   **Transformations:**
    *   **Flip:** Horizontally flip the image.
    *   **Rotate:** Rotate the image in 90-degree increments.
*   **Image Filters:**
    *   Original
    *   Black and White
    *   Sepia
    *   Negative
    *   Solarize
    *   Posterize
    *   Blur
    *   Contour
    *   Detail
    *   Emboss
    *   Edge Enhance
    *   Sharpen
    *   Smooth
*   **Drawing Tools:**
    *   Draw on the image with a pen.
    *   Select pen color using a color chooser.
    *   Clear all drawings from the current image.
*   **User Interface:**
    *   Modern look and feel using the `ttkbootstrap` "vapor" theme.
    *   Organized layout with a tools panel and a main image canvas.
    *   Interactive filter selection via a combobox.
    *   Buttons are enabled/disabled based on whether an image is loaded.

## Technologies Used

*   **Python 3.x**
*   **Tkinter:** Standard Python interface to the Tcl/Tk GUI toolkit.
*   **ttkbootstrap:** A collection of modern, flat themes for Tkinter/TTK.
*   **Pillow (PIL Fork):** Python Imaging Library for opening, manipulating, and saving many different image file formats.


## Prerequisites

*   Python 3.x installed on your system.
*   `pip` (Python package installer).

## Setup and Installation

1.  **Clone the repository (or download the `app.py` file):**
    ```bash
    git clone https://github.com/abdallah-bassem/Multimedia-image-editor.git
    cd Multimedia-image-editor
    ```

2.  **Install required Python libraries:**
    ```bash
    pip install ttkbootstrap Pillow
    ```

3.  **Icon Files (Optional but Recommended):**
    The application attempts to load several icon files for its buttons. If these files are not present in the same directory as `app.py`, warnings will be printed to the console, and buttons will appear without icons.
    The expected icon files are:
    *   `app_icon.png` (for the application window)
    *   `open_icon.png`
    *   `save_icon.png`
    *   `flip_icon.png`
    *   `rotate_icon.png`
    *   `color_icon.png`
    *   `erase_icon.png`

    Make sure to place these `.png` files in the same directory as `app.py` for the best visual experience.

## How to Run

Navigate to the directory containing `app.py` and run the script using Python:

```bash
python app.py
```

## Usage Guide

1.  **Open an Image:**
    *   Click the "Open Image" button in the "File Operations" section.
    *   Select an image file from your computer. The image will be displayed on the canvas.
2.  **Apply Transformations:**
    *   **Flip:** Click the "Flip" button in the "Transformations" section to flip the image horizontally.
    *   **Rotate:** Click the "Rotate" button to rotate the image 90 degrees clockwise.
3.  **Apply Filters:**
    *   Select a filter from the dropdown menu in the "Image Filters" section. The filter will be applied to the image instantly.
4.  **Drawing on the Image:**
    *   **Select Pen Color:** Click the "Pen Color" button in the "Drawing Tools" section to choose a color for drawing.
    *   **Draw:** Click and drag your mouse on the image canvas to draw.
    *   **Clear Drawings:** Click the "Clear Drawings" button to remove all drawings made on the current image.
5.  **Save the Edited Image:**
    *   Click the "Save Image" button.
    *   Choose a location, file name, and format (PNG, JPG, BMP) to save your edited image. The drawings will be included in the saved image.
6.  **Status Bar:**
    *   Keep an eye on the status bar at the bottom of the window for messages about ongoing operations, errors, or successful actions.

## File Structure

```
Multimedia-image-editor/
├── app.py              # The main application script
├── app_icon.png        # (Optional) Application icon
├── open_icon.png       # (Optional) Icon for open button
├── save_icon.png       # (Optional) Icon for save button
├── flip_icon.png       # (Optional) Icon for flip button
├── rotate_icon.png     # (Optional) Icon for rotate button
├── color_icon.png      # (Optional) Icon for color picker button
└── erase_icon.png      # (Optional) Icon for erase button
```

