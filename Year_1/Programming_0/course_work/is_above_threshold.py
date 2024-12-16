def is_above_threshold(number: int, threshold: int) -> int:
    """Takes a number and a threshold, and returns 1 if the number is greater than
    the threshold, otherwise returns 0.
        Example: is_above_threshold(15, 10) should return 1."""
    # check if the number is greater than the threshold
    return 1 if number > threshold else 0


def test_is_above_threshold() -> None:
    """Tests the is_above_threshold function."""
    # test 1 - number is greater than threshold
    assert is_above_threshold(15, 10) == 1
    # test 2 - number is equal to threshold
    assert is_above_threshold(10, 10) == 0
    # test 3 - number is less than threshold
    assert is_above_threshold(5, 10) == 0
    # test 4 - negative number greater than negative threshold
    assert is_above_threshold(-5, -10) == 1
    print("All tests passed.")


if __name__ == "__main__":
    # example usage
    print(is_above_threshold(15, 10))  # expected output - 1
    # run the tests
    test_is_above_threshold()
