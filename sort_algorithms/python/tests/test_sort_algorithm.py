import pytest
import random

from python.src import bubble_sort, bubble_sort_optimized


ITEM_COUNT = 20


@pytest.fixture
def random_data():
    data = list(range(ITEM_COUNT))
    random.shuffle(data)
    return data


@pytest.mark.parametrize("sort_method", [bubble_sort, bubble_sort_optimized])
def test_bubble_sort(random_data, sort_method):
    expected = list(range(ITEM_COUNT))
    assert not expected == random_data
    result = sort_method(random_data)
    assert expected == result
