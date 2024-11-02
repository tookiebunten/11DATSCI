def square_root(number) -> float:
    """Return the square root of a supplied number."""
    if number < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    return number ** 0.5

def test_square_root() -> None:
    assert square_root(4) == 2
    assert square_root(9) == 3
    assert square_root(0) == 0
    assert square_root(1) == 1
    assert square_root(16) == 4
    print("All tests passed.")

if __name__ == "__main__":
    print("Result of square_root for 4:", square_root(4))
    test_square_root()