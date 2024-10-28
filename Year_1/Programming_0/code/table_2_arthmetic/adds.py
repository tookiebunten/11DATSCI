def sum_list(numbers):
    """Receives a list of numbers, and returns the sum."""
    return sum(numbers)

def test_sum_list():
    assert sum_list([1, 2, 3, 4]) == 10
    assert sum_list([0, 0, 0, 0]) == 0
    assert sum_list([-1, -2, -3, -4]) == -10
    assert sum_list([1.5, 2.5, 3.5]) == 7.5
    print("All tests passed.")

if __name__ == "__main__":
    print("Result of sum_list for [1, 2, 3, 4]:", sum_list([1, 2, 3, 4]))
    test_sum_list()