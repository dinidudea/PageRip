# PageRip

PageRip is a Python script that adds context menu options to Windows for extracting PDF pages as JPG or PNG images.

## Prerequisites

* Python 3.x installed.
* ImageMagick installed and added to your system's PATH.

## Installation

1.  Download the `pagerip.py` and `remove_context_menu.reg` files.
2.  Open a command prompt or PowerShell as administrator.
3.  Navigate to the directory where you saved `pagerip.py`.
4.  Run the following command: `python pagerip.py`
5.  This will automatically install the context menu entries.
6.  Right-click on a PDF file to see the new context menu options.

## Usage

* **Extraction:** Right-click on a PDF file and select "Extract here as JPG" or "Extract here as PNG". A folder with the same name as the PDF will be created in the same directory, containing the extracted images.
* **Command-line extraction:** you can also extract files directly from the command line. `python pagerip.py "path/to/my/file.pdf" jpg` or `python pagerip.py "path/to/my/file.pdf" png`

## Uninstallation

1.  Double-click `remove_context_menu.reg` and confirm the registry changes.

## Notes

* Ensure ImageMagick is correctly installed and in your system's PATH.
* The script uses `pythonw.exe` to run without a console window when run from the context menu.
* Administrative privileges are required for the installation process.
* If you are using pyinstaller to create an executable, the usage will remain the same.

## License

All rights waived.
