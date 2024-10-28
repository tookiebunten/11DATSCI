def absolute_sum(num1, num2):
    """Receives two numbers and returns their sum as an absolute value"""
    return abs(num1 + num2)

def test_absolute_sum():
    assert absolute_sum(5, 3) == 8
    assert absolute_sum(-5, 3) == 2
    assert absolute_sum(-5, -3) == 8
    assert absolute_sum(0, 0) == 0
    print("All tests passed.")

if __name__ == "__main__":
    print("Result of absolute sum of 5 and 3:", absolute_sum(5, 3))
    test_absolute_sum()
