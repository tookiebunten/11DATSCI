def sum_powered(list) -> int: 
    """Receives a list. The sum of the first n - 1 elements is raised to the 
    power of the nth element. The resulting value is returned."""
    
    if len(list) < 2:
        raise ValueError("List must contain at least two elements.")
    
    sum_of_elements = sum(list[:-1])
    nth_element = list[-1]
    result = sum_of_elements ** nth_element
    return result

def test_sum_powered() -> None:
    assert sum_powered([1, 2, 3]) == 27  # (1 + 2) ** 3 = 3 ** 3 = 27
    assert sum_powered([2, 3, 2]) == 25  # (2 + 3) ** 2 = 5 ** 2 = 25
    assert sum_powered([1, 1, 1, 1, 2]) == 16  # (1 + 1 + 1 + 1) ** 2 = 4 ** 2 = 16
    assert sum_powered([0, 0, 0, 0, 3]) == 0  # (0 + 0 + 0 + 0) ** 3 = 0 ** 3 = 0
    print("All tests passed.")

if __name__ == "__main__":
    print("Result of sum powered for [1, 2, 3]:", sum_powered([1, 2, 3]))
    test_sum_powered()