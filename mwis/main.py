from pathlib import Path

import typer
from rich import print
from rich.console import Console
from anytree import RenderTree

from core.mwis import mwis
from core.animal import get_animals_tree


def main(json_path: Path, include_king: bool = True):
    console = Console(
        width=400,
        height=200,
    )
    # king, animals = get_animals_tree("birds/example.json")
    king, animals = get_animals_tree(json_path)

    style_header = "green on black bold"

    console.print("TREE:", style=style_header)
    console.print(RenderTree(king), style="Red on Black")

    score, invited_list = mwis(king, force_keep_root=include_king)
    # Assuming that the JSON file is sorted by the party score
    invited_list = sorted(
        invited_list, key=lambda x: list(animals.keys()).index(x.name)
    )

    console.print(f"Score: {score}", style=style_header)
    console.print("Invitated List: ", style=style_header, end="")
    console.print(
        ", ".join([animal.name for animal in invited_list]), style="white on black bold"
    )

    validation_score = sum([invited.party_score for invited in invited_list])

    console.print(f"Validation score: {validation_score}", style=style_header)
    pass


if __name__ == "__main__":
    typer.run(main)
