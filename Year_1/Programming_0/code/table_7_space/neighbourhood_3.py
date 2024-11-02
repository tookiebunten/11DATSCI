def moore_neighborhood_3d() -> list:
    """Returns 3D Moore neighborhood offsets as a list of lists."""
    offsets = []
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            for z in [-1, 0, 1]:
                offsets.append([x, y, z])
    return offsets

def test_moore_neighborhood_3d() -> None:
    expected = [
        [-1, -1, -1], [-1, -1, 0], [-1, -1, 1],
        [-1, 0, -1], [-1, 0, 0], [-1, 0, 1],
        [-1, 1, -1], [-1, 1, 0], [-1, 1, 1],
        [0, -1, -1], [0, -1, 0], [0, -1, 1],
        [0, 0, -1], [0, 0, 0], [0, 0, 1],
        [0, 1, -1], [0, 1, 0], [0, 1, 1],
        [1, -1, -1], [1, -1, 0], [1, -1, 1],
        [1, 0, -1], [1, 0, 0], [1, 0, 1],
        [1, 1, -1], [1, 1, 0], [1, 1, 1]
    ]
    assert moore_neighborhood_3d() == expected
    print("All tests passed.")

if __name__ == "__main__":
    print("3D Moore neighborhood offsets:", moore_neighborhood_3d())
    test_moore_neighborhood_3d()