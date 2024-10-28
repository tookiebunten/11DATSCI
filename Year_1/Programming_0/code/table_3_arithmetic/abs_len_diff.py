def abs_len_diff_powered(list1, list2, power) -> int:
    """Receives two lists and returns the difference between their length as an 
    absolute value, raised to the power of a number, which is the third 
    argument to the function."""
    
    len_diff = abs(len(list1) - len(list2))
    result = len_diff ** power
    return result

def test_abs_len_diff_powered() -> None:
    assert abs_len_diff_powered([1, 2, 3], [4, 5], 2) == 1  # abs(3 - 2) ** 2 = 1 ** 2 = 1
    assert abs_len_diff_powered([1, 2], [3, 4, 5, 6], 3) == 8  # abs(2 - 4) ** 3 = 2 ** 3 = 8
    assert abs_len_diff_powered([], [1, 2, 3], 2) == 9  # abs(0 - 3) ** 2 = 3 ** 2 = 9
    assert abs_len_diff_powered([1, 2, 3], [4, 5, 6], 1) == 0  # abs(3 - 3) ** 1 = 0 ** 1 = 0
    print("All tests passed.")

if __name__ == "__main__":
    print("Result of abs_len_diff_powered for [1, 2, 3], [4, 5], 2:", abs_len_diff_powered([1, 2, 3], [4, 5], 2))
    test_abs_len_diff_powered()