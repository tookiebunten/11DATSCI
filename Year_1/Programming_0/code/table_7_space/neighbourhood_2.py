def moore_neighborhood_2d() -> list:
    """Returns 2D Moore neighborhood offsets as a list of lists."""
    return [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1], [0, 0], [0, 1],
        [1, -1], [1, 0], [1, 1]
    ]

def test_moore_neighborhood_2d() -> None:
    expected = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1], [0, 0], [0, 1],
        [1, -1], [1, 0], [1, 1]
    ]
    assert moore_neighborhood_2d() == expected
    print("All tests passed.")

if __name__ == "__main__":
    print("2D Moore neighborhood offsets:", moore_neighborhood_2d())
    test_moore_neighborhood_2d()