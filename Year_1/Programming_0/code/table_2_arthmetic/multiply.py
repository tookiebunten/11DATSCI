def multiply_five_numbers(a, b, c, d, e) -> float:
    """Receives five arguments and returns the results of multiplying those numbers."""
    return a * b * c * d * e

def test_multiply_five_numbers() -> None:
    assert multiply_five_numbers(1, 2, 3, 4, 5) == 120
    assert multiply_five_numbers(1, 1, 1, 1, 1) == 1
    assert multiply_five_numbers(2, 3, 4, 5, 6) == 720
    assert multiply_five_numbers(1.5, 2.5, 3.5, 4.5, 5.5) == 324.84375
    print("All tests passed.")

if __name__ == "__main__":
    print("Result of multiplying 1, 2, 3, 4, 5:", multiply_five_numbers(1, 2, 3, 4, 5))
    test_multiply_five_numbers()