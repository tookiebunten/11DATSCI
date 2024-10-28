def modulo(num1, num2) -> int:
    """The function takes two numbers as inputs and returns the remainder 
    when the first number is divided by the second."""
    return num1 % num2

def test_modulo() -> None:
    assert modulo(10, 3) == 1
    assert modulo(20, 5) == 0
    assert modulo(7, 4) == 3
    assert modulo(9, 2) == 1
    print("All tests passed.")

if __name__ == "__main__":
    print("Result of 10 % 3:", modulo(10, 3))
    test_modulo()