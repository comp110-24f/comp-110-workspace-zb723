"""Implementing tests for list utility functions"""

__author__ = "730700099"

from exercises.ex05.utils import only_evens, sub, add_at_index

import pytest

# for only evens fucntion
#   how should return, how should mutate, edge case for bad input/empty list


def test_return_only_evens() -> None:
    """Use case to check if returns correctly"""
    a: list[int] = [3, 66, 75, 93, 4]
    assert only_evens(a) == [66, 4]


def test_mutate_only_evens() -> None:
    """Use case to test if mutates correct (no mutate)"""
    a: list[int] = [3, 5, 6, 9]
    only_evens(a)
    assert a == [3, 5, 6, 9]


def test_empty_list_only_evens() -> None:
    """Unit tets to test if return correct if bad/empty input (edge)"""
    assert only_evens([]) == []


# for sub fucntion


def test_return_sub() -> None:
    """Use case to check if returns correctly"""
    b: list[int] = [1, 3, 5, 7, 9, 11, 13, 15]
    sub(b, 2, 5)
    assert sub(b, 2, 5) == [5, 7, 9]


def test_mutate_sub() -> None:
    """Use case to test if mutates correct (no mutation)"""
    b: list[int] = [1, 3, 5, 7, 9, 11, 13, 15]
    sub(b, 3, 7)
    assert b == [1, 3, 5, 7, 9, 11, 13, 15]


def test_empty_list_sub() -> None:
    """Unit test to test if return correct if bad/empty input (edge)"""
    assert sub([], 1, 5) == []


# for add_at_index fucntion


def test_return_add_at_index() -> None:
    """Use case to test if returns correctly"""
    c: list[int] = [5, 6, 8]
    assert add_at_index(c, 7, 2) is None


def test_mutate_add_at_index() -> None:
    """Use case make sure mutate correctly (there is mutation)"""
    c: list[int] = [9, 33, 99]
    add_at_index(c, 3, 0)
    assert c == [3, 9, 33, 99]


def test_edge_add_at_index() -> None:
    """Test that add_at_index raises an IndexError for an invalid index"""
    with pytest.raises(IndexError):
        add_at_index([], 3, 4)
