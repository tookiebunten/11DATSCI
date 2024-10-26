def square(number) -> float:
    """Return the square of a supplied number."""
    return number ** 2

def test_square() -> None:
    assert square(2) == 4
    assert square(-3) == 9
    assert square(0) == 0
    assert square(1.5) == 2.25
    print("All tests passed.")

if __name__ == "__main__":
    print("Result of squaring 3:", square(3))
    test_square()