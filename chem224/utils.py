import json
import os
from pathlib import Path

from IPython.display import Markdown

MAIN_DIR = Path(os.path.dirname(os.path.abspath(__file__))).parent

EQUATIONS = MAIN_DIR / "docs" / "resources" / "equations.json"


class EquationNotFoundError(Exception):
    pass


def insert_equation(
    equation: str, heading_level: int = 2, source: Path = EQUATIONS
) -> Markdown:
    """Used in a code cell in a Jupyter notebook to insert an equation from a reference
    json file and display it as Markdown with additional pieces of information about
    the equation.

    Parameters
    ----------
    equation : str
        The name of the equation as listed in the json file.
    heading_level : int, optional
        The heading level to give the name of the equation in the Markdown output,
        by default 2 (##).
    source : Path, optional
        The pat of the json file. Defaults to the global variable EQUATIONS, which
        is the path to the equations.json file in the docs/resources directory.

    Returns
    -------
    Markdown
        The Markdown output of the equation.

    Raises
    ------
    EquationNotFoundError
        Raised when the name of the equation is not found in the json file.
    """
    with open(source, "r", encoding="utf-8") as f:
        equations = json.load(f)
    eqn: dict = None
    for e in equations:
        if e["name"].lower() == equation.lower():
            eqn = e
            break
    if eqn is None:
        raise EquationNotFoundError(f'Equation "{equation}" not found in {source.name}')

    symbols = eqn["symbols"]
    formatted_symbols = ["- $" + key + "$: " + value for key, value in symbols.items()]
    formatted_symbols = "\n".join(formatted_symbols)

    output: str = f"{heading_level * '#'} {eqn['name'].title()}\n\n"
    output += f"$${eqn['latex']}$$\n\n"
    output += f"{formatted_symbols}\n\n"
    output += f"{eqn['description']} ([Wikipedia]({eqn['wikipedia']}))\n"

    return Markdown(output)
