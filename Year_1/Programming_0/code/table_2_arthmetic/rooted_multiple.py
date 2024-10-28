def rooted_multiple(*args) -> int:
    """Receives a list of args. Returns (as an integer) the square root of 
    the result of multiplying each element in the list."""
    
    if not args:
        raise ValueError("At least one argument is required.")
    
    product = 1
    for number in args:
        product *= number
    
    sqrt_result = int(product ** 0.5)
    return sqrt_result

def test_rooted_multiple() -> None:
    assert rooted_multiple(1, 2, 3, 4) == 4  # sqrt(24) = 4.898, int(4.898) = 4
    assert rooted_multiple(4, 9, 16) == 24  # sqrt(576) = 24, int(24) = 24
    assert rooted_multiple(1, 1, 1, 1) == 1  # sqrt(1) = 1, int(1) = 1
    assert rooted_multiple(2, 2, 2, 2) == 4  # sqrt(16) = 4, int(4) = 4
    print("All tests passed.")

if __name__ == "__main__":
    print("Result of rooted_multiple for (1, 2, 3, 4):", rooted_multiple(1, 2, 3, 4))
    test_rooted_multiple()