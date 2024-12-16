def is_even(number: int) -> bool:
    """Checks if a number is even.
    Example 1: is_even(10) should return the boolean value True.
     Example 2: is_even(9) should return the boolean value False."""
    # checks if a number is even.
    return number % 2 == 0


def test_is_even() -> None:
    """Tests the is_even function."""
    # test 1 - even number
    assert is_even(10) is True
    # test 2 - odd number
    assert is_even(9) is False
    # test 3 - zero (even number)
    assert is_even(0) is True
    # test 4 - negative even number
    assert is_even(-4) is True
    # test 5 - negative odd number
    assert is_even(-3) is False
    print("All tests passed.")


if __name__ == "__main__":
    # example usage
    print(is_even(10))  # expected output - true
    print(is_even(9))  # expected output - false
    # run the tests
    test_is_even()
