def sort_to_types(arbitrary_ordered_types: list) -> list:
    """Takes a list with elements of different types (strings, integers, and floats) and 
    returns a new list where strings come first, followed by integers, and finally floats.
    Example Input:
    ['banana', 5, 3.14, 'apple', 42, 2.71] Returns: ['banana', 'apple', 5, 42, 3.14, 2.71]."""
    # separate the types
    strings = [x for x in arbitrary_ordered_types if isinstance(x, str)]
    integers = [x for x in arbitrary_ordered_types if isinstance(x, int)]
    floats = [x for x in arbitrary_ordered_types if isinstance(x, float)]
    # return the sorted list
    return strings + integers + floats


def test_sort_to_types() -> None:
    """Tests the sort_to_types function."""
    # test 1 - mixed types
    assert sort_to_types(["banana", 5, 3.14, "apple", 42, 2.71]) == [
        "banana",
        "apple",
        5,
        42,
        3.14,
        2.71,
    ]
    # test 2 - only strings
    assert sort_to_types(["banana", "apple"]) == ["banana", "apple"]
    # test 3 - only integers
    assert sort_to_types([5, 42]) == [5, 42]
    # test 4 - only floats
    assert sort_to_types([3.14, 2.71]) == [3.14, 2.71]
    print("All tests passed.")


if __name__ == "__main__":
    # example usage
    print(
        sort_to_types(["banana", 5, 3.14, "apple", 42, 2.71])
    )  # expected output: ['banana', 'apple', 5, 42, 3.14, 2.71]
    # run the tests
    test_sort_to_types()
