def is_even_and_positive(number: int) -> bool:
    """Takes an integer as input and returns True if the number is both even and positive, otherwise returns False.
    Example:
        is_even_and_positive(4) returns True
        is_even_and_positive(-2) returns False."""
    # check if the number is both even an positive
    return number >= 0 and number % 2 == 0


def test_is_even_and_positive() -> None:
    """Tests the is_even_and_positive function."""
    # test 1 - even and positive number
    assert is_even_and_positive(4) is True
    # test 2 - odd and positive number
    assert is_even_and_positive(3) is False
    # test 3 - zero
    assert is_even_and_positive(0) is True
    # test 4 - negative even number
    assert is_even_and_positive(-2) is False
    print("All tests passed.")


if __name__ == "__main__":
    # example usage
    print(is_even_and_positive(4))  # expected output - True
    print(is_even_and_positive(-2))  # expected output - False
    # run the tests
    test_is_even_and_positive()
