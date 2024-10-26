def multiply_numbers(*args) -> int:
    """Receives an arbitrary list of numbers (you can use *args, for example) 
    and returns the result of multiplying those numbers."""
    
    result = 1
    for number in args:
        result *= number
    return result

def test_multiply_numbers() -> None:
    assert multiply_numbers(1, 2, 3, 4) == 24
    assert multiply_numbers(2, 3, 5) == 30
    assert multiply_numbers(10, 0.5) == 5
    assert multiply_numbers(1, -1, 1, -1) == 1
    print("All tests passed.")

if __name__ == "__main__":
    print("Result of multiplying 1, 2, 3, 4:", multiply_numbers(1, 2, 3, 4))
    test_multiply_numbers()