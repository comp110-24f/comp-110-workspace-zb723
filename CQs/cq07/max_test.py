"""Unit tests for find_and_remove_max"""

___author___ = "730700099"

from CQs.cq07.find_max import find_and_remove_max


def test_return_find_and_remove_max_() -> None:
    """Use case to check expected value"""
    a: list[int] = [5, 4, 3]
    assert find_and_remove_max(a) == 5  # expected return


def test_mutate_find_and_remove_max() -> None:
    """Use case to check if mutate correctly"""
    # c: list[int] = [9, 3, 33, 99, 39]
    c: list[int] = [1, 8, 2, 3, 8, 3]
    find_and_remove_max(c)
    assert c == [1, 2, 3, 3]  # expected return


def test_edge_find_and_remove_max() -> None:
    """Edge case to check if return correct if bad input"""
    assert find_and_remove_max([]) == -1  # expected value checked = correct
