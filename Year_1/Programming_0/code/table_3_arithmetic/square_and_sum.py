def square_and_multiply_by_phi(lst) -> list:
    """Receives a single list of numbers, takes the square of the values and stores 
    those to a local list, then returns that list, but before doing so multiplies 
    each element by the approximate value of the golden ratio ø (phi) contained 
    in the associated script where ø = 1.618."""
    
    phi = 1.618
    squared_and_multiplied = [(number ** 2) * phi for number in lst]
    return squared_and_multiplied

def test_square_and_multiply_by_phi() -> None:
    assert square_and_multiply_by_phi([0, 1, 2]) == [0.0, 1.618, 6.472]
    print("All tests passed.")

if __name__ == "__main__":
    print("Result of square_and_multiply_by_phi for [1, 2, 3]:", square_and_multiply_by_phi([1, 2, 3]))
    test_square_and_multiply_by_phi()