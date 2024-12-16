def sum_perfect_squares(number: int) -> int:
    """Sums the perfect squares of the form n2 for number n = 1 up to and including n.
    Example:
     sum_perfect_squares(4) should return 30."""
    total_sum = sum(i * i for i in range(1, number + 1))
    # return the total sum
    return total_sum


def test_sum_perfect_squares() -> None:
    """Tests the sum_perfect_squares function."""
    # test 1: Sum of perfect squares up to 4
    assert sum_perfect_squares(4) == 30  # 1^2 + 2^2 + 3^2 + 4^2 = 1 + 4 + 9 + 16 = 30
    # test 2: Sum of perfect squares up to 1
    assert sum_perfect_squares(1) == 1  # 1^2 = 1
    # test 3: Sum of perfect squares up to 2
    assert sum_perfect_squares(2) == 5  # 1^2 + 2^2 = 1 + 4 = 5
    # test 4: Sum of perfect squares up to 3
    assert sum_perfect_squares(3) == 14  # 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14
    print("All tests passed.")


if __name__ == "__main__":
    # example usage
    print(sum_perfect_squares(4))  # expected output: 30
    # run the test cases
    test_sum_perfect_squares()
