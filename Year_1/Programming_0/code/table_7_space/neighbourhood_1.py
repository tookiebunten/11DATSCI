def moore_neighborhood_1d() -> list:
    """Returns 1D Moore neighborhood offsets as a list of lists."""
    return [[-1], [0], [1]]

def test_moore_neighborhood_1d()-> None:
    assert moore_neighborhood_1d() == [[-1], [0], [1]]
    print("All tests passed.")

if __name__ == "__main__":
    print("1D Moore neighborhood offsets:", moore_neighborhood_1d())
    test_moore_neighborhood_1d()