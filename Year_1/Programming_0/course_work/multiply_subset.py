def multiply_subset(numbers: list[int], indices: list[int]) -> int:
    """Multiplies numbers from a list at specified indices.
    Example: multiply_subset([2, 3, 4, 5, 6, 7, 8], [0, 2, 4]) should return 48."""
    # initialise the result
    result = 1
    # multiply the numbers at the specified indices
    for index in indices:
        result *= numbers[index]
    # return the result
    return result


def test_multiply_subset() -> None:
    """Tests the multiply_subset function."""
    # test 1 - normal case
    assert multiply_subset([2, 3, 4, 5, 6, 7, 8], [0, 2, 4]) == 48
    # test 2 - single index
    assert multiply_subset([2, 3, 4, 5, 6, 7, 8], [1]) == 3
    # test 3 - all indices
    assert multiply_subset([2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6]) == 40320
    # test 4 - no indices
    assert multiply_subset([2, 3, 4, 5, 6, 7, 8], []) == 1
    print("All tests passed.")


if __name__ == "__main__":
    # example usage
    print(multiply_subset([2, 3, 4, 5, 6, 7, 8], [0, 2, 4]))  # expected output - 48
    # run the tests
    test_multiply_subset()
