from pathlib import Path

import pytest

from mwis.core.animal import get_animals_tree
from mwis.core.mwis import mwis


def test_mwis():
    king, animals = get_animals_tree(Path("tests/example.json"))

    assert king.name == "Mufasa"

    score, invited_list = mwis(king, force_keep_root=True)
    # Assuming that the JSON file is sorted by the party score

    assert set([animal.name for animal in invited_list]) == set(
        ["Mufasa", "Timon", "Shenzi", "Ed"]
    )

    assert pytest.approx(score, 0.1) == 86.31

    score, invited_list = mwis(king, force_keep_root=False)
    # Assuming that the JSON file is sorted by the party score

    assert set([animal.name for animal in invited_list]) == set(
        ["Simba", "Timon", "Shenzi", "Ed"]
    )

    assert pytest.approx(score, 0.1) == 96.41
