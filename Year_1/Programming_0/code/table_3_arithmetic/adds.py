def sum_odd_indices(lst) -> int:
    """Receives a list and returns the sum of the values stored at odd indices."""
    return sum(lst[number] for number in range(1, len(lst), 2))

def test_sum_odd_indices() -> None:
    assert sum_odd_indices([1, 2, 3, 4, 5]) == 6  # 2 + 4 = 6
    assert sum_odd_indices([0, 1, 0, 1, 0, 1]) == 3  # 1 + 1 + 1 = 3
    assert sum_odd_indices([10, 20, 30, 40, 50, 60]) == 120  # 20 + 40 + 60 = 120
    assert sum_odd_indices([1]) == 0  # No odd indices
    assert sum_odd_indices([]) == 0  # Empty list
    print("All tests passed.")

if __name__ == "__main__":
    print("Result of sum_odd_indices for [1, 2, 3, 4, 5]:", sum_odd_indices([1, 2, 3, 4, 5]))
    test_sum_odd_indices()