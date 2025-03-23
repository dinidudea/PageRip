import os
import subprocess
import sys

def extract_pdf_pages(pdf_path, output_format):
    """Extracts PDF pages as JPG or PNG images."""

    folder_name = os.path.splitext(os.path.basename(pdf_path))[0] # Get filename without extension
    output_folder = os.path.join(os.path.dirname(pdf_path), folder_name) # Create output folder in same directory
    os.makedirs(output_folder, exist_ok=True)

    try:
        if output_format == "jpg":
            subprocess.run(["magick", "convert", pdf_path, f"{output_folder}/Page%d.jpg"], check=True)
        elif output_format == "png":
            subprocess.run(["magick", "convert", pdf_path, f"{output_folder}/Page%d.png"], check=True)
        else:
            print("Error: Invalid output format. Use 'jpg' or 'png'.")
            return

        print(f"Extraction to {output_format.upper()} complete. Images saved in '{output_folder}'.")

    except FileNotFoundError:
        print("Error: ImageMagick not found. Please ensure ImageMagick is installed and in your PATH.")
    except subprocess.CalledProcessError as e:
        print(f"Error during extraction: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python pagerip.py <pdf_path> <output_format (jpg or png)>")
    else:
        pdf_path = sys.argv[1]
        output_format = sys.argv[2].lower()
        extract_pdf_pages(pdf_path, output_format)
