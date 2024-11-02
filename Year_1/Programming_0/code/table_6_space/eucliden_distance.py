def euclidean_distance(list1, list2) -> float:
    """Return the Euclidean distance given two lists of arbitrary dimensions. 
    If the lists are different lengths, return Python's None value."""
    
    if len(list1) != len(list2):
        return None
    
    distance = sum((a - b) ** 2 for a, b in zip(list1, list2)) ** 0.5
    return distance

def test_euclidean_distance() -> None:
    assert euclidean_distance([1, 2, 3], [4, 5, 6]) == 5.196152422706632
    assert euclidean_distance([0, 0], [3, 4]) == 5.0
    assert euclidean_distance([1, 2], [1, 2]) == 0.0
    assert euclidean_distance([1, 2, 3], [4, 5]) is None
    print("All tests passed.")

if __name__ == "__main__":
    print("Euclidean distance between [1, 2, 3] and [4, 5, 6]:", euclidean_distance([1, 2, 3], [4, 5, 6]))
    test_euclidean_distance()