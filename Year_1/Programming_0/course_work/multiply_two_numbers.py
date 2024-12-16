def multiply_two_numbers(m: int, n: int) -> int:
    """Multiplies two numbers and returns the product.
    Example:
       multiply_two_numbers(4, 6) should return a numerical value 24."""
    # return the product of the two numbers
    return m * n


def test_multiply_two_numbers():
    """Tests the multiply_two_numbers function."""
    # test 1 - positive numbers
    assert multiply_two_numbers(4, 6) == 24
    # test 2 - positive and negative number
    assert multiply_two_numbers(-4, 6) == -24
    # test 3 - two negative numbers
    assert multiply_two_numbers(-4, -6) == 24
    # test 4 - zero and a positive number
    assert multiply_two_numbers(0, 6) == 0
    print("All tests passed.")


if __name__ == "__main__":
    # example usage
    print(multiply_two_numbers(4, 6))  # expected output -  24
    # run the tests
    test_multiply_two_numbers()
