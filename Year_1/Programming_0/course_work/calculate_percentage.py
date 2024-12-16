def calculate_percentage(part: float, total: float) -> float:
    """Returns a percentage given a part and a total.
    Example:
        calculate_percentage(30, 150) should return a numerical value 20.0."""
    # calculates the percentage of 'part' with respect to 'total'.
    if total == 0:
        return 0
    return (part / total) * 100


def test_calculate_percentage() -> None:
    """Tests the calculate_percentage function."""
    # test 1 - normal case
    assert calculate_percentage(50, 200) == 25.0
    # test 2 - part is 0
    assert calculate_percentage(0, 100) == 0.0
    # test 3 - total is 0
    assert calculate_percentage(50, 0) == 0
    # test 4 - part equals total
    assert calculate_percentage(100, 100) == 100.0
    print("All tests passed.")


if __name__ == "__main__":
    # example usage
    print(calculate_percentage(30, 150))  # expected output - 20.0
    # run the test cases
    test_calculate_percentage()
