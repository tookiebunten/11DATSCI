def powered_multiple(arg1, arg2, arg3) -> float:
    """Raise a supplied number arg1 to the power of arg2, then 
    returns the result, multiplied by arg3."""
    result = (arg1 ** arg2) * arg3
    return result

def test_powered_multiple() -> None:
    assert powered_multiple(2, 3, 4) == 32  # (2^3) * 4 = 8 * 4 = 32
    assert powered_multiple(3, 2, 5) == 45  # (3^2) * 5 = 9 * 5 = 45
    assert powered_multiple(1, 5, 10) == 10  # (1^5) * 10 = 1 * 10 = 10
    assert powered_multiple(4, 0.5, 2) == 4  # (4^0.5) * 2 = 2 * 2 = 4
    print("All tests passed.")

if __name__ == "__main__":
    print("Result of powered_multiple for 2, 3, 4:", powered_multiple(2, 3, 4))
    test_powered_multiple()