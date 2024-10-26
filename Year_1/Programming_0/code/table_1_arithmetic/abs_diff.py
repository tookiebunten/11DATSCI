def absolute_difference(num1, num2) -> int:
    """Receives two numbers and returns their difference as an absolute value."""
    return abs(num1 - num2)

def test_absolute_difference() -> None:
    assert absolute_difference(5, 3) == 2
    assert absolute_difference(3, 5) == 2
    assert absolute_difference(-5, -3) == 2
    assert absolute_difference(-3, -5) == 2
    assert absolute_difference(0, 0) == 0
    print("All tests passed.")

if __name__ == "__main__":
    print("Result of absolute difference between 5 and 3:", absolute_difference(5, 3))
    test_absolute_difference()