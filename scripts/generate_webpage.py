"""
This script modifies a Jupyter notebook as written in the lessons/ directory to be
formatted for the website.

It assumes that it will be run from the root directory of the repository, that the
original notebook will be in the lessons/ directory, and that the modified notebook
will be saved in the docs/lessons/ directory with the same file name.

Several changes need to be made to the raw notebook file before conversion:
    1. Change paths to images. Note that given the above assumptions about the
        directory structure, relative paths to the images/ directory will be correct
        for both the original lesson notebook and the converted notebook. Only images
        in the original notebook directoy will need to be changed. 

        If images are placed in any other dirctory other than the images/ directory or
        the directory of the original notebook, the path will need to be changed
        manually.

    2. Detect markdown-formatted code cell output and convert it to an equivalent
        markdown cell
"""
import argparse
import re
from pathlib import Path
from typing import Any, Protocol
import warnings

import nbformat

warnings.filterwarnings("ignore", category=nbformat.validator.MissingIDFieldWarning)


class InputFileNotFoundError(Exception):
    pass


class CellConversion(Protocol):
    def __call__(
        self, cell: nbformat.NotebookNode, **kwargs: Any
    ) -> nbformat.NotebookNode:
        ...


def image_path_conversion(
    cell: nbformat.NotebookNode, **kwargs
) -> nbformat.NotebookNode:
    if cell["cell_type"] != "markdown":
        return cell
    cell_text: str = cell["source"]
    pattern = r'<img src="../../docs/images/'
    replacement = r'<img src="../../images/'
    # Replace the pattern while ignoring relative directories
    cell_text = re.sub(pattern, replacement, cell_text)
    cell["source"] = cell_text
    return cell


def make_edited_notebook(
    input_file: Path, output_file: Path, conversions: list[CellConversion]
) -> None:
    original_notebook_dir = input_file.parent
    original_notebook = nbformat.read(input_file, as_version=nbformat.NO_CONVERT)
    edited_notebook = nbformat.v4.new_notebook()

    for cell in original_notebook.cells:
        for conversion in conversions:
            cell = conversion(cell, parent_dir=original_notebook_dir)
        edited_notebook.cells.append(cell)
    edited_notebook.metadata = original_notebook.metadata
    _, edited_notebook = nbformat.validator.normalize(edited_notebook)
    nbformat.write(edited_notebook, output_file, version=nbformat.NO_CONVERT)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert Jupyter Notebook to PDF using Pandoc."
    )
    parser.add_argument("input_file", type=Path, help="Input .ipynb file to convert.")
    args = parser.parse_args()

    input_file: Path = args.input_file

    if not input_file.exists():
        raise InputFileNotFoundError(f"Input file {input_file} does not exist.")

    web_nb: Path = Path(
        input_file.parent.parent.parent / "docs" / "lessons" / input_file.name
    )
    make_edited_notebook(input_file, web_nb, conversions=[image_path_conversion])
