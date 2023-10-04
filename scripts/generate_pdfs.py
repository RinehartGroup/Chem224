"""
This script converts a Jupyter Notebook to a PDF file usig pandoc.

Several changes need to be made to the raw notebook file before conversion:
   1. Detect HTML images and convert them to LaTeX images
   2. Detect markdown-formatted links and convert them to LaTeX links
   3. Detect markdown-formatted code cell output and convert it to an equivalent
        markdown cell

Current issues:
    1. Pandoc does not support LaTeX image formatting. nbconvet does, but it adds
        extra unwanted formatting to the PDF. We'll need to write a custom template
        for nbconvert to fix this.
"""
import re
import argparse
import subprocess
import warnings
from pathlib import Path
import nbformat
from typing import Callable

warnings.filterwarnings("ignore", category=nbformat.validator.MissingIDFieldWarning)


class PandocNotInstalledError(Exception):
    pass


class PandocConversionError(Exception):
    pass


class InputFileNotFoundError(Exception):
    pass


def confirm_pandoc_installed() -> bool:
    try:
        subprocess.run(
            ["pandoc", "--version"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
        )
    except FileNotFoundError as exc:
        raise PandocNotInstalledError(
            "Pandoc is not installed. Please install Pandoc before using this script."
        ) from exc


CellConversion = Callable[[nbformat.NotebookNode], nbformat.NotebookNode]


def image_conversion(cell: nbformat.NotebookNode) -> nbformat.NotebookNode:
    if cell["cell_type"] != "markdown":
        return cell
    cell_text: SystemError = cell["source"]
    pattern = (
        r'<div align="center">\s*<img src="([^"]+)" alt="[^"]+" '
        r'style="height:(\d+)cm;">\s*</div>'
    )
    # check if the cell contains an HTML image
    matches = re.finditer(pattern, cell_text)

    # ignore any text found in code blocks
    to_replace: list[re.Match] = []
    for match_ in matches:
        if (
            cell_text[
                max(0, match_.span()[0] - 9) : min(match_.span()[1] + 5, len(cell_text))
            ]
        ).count("```") == 0:
            to_replace.append(match_)

    # replace the HTML image with a LaTeX image
    offset = 0
    for match_ in to_replace:
        path = match_.group(1)
        height = match_.group(2)
        replacement = rf"$\includegraphics[height={height}cm]{{{path}}}$"
        cell_text = (
            cell_text[: match_.span()[0] + offset]
            + replacement
            + cell_text[match_.span()[1] + offset :]
        )
        offset += len(replacement) - len(match_.group(0))

    cell["source"] = cell_text

    return cell


def make_edited_notebook(
    input_file: Path, output_file: Path, conversions: list[CellConversion]
) -> None:
    original_notebook = nbformat.read(input_file, as_version=nbformat.NO_CONVERT)
    edited_notebook = nbformat.v4.new_notebook()

    for cell in original_notebook.cells:
        for conversion in conversions:
            cell = conversion(cell)
        edited_notebook.cells.append(cell)
    edited_notebook.metadata = original_notebook.metadata
    _, edited_notebook = nbformat.validator.normalize(edited_notebook)
    nbformat.write(edited_notebook, output_file, version=nbformat.NO_CONVERT)


def convert_ipynb_to_pdf(input_file: Path, output_file: Path):
    # Build the Pandoc command
    pandoc_command = [
        "pandoc",
        "--to",
        "pdf",
        "--from",
        "ipynb",
        "-o",
        str(output_file),
        "-V",
        "geometry:margin=1in",
        str(input_file),
    ]

    # Run Pandoc to convert the notebook to PDF
    try:
        subprocess.run(pandoc_command, check=True)
        print(f"Conversion complete. PDF saved as: {output_file}")
        # The following warning will be raised and is currently ignored:
        # MissingIDFieldWarning: Code cell is missing an id field, this will become a
        # hard error in future nbformat versions. You may want to use `normalize()` on
        # your notebooks before validations (available since nbformat 5.1.4). Previous
        # versions of nbformat are fixing this issue transparently, and will stop doing
        # so in the future.
        # validate(nb)
        # Conversion complete. PDF saved as: ...
    except subprocess.CalledProcessError as exc:
        raise PandocConversionError(
            "Error occurred during conversion. Please check the input file and try again."
        ) from exc


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert Jupyter Notebook to PDF using Pandoc."
    )
    parser.add_argument("input_file", type=Path, help="Input .ipynb file to convert.")
    parser.add_argument(
        "-o",
        "--output_file",
        type=Path,
        help="Output .pdf file (default: input_file.pdf).",
    )
    args = parser.parse_args()

    confirm_pandoc_installed()

    input_file: Path = args.input_file
    output_file: Path | None = args.output_file

    if output_file is None:
        output_file = input_file.with_suffix(".pdf")

    if not input_file.exists():
        raise InputFileNotFoundError(f"Input file {input_file} does not exist.")

    tmp_nb: Path = Path(input_file.parent / "tmp.ipynb")
    make_edited_notebook(input_file, tmp_nb, conversions=[image_conversion])

    try:
        convert_ipynb_to_pdf(tmp_nb, output_file)
    finally:
        if tmp_nb.exists():
            tmp_nb.unlink()
