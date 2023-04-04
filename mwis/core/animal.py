from __future__ import annotations

import json
from collections import OrderedDict
from pathlib import Path

from anytree import NodeMixin


class Animal(NodeMixin):
    '''
    Animal class

    Attributes:
        name: Name of the animal
        party_score: Party score of the animal
        parent: Parent animal
        children: Children animals
    '''

    def __init__(
        self,
        name: str,
        party_score: float,
        parent: Animal = None,
        children: list[Animal] = None,
    ):
        self.name = name
        self.party_score = party_score

    def __repr__(self) -> str:
        return f"Animal(name={self.name}, party_score={self.party_score})"


def get_animals_tree(json_data: Path | list) -> tuple[Animal, dict[str, Animal]]:
    if isinstance(json_data, Path):
        with open(json_data) as f:
            json_data = json.load(f)

    # Initialize animals
    animals = {
        animal["name"]: Animal(animal["name"], animal["party-animal-score"])
        for animal in json_data
    }
    animals = OrderedDict(animals)

    # Add parent and children
    for animal_info in json_data:
        animal = animals[animal_info["name"]]
        if animal_info["ruler"] is not None:
            animal.parent = animals[animal_info["ruler"]]

    # Find the king/root
    king = [animal for animal in animals.values() if animal.is_root][0]

    return king, animals
