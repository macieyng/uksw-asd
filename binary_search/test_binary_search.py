from typing import Tuple
import pytest
from . import binary_search

@pytest.mark.parametrize(
    "collection, key, item_idx", [
        ((1, 2, 3), 2, 1),
        ((1, 3), 2, -1),
        ((1, 3, 7, 10, 15, 23, 111), 10, 3),
        ((1, 3, 7, 10, 15, 23, 111), 111, 6),
        ((1, 3, 7, 10, 15, 23, 111), 1, 0),
        ((-11, 3, 7, 10, 15, 23, 111), -11, 0),
        ((1, 3, 7, 10, 15, 23, 111), 2222, -1),
    ]
)
def test_binary_search(collection: Tuple[int], key: int, item_idx: int):
    """-1 means not found"""
    assert binary_search(*collection, key=key) == item_idx
