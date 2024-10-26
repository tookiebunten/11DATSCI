def calculate_expression(a, b, c, d, e, f, g) -> float:
    """Receives 7 parameters a to g, which are arranged according to the 
    following equation: 
    
    ((a + b * c) * d / e - f) + g
    
    …the resulting value is returned """
    
    result = ((a + b * c) * d / (e - f)) + g
    return result

def test_calculate_expression() -> None:
    assert calculate_expression(1, 2, 3, 4, 5, 6, 7) == -21
    assert calculate_expression(0, 1, 2, 3, 4, 5, 6) == 0
    assert calculate_expression(1, 1, 1, 1, 1, 2, 1) == -1
    assert calculate_expression(2, 3, 4, 5, 6, 7, 8) == -62
    print("All tests passed.")

if __name__ == "__main__":
    print("Result of the expression with parameters 1, 2, 3, 4, 5, 6, 7:", calculate_expression(1, 2, 3, 4, 5, 6, 7))
    test_calculate_expression()