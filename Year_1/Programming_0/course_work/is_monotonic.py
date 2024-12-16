def is_monotonic(string_of_digits: str) -> bool:
    """Checks if a string of digits follow a monotonic pattern (consistently increasing / decreasing). Returns True if so, otherwise False.
    Examples:
    Monotonically Increasing: '22456'
    Monotonically Decreasing: '66521'
    Non-Monotonic: '98612'."""
    # check if the string is increasing
    increasing = all(
        string_of_digits[i] <= string_of_digits[i + 1]
        for i in range(len(string_of_digits) - 1)
    )
    # check if the string is decreasing
    decreasing = all(
        string_of_digits[i] >= string_of_digits[i + 1]
        for i in range(len(string_of_digits) - 1)
    )
    # return True if either increasing or decreasing
    return increasing or decreasing


def test_is_monotonic() -> None:
    """Tests the is_monotonic function."""
    # test 1 - monotonically increasing
    assert is_monotonic("22456") is True
    # test 2 - monotonically decreasing
    assert is_monotonic("66521") is True
    # test 3 - non-monotonic
    assert is_monotonic("98612") is False
    # test 4 - single digit (considered monotonic)
    assert is_monotonic("5") is True
    print("All tests passed.")


if __name__ == "__main__":
    # example usage
    print(is_monotonic("22456"))  # expected output - True
    print(is_monotonic("66521"))  # expected output - True
    print(is_monotonic("98612"))  # expected output - False
    # run the tests
    test_is_monotonic()
