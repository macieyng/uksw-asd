from typing import Any, Callable, Iterable
import pytest

from main import bubble_sort, insert_sort, merge_sort, quick_sort, simple_sort

@pytest.mark.parametrize(
    "unsorted, expected", [
        ([64,2,31,23,653,1,234,123,76], [1, 2, 23, 31, 64, 76,123, 234,653]),
        ([64,2], [2, 64]),
        ([2], [2])
    ]
)
@pytest.mark.parametrize(
    "sort_function", [
        simple_sort,
        bubble_sort, 
        quick_sort,
        merge_sort,
        insert_sort
    ]
)
def test_sorting(unsorted: Iterable[Any], expected: Iterable[Any], sort_function: Callable[[Any], Any]):
    assert sort_function(unsorted) == expected
