import json
import os
from pathlib import Path

from IPython.display import Markdown

MAIN_DIR = Path(os.path.dirname(os.path.abspath(__file__))).parent

EQUATIONS = MAIN_DIR / "docs" / "resources" / "equations.json"


def insert_equation(
    equation: str, heading_level: int = 2, source: Path = EQUATIONS
) -> Markdown:
    with open(source, "r", encoding="utf-8") as f:
        equations = json.load(f)
    eqn: dict = None
    for e in equations:
        if e["name"].lower() == equation.lower():
            eqn = e
            break
    if eqn is None:
        raise ValueError(f'Equation "{equation}" not found in {source.name}')

    symbols = eqn["symbols"]
    formatted_symbols = ["- " + key + ": " + value for key, value in symbols.items()]
    formatted_symbols = "\n".join(formatted_symbols)

    output: str = f"{heading_level * '#'} {eqn['name'].title()}\n\n"
    output += f"$${eqn['latex']}$$\n\n"
    output += f"{formatted_symbols}\n\n"
    output += f"{eqn['description']} ([Wikipedia]({eqn['wikipedia']}))\n"

    return Markdown(output)
