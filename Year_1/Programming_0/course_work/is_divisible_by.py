def is_divisible_by(number: int, denominators: list[int]) -> bool:
    """Checks if a number is perfectly divisible by each element in a list of denominators.
    Example:
        is_divisible_by(12, [3, 4])  returns True Otherwise returns False."""
    # checks if a number is perfectly divisible by each element in a list of denominators.
    for denominator in denominators:
        if number % denominator != 0:
            # return False if the number is not divisible by any of the denominators
            return False
    # return True if the number is divisible by all denominators
    return True


def test_is_divisible_by() -> None:
    """Tests the is_divisible_by function."""
    # test 1 - number is divisible by all denominators
    assert is_divisible_by(12, [3, 4]) is True
    # test 2 - number is not divisible by one of the denominators
    assert is_divisible_by(12, [3, 5]) is False
    # test 3 - number is divisible by a single denominator
    assert is_divisible_by(10, [2]) is True
    # test 4 - number is not divisible by a single denominator
    assert is_divisible_by(10, [3]) is False
    print("All tests passed.")


if __name__ == "__main__":
    # example usage
    print(is_divisible_by(12, [3, 4]))  # expected output - True
    # run the tests
    test_is_divisible_by()
