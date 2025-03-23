import os
import subprocess
import sys
import winreg

def install():
    """Installs the context menu entries."""
    script_path = os.path.abspath(__file__)  # Get the absolute path of the script
    key_path_jpg = r"SystemFileAssociations\.pdf\shell\PageRipJPG\command"
    key_path_png = r"SystemFileAssociations\.pdf\shell\PageRipPNG\command"

    try:
        with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, key_path_jpg, 0, winreg.KEY_WRITE) as key:
            winreg.SetValueEx(key, "", 0, winreg.REG_SZ, f'pythonw.exe "{script_path}" "%1" jpg')
        with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, key_path_png, 0, winreg.KEY_WRITE) as key:
            winreg.SetValueEx(key, "", 0, winreg.REG_SZ, f'pythonw.exe "{script_path}" "%1" png')
        print("Installation successful.")

    except Exception as e:
        print(f"Installation failed: {e}")

def extract_pdf_pages(pdf_path, output_format):
    """Extracts PDF pages as JPG or PNG images."""
    folder_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_folder = os.path.join(os.path.dirname(pdf_path), folder_name)
    os.makedirs(output_folder, exist_ok=True)

    try:
        subprocess.run(["magick", "convert", pdf_path, f"{output_folder}/Page%d.{output_format}"], check=True)
        print(f"Extraction to {output_format.upper()} complete. Images saved in '{output_folder}'.")

    except FileNotFoundError:
        print("Error: ImageMagick not found. Please ensure ImageMagick is installed and in your PATH.")
    except subprocess.CalledProcessError as e:
        print(f"Error during extraction: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        install()
    elif len(sys.argv) == 3:
        pdf_path = sys.argv[1]
        output_format = sys.argv[2].lower()
        extract_pdf_pages(pdf_path, output_format)
    else:
        print("Usage:")
        print("  - Run without arguments to install.")
        print("  - Run with <pdf_path> <output_format (jpg or png)> to extract.")
