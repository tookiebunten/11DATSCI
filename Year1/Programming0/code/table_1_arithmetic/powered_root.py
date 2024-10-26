def powered_root(arg1, arg2) -> float:
    """Raise a supplied number arg1 to the power of arg2, then returns the 
    square root of the result."""
    
    result = arg1 ** arg2
    sqrt_result = result ** 0.5
    return sqrt_result

def test_powered_root() -> None:
    assert powered_root(4, 2) == 4  # 4^2 = 16, sqrt(16) = 4
    assert powered_root(9, 2) == 9  # 9^2 = 81, sqrt(81) = 9
    assert powered_root(2, 3) == 2 ** 1.5  # 2^3 = 8, sqrt(8) = 2 ** 1.5
    assert powered_root(16, 0.5) == 2  # 16^0.5 = 4, sqrt(4) = 2
    print("All tests passed.")

if __name__ == "__main__":
    print("Result of raising 4 to the power of 2 and taking the square root:", powered_root(4, 2))
    test_powered_root()