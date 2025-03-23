# PageRip

PageRip is a simple Python script that adds context menu options to Windows for extracting PDF pages as JPG or PNG images.

## Prerequisites

* Python 3.x installed.
* ImageMagick installed and added to your system's PATH.

## Installation

1.  Download the `pagerip.py`, `add_context_menu.reg`, and `remove_context_menu.reg` files.
2.  **Important:** Edit the `add_context_menu.reg` file and replace `[PATH_TO_PAGERIP.PY]` with the actual path to your `pagerip.py` file.
3.  Double-click `add_context_menu.reg` and confirm the registry changes.
4.  Right-click on a PDF file to see the new context menu options.

## Usage

* Right-click on a PDF file.
* Select "Extract here as JPG" or "Extract here as PNG".
* A folder with the same name as the PDF will be created in the same directory, containing the extracted images.

## Uninstallation

* Double-click `remove_context_menu.reg` and confirm the registry changes.

## Notes

* Ensure ImageMagick is correctly installed and in your system's PATH.
* The script uses `pythonw.exe` to run without a console window.
* If you are using pyinstaller to create an executable, make sure to change the paths in the .reg files to the location of the .exe file.

## License

[Add your license here, e.g., MIT License]
