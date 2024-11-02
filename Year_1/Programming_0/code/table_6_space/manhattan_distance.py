def manhattan_distance(list1, list2) -> int:
    """Return the Manhattan distance given two lists of arbitrary dimensions. 
    If the lists are different lengths, return Python's None value."""
    
    if len(list1) != len(list2):
        return None
    
    distance = sum(abs(a - b) for a, b in zip(list1, list2))
    return distance

def test_manhattan_distance() -> None:
    assert manhattan_distance([1, 2, 3], [4, 5, 6]) == 9
    assert manhattan_distance([0, 0], [3, 4]) == 7
    assert manhattan_distance([1, 2], [1, 2]) == 0
    assert manhattan_distance([1, 2, 3], [4, 5]) is None
    print("All tests passed.")

if __name__ == "__main__":
    print("Manhattan distance between [1, 2, 3] and [4, 5, 6]:", manhattan_distance([1, 2, 3], [4, 5, 6]))
    test_manhattan_distance()