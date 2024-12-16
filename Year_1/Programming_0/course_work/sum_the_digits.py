def sum_the_digits(number: int) -> int:
    """Calculates the sum of the digits of a number.
    Example:
       sum_the_digits(1234) should return 10."""
    # convert the number to a string and sum the digits
    return sum(int(digit) for digit in str(number))


def test_sum_the_digits() -> None:
    """Tests the sum_the_digits function."""
    # test 1 - sum of digits of 1234
    assert sum_the_digits(1234) == 10  # 1 + 2 + 3 + 4 = 10
    # test 2 - sum of digits of 0
    assert sum_the_digits(0) == 0  # 0 = 0
    # test 3 - sum of digits of 1111
    assert sum_the_digits(1111) == 4  # 1 + 1 + 1 + 1 = 4
    # test 4 - sum of digits of 9876
    assert sum_the_digits(9876) == 30  # 9 + 8 + 7 + 6 = 30
    print("All tests passed.")


if __name__ == "__main__":
    # example usage
    print(sum_the_digits(1234))  # expected output - 10
    # run the tests
    test_sum_the_digits()
