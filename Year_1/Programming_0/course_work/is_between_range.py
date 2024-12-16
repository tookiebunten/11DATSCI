def is_between_range(number: int, range:list[int]) -> bool:
    """Checks if a number is inclusively within a range.
    Example:
        is_between_range(5, [1, 10]) should return True.
        is_between_range(50, [1, 50]) should return True."""
    # checks if a number is inclusively within a range.
    lower, upper = range
    # return the result of the comparison
    return lower <= number <= upper


def test_is_between_range() -> None:
    """Tests the is_between_range function."""
    # test 1 - number is within the range
    assert is_between_range(5, [1, 10]) is True
    # test 2 - number is equal to the lower
    assert is_between_range(1, [1, 10]) is True
    # test 3 - number is below the range
    assert is_between_range(0, [1, 10]) is False
    # test 4 - number is above the range
    assert is_between_range(11, [1, 10]) is False
    print("All tests passed.")


if __name__ == "__main__":
    # example usage
    print(is_between_range(5, [1, 10]))  # expected output - True
    print(is_between_range(50, [1, 50]))  # expected output - True
    # run the test cases
    test_is_between_range()
