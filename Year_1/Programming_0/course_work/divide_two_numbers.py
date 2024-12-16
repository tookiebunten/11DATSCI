def divide_two_numbers(m: float, n: float) -> float | str:
    """Divides two numbers and returns the quotient. Handles division by zero by returning a string “NAN”.
    Examples:
        divide_two_numbers(10, 2) should return a numerical value 5.0.
        divide_two_numbers(10, 0) returns “NAN”."""
    # check if the divisor is 0
    if n == 0:
        return "NAN"
    # return the quotient
    return m / n


def test_divide_two_numbers() -> None:
    """Tests the divide_two_numbers function."""
    # test 1 - normal division
    assert divide_two_numbers(10, 2) == 5
    # test 2 - division by zero
    assert divide_two_numbers(10, 0) == "NAN"
    # test 3 - division resulting in a float
    assert divide_two_numbers(7, 2) == 3.5
    # test 4 - division by one
    assert divide_two_numbers(10, 1) == 10.0
    print("All tests passed.")


if __name__ == "__main__":
    # example usage
    print(divide_two_numbers(10, 2))  # Expected output - 5.0
    print(divide_two_numbers(10, 0))  # Expected output - NAN
    # run the tests
    test_divide_two_numbers()
