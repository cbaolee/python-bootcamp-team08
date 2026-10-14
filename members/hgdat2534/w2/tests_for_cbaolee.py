import importlib
import sys
from pathlib import Path

MEMBER = "cbaolee"

for parent in Path(__file__).resolve().parents:
    if (parent / "members").is_dir():
        if str(parent) not in sys.path:
            sys.path.insert(0, str(parent))
        break


def load_translate():
    """Import cbaolee's w1.translate module (with local fallback)."""
    try:
        return importlib.import_module(f"members.{MEMBER}.w1.translate")
    except ModuleNotFoundError:
        return importlib.import_module("translate")


def test_binary_search_single_element():
    """Edge case: 1-element list when key is present vs. absent (lo == hi == 0)."""
    tr = load_translate()
    assert tr.binary_search([42], 42) == 0
    assert tr.binary_search([42], 7) == -1


def test_binary_search_first_and_last_boundaries():
    """Edge case: Target sits at the very first index (0) or very last index (n - 1)."""
    tr = load_translate()
    arr = [2, 5, 8, 12, 16, 23, 38]
    assert tr.binary_search(arr, 2) == 0
    assert tr.binary_search(arr, 38) == 6


def test_binary_search_out_of_bounds_keys():
    """Edge case: Target is strictly smaller than min(a) or strictly larger than max(a)."""
    tr = load_translate()
    arr = [10, 20, 30, 40, 50]
    assert tr.binary_search(arr, 5) == -1
    assert tr.binary_search(arr, 60) == -1


def test_binary_search_negative_numbers_and_zero():
    """Tests sorted lists containing negative integers and zero."""
    tr = load_translate()
    arr = [-25, -10, -3, 0, 7, 14]
    assert tr.binary_search(arr, -10) == 1
    assert tr.binary_search(arr, 0) == 3
    assert tr.binary_search(arr, -5) == -1


def test_binary_search_odd_and_even_lengths():
    """Tests middle-element resolution on both odd-length and even-length lists."""
    tr = load_translate()
    assert tr.binary_search([1, 4, 9, 16, 25], 9) == 2
    assert tr.binary_search([1, 4, 9, 16, 25, 36], 16) == 3
