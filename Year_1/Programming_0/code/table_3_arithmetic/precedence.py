def calculate_expression(a, b, c, d, e, f, g) -> float:
    """Receives 7 parameters a to g, which are arranged according to the 
    following equation: 
    
    ((((a + b) * c * d) / (e - f + g)) / f) - g
    
    Return the result of the calculation."""
    
    result = ((((a + b) * c * d) / (e - f + g)) / f) - g
    return result

def test_calculate_expression() -> None:
    assert calculate_expression(1, 2, 3, 4, 5, 6, 7) == -6
    assert calculate_expression(1, 1, 1, 1, 1, 1, 1) == 1
    assert calculate_expression(10, 20, 30, 40, 50, 60, 70) == -60
    print("All tests passed.")

if __name__ == "__main__":
    print("Result of calculate_expression for (1, 2, 3, 4, 5, 6, 7):", calculate_expression(1, 2, 3, 4, 5, 6, 7))
    test_calculate_expression()