def calculate_distance(p, q, distance_type) -> float:
    """Return either the Euclidean or Manhattan 2D distance between two points p 
    and q, depending on if a third arg is “euclid” or “manhattan”, otherwise return 
    None."""
    
    if distance_type == "euclid":
        return ((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2) ** 0.5
    elif distance_type == "manhattan":
        return abs(p[0] - q[0]) + abs(p[1] - q[1])
    else:
        return None

def test_calculate_distance() -> None:
    assert calculate_distance((0, 0), (3, 4), "euclid") == 5.0
    assert calculate_distance((0, 0), (3, 4), "manhattan") == 7
    assert calculate_distance((1, 2), (4, 6), "euclid") == 5.0
    assert calculate_distance((1, 2), (4, 6), "manhattan") == 7
    assert calculate_distance((0, 0), (3, 4), "invalid") is None
    print("All tests passed.")

if __name__ == "__main__":
    print("Euclidean distance between (0, 0) and (3, 4):", calculate_distance((0, 0), (3, 4), "euclid"))
    print("Manhattan distance between (0, 0) and (3, 4):", calculate_distance((0, 0), (3, 4), "manhattan"))
    test_calculate_distance()