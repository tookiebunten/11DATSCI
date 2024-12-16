def sum_odd_numbers_in_table(n) -> int:
    """Sums the odd numbers in the multiplication table up to n x n.
    Example
    sum_odd_numbers_in_table(3) should return 16.

    Example
    sum_odd_numbers_in_table(5) should return 81."""
    # find all odd numbers from 1 to n
    odd_numbers = [x for x in range(1, n + 1) if x % 2 != 0]
    # compute the sum of all products of these odd numbers
    odd_sum = sum(i * j for i in odd_numbers for j in odd_numbers)
    return odd_sum


def test_sum_odd_numbers_in_table() -> None:
    """tests the sum_odd_numbers_in_table function."""
    # test 1 - 3 x 3 table
    assert sum_odd_numbers_in_table(3) == 16
    # test 2 - 5 x 5 table
    assert sum_odd_numbers_in_table(5) == 81
    # test 3 - 1 x 1 table
    assert sum_odd_numbers_in_table(1) == 1
    # test 4 - 2 x 2 table
    assert sum_odd_numbers_in_table(2) == 1
    print("All tests passed.")


if __name__ == "__main__":
    # example usage
    print(sum_odd_numbers_in_table(3))  # Expected output: 16
    print(sum_odd_numbers_in_table(5))  # Expected output: 81
    # run the tests
    test_sum_odd_numbers_in_table()
