def add_three_numbers(a, b, c):
    """Receives three numbers, adds them together, and returns the result."""
    return a + b + c

def test_add_three_numbers():
    assert add_three_numbers(1, 2, 3) == 6
    assert add_three_numbers(-1, -2, -3) == -6
    assert add_three_numbers(0, 0, 0) == 0
    assert add_three_numbers(1.5, 2.5, 3.5) == 7.5
    print("All tests passed.")

if __name__ == "__main__":
    print("Result of adding 1, 2, 3 = ", add_three_numbers(1, 2, 3))
    test_add_three_numbers()