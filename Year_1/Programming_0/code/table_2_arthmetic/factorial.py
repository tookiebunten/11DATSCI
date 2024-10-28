def factorial(n) -> int:
    """Receives a positive integer n and returns its factorial. A factorial is 
    the product (multiplication) of each positive integer less than or 
    equal to n."""
    
    if n < 0:
        raise ValueError("n must be a positive integer.")
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def test_factorial() -> None:
    assert factorial(5) == 120  # 5! = 5 * 4 * 3 * 2 * 1 = 120
    assert factorial(0) == 1  # 0! is defined as 1
    assert factorial(1) == 1  # 1! = 1
    assert factorial(3) == 6  # 3! = 3 * 2 * 1 = 6
    print("All tests passed.")

if __name__ == "__main__":
    print("Result of factorial for 5:", factorial(5))
    test_factorial()