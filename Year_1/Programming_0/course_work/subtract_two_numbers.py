def subtract_two_numbers(m: int, n: int) -> int:
    """Subtracts the second number n from the first m.
    Example:
        subtract_two_numbers(10, 4) should return a numerical value 6."""
    # return the difference
    return m - n


def test_subtract_two_numbers() -> None:
    """Tests the subtract_two_numbers function."""
    # test 1 - positive numbers
    assert subtract_two_numbers(10, 4) == 6
    # test 2 - negative result
    assert subtract_two_numbers(4, 10) == -6
    # test 3 - zero result
    assert subtract_two_numbers(5, 5) == 0
    # test 4 - negative numbers
    assert subtract_two_numbers(-10, -4) == -6
    print("All tests passed.")


if __name__ == "__main__":
    # example usage
    print(subtract_two_numbers(10, 4))  # Expected output - 6
    # run the tests
    test_subtract_two_numbers()
