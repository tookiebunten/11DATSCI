def adds(p1: list[int], p2: list[int]) -> list[int] | None:
    """Adds and returns generic list vectors p1 and p2.
        Example:
        adds ([5, 7, 3], [2, -1, 4]) should return: [7, 6, 7].
        If p1 and p2 are different sizes, return None."""
    # check if the lengths of the two lists are the same
    if len(p1) != len(p2):
        return None
    # empty list to store the results
    result = []
    # iterate over the lists
    for i in range(len(p1)):
        # add the elements and append to the results list
        result.append(p1[i] + p2[i]) 
    # return the resulting list
    return result


def test_adds() -> None:
    """Tests the adds function."""
    # test 1 - normal case
    assert adds([5, 7, 3], [2, -1, 4]) == [7, 6, 7]
    # test 2 - different sizes
    assert adds([1, 2], [3, 4, 5]) is None
    # test 3 - empty list
    assert adds([], []) == []
    # test 4 - single element list
    assert adds([1], [1]) == [2]
    print("All tests passed.")


if __name__ == "__main__":
    # example usage
    print(adds([5, 7, 3], [2, -1, 4]))
    # run the tests
    test_adds()
