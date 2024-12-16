def greatest(a: int, b: int, c: int) -> int:
    """Finds the greatest of three numbers.
        Example: greatest_of_three(5, 12, 8) should return 12."""
    # Finds the greatest of three numbers. Returns max number
    return max(a, b, c)


def test_greatest() -> None:
    """Tests the greatest function."""
    # test 1 - normal case
    assert greatest(5, 12, 8) == 12
    # test 2 - all numbers are the same
    assert greatest(7, 7, 7) == 7
    # test 3 - first number is the greatest
    assert greatest(15, 10, 5) == 15
    # test 4 - last number is the greatest
    assert greatest(1, 2, 3) == 3
    print("All tests passed.")


if __name__ == "__main__":
    # example usage
    print(greatest(5, 12, 8))  # expected output - 12
    # run the tests
    test_greatest()
