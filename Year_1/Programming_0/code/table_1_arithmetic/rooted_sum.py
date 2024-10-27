def rooted_sum(list):
    """Receives a list of args. Returns as an integer the square root of the 
    sum of a list of numbers."""
    
    if not list:
        raise ValueError("List must contain at least one element.")
    
    sum_of_elements = sum(list)
    sqrt_result = int(sum_of_elements ** 0.5)
    return sqrt_result

def test_rooted_sum():
    assert rooted_sum([1, 2, 3, 4]) == 3  # sqrt(10) = 3.162, int(3.162) = 3
    assert rooted_sum([4, 9, 16]) == 5  # sqrt(29) = 5.385, int(5.385) = 5
    assert rooted_sum([1, 1, 1, 1]) == 2  # sqrt(4) = 2, int(2) = 2
    assert rooted_sum([0, 0, 0, 0]) == 0  # sqrt(0) = 0, int(0) = 0
    print("All tests passed.")

if __name__ == "__main__":
    print("Result of rooted sum for [1, 2, 3, 4]:", rooted_sum([1, 2, 3, 4]))
    test_rooted_sum()