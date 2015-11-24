import pytest
import random

from python.src import bubble_sort


ITEM_COUNT = 20


@pytest.fixture
def random_data():
    data = list(range(ITEM_COUNT))
    random.shuffle(data)
    return data


def test_bubble_sort(random_data):
    expected = list(range(ITEM_COUNT))
    assert not expected == random_data
    result = bubble_sort(random_data)
    assert expected == result
