# Multimedia Image Editor

A desktop application built with Python, Tkinter, and `ttkbootstrap` for basic image viewing, editing, and drawing. It provides a user-friendly interface to apply various transformations and filters to images.

## Features

*   **Image Loading & Saving:**
    *   Open common image formats.
    *   Save edited images.
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
    *   Buttons with icons for common actions.
    *   Status bar to provide feedback on operations.
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
