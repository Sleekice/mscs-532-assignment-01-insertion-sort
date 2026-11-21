
from src.insertion_sort import insertion_sort


def test_unsorted_array():
    arr = [12, 11, 13, 5, 6]
    insertion_sort(arr)
    assert arr == [13, 12, 11, 6, 5]


def test_already_decreasing():
    arr = [9, 7, 5, 3, 1]
    insertion_sort(arr)
    assert arr == [9, 7, 5, 3, 1]


def test_increasing_array():
    arr = [1, 2, 3, 4, 5]
    insertion_sort(arr)
    assert arr == [5, 4, 3, 2, 1]


def test_duplicates():
    arr = [4, 2, 4, 1, 2]
    insertion_sort(arr)
    assert arr == [4, 4, 2, 2, 1]


def test_empty_array():
    arr = []
    insertion_sort(arr)
    assert arr == []
