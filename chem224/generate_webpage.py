r"""
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


Usage
-----
generate-webpage <input_file>
    
    where <input_file> is the path to the original notebook in the lessons/ directory.


Example
-------
```
generate-webpage .\lessons\template\template_lecture.ipynb
```
"""
import argparse
import json
import re
from pathlib import Path
from typing import Any, Protocol
import warnings

import nbformat

from chem224.utils import Equation, EQUATIONS_JSON

warnings.filterwarnings("ignore", category=nbformat.validator.MissingIDFieldWarning)


class InputFileNotFoundError(Exception):
    pass


# make custom WARNING for when an equation is not found
class EquationNotFoundWarning(Warning):
    pass


class CellConversion(Protocol):
    """CellConversion is a protocol for functions that perform some conversion on a
    single cell in a Jupyter notebook."""

    def __call__(
        self, cell: nbformat.NotebookNode, **kwargs: Any
    ) -> nbformat.NotebookNode:
        ...


def image_path_conversion(cell: nbformat.NotebookNode) -> nbformat.NotebookNode:
    """Adjusts the path to images in markdown cells"""
    if cell["cell_type"] != "markdown":
        return cell
    cell_text: str = cell["source"]
    pattern = r'<img src="../../docs/images/'
    replacement = r'<img src="../../images/'
    # Replace the pattern while ignoring relative directories
    cell_text = re.sub(pattern, replacement, cell_text)
    cell["source"] = cell_text
    return cell


def equation_cell_conversion(cell: nbformat.NotebookNode) -> nbformat.NotebookNode:
    """Finds cells with markdown-formatted code cell output and converts them to
    markdown cells"""
    pattern = r"insert_equation\((.+)\)"
    match = re.search(pattern, cell["source"])
    if cell["cell_type"] != "code" or match is None:
        return cell
    new_cell = nbformat.NotebookNode()
    new_cell["cell_type"] = "markdown"
    new_cell["metadata"] = {}
    new_cell["source"] = cell["outputs"][0]["data"]["text/markdown"]
    return new_cell


def linked_equation_conversion(cell: nbformat.NotebookNode) -> nbformat.NotebookNode:
    """Searches markdown cells for the pattern '[EQ: <equation name>]' and replaces it
    with the name of the equation as a link to the equation in the Equations webpage."""
    pattern = r"@EQ: (.+?)@"
    matches = list(re.finditer(pattern, cell["source"]))
    if cell["cell_type"] != "markdown" or len(matches) == 0:
        return cell
    # check that the equation exists in the equations.json file
    with open(EQUATIONS_JSON, "r", encoding="utf-8") as f:
        equations: list[Equation] = json.load(f)
    for match_ in matches:
        for eqn in equations:
            if eqn["name"].lower() == match_.group(1).lower():
                cell_text: str = cell["source"]
                equation_link = match_.group(1).lower().replace(" ", "-")
                replacement = rf"[{match_.group(1)}](../../equations/#{equation_link})"
                cell_text = re.sub(match_.group(0), replacement, cell_text, count=1)
                cell["source"] = cell_text
                break
        else:
            if match_.group(1) != "equation name":  # for template notebook
                warnings.warn(
                    f'Equation "{match_.group(1)}" not found in equations.json',
                    EquationNotFoundWarning,
                )
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


def main() -> None:
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
    make_edited_notebook(
        input_file,
        web_nb,
        conversions=[
            image_path_conversion,
            equation_cell_conversion,
            linked_equation_conversion,
        ],
    )


if __name__ == "__main__":
    main()
