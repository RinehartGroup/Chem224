"""
This script reads the equations.json file in the docs/resources/ directory,
alphabetizes the equations by name, and updates the equations.md file in the
docs/ directory with the new list of equations.

Usage
-----
generate-equations-webpage
"""
import os
import json
from pathlib import Path
from typing import TypedDict

MAIN_DIR = Path(os.path.dirname(os.path.abspath(__file__))).parent

EQUATIONS_JSON = MAIN_DIR / "docs" / "resources" / "equations.json"

EQUATIONS_MD = MAIN_DIR / "docs" / "equations.md"


class Equation(TypedDict):
    name: str
    latex: str
    symbols: dict[str, str]
    wikipedia: str
    description: str


def read_equations(source: Path) -> list[Equation]:
    with open(source, "r", encoding="utf-8") as f:
        equations = json.load(f)
    return equations


def write_md_file(equations: list[Equation]) -> None:
    with open(EQUATIONS_MD, "w", encoding="utf-8") as f:
        f.write("## Equations\n\n")
        for eqn in equations:
            formatted_symbols = [
                "- $`" + key + "`$: " + value for key, value in eqn["symbols"].items()
            ]
            formatted_symbols = "\n".join(formatted_symbols)
            output: str = f"# {eqn['name'].title()}\n\n"
            output += f"```math\n{eqn['latex']}\n```\n\n"
            output += f"{formatted_symbols}\n\n"
            output += f"{eqn['description']} ([Wikipedia]({eqn['wikipedia']}))\n\n"
            f.write(output)


def main() -> None:
    equations: list[Equation] = read_equations(EQUATIONS_JSON)
    equations = sorted(equations, key=lambda x: x["name"])
    write_md_file(equations)


if __name__ == "__main__":
    main()
