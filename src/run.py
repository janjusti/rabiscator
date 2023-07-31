import datetime
import logging
import sys
import fitz
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


def get_first_pdf_and_png_files(folder_path):
    pdf_file = None
    png_file = None

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf") and not pdf_file:
            pdf_file = os.path.join(folder_path, filename)
        elif filename.lower().endswith(".png") and not png_file:
            png_file = os.path.join(folder_path, filename)
        if pdf_file and png_file:
            break

    return pdf_file, png_file


def add_png_to_pdf(pdf_file_path, png_file_path, output_filename):
    coords = [int(x) for x in os.getenv("IMG_POS").split(",")]
    image_rectangle = fitz.Rect(coords)

    file_handle = fitz.open(pdf_file_path)
    first_page = file_handle[0]

    first_page.insert_image(image_rectangle, filename=png_file_path)

    file_handle.save(output_filename, garbage=3, deflate=True)


if __name__ == "__main__":
    local_folder_path = Path("/local-folder")
    input_folder_path = local_folder_path / "input"
    pdf_file, png_file = get_first_pdf_and_png_files(input_folder_path)

    if pdf_file is None or png_file is None:
        logging.error(
            "Set your files: there should be at least one .PDF file and one .PNG file."
        )
        sys.exit(1)

    basename = os.getenv("BASENAME")
    prevmonth = (
        datetime.date.today().replace(day=1) - datetime.timedelta(days=1)
    ).strftime("%m-%Y")
    somenumber = os.getenv("SOMENUMBER")
    somename = os.getenv("SOMENAME")

    output_folder = local_folder_path / "output"
    if not output_folder.exists():
        output_folder.mkdir(parents=True, exist_ok=True)

    output_filename = (
        output_folder / f"{basename}_{prevmonth}_{somenumber}_{somename}.pdf"
    )

    add_png_to_pdf(pdf_file, png_file, output_filename)
    logging.info(f"File '{output_filename}' created.")
