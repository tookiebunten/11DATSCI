def is_overlap(circle1, circle2) -> bool:
    """Two 'circles' are received in respective lists containing coordinates x, y and 
    radius r. Return True or False, depending on whether or not the circles touch or 
    overlap."""
    
    x1, y1, r1 = circle1
    x2, y2, r2 = circle2
    
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return distance <= (r1 + r2)

def test_is_overlap() -> None:
    assert is_overlap([0, 0, 1], [2, 0, 1])
    assert not is_overlap([0, 0, 1], [3, 0, 1])
    assert is_overlap([0, 0, 2], [1, 1, 2])
    assert is_overlap([0, 0, 1], [0, 0, 1])
    print("All tests passed.")

if __name__ == "__main__":
    print("Result of is_overlap for [0, 0, 1] and [2, 0, 1]:", is_overlap([0, 0, 1], [2, 0, 1]))
    test_is_overlap()