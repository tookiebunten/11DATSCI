def smooth_list(lst) -> list:
    """Receives a list and returns a 'smoothed' version - i.e. a list where the value 
    of each element is the average of itself and the left and right adjacent 
    elements. 'Edge'elements at index 0 and index length - 1 should be 
    averaged with their right and left adjacent neighbour, respectively."""
    
    if len(lst) < 2:
        return lst
    
    smoothed = []
    smoothed.append((lst[0] + lst[1]) / 2)  # Edge element at index 0
    
    for number in range(1, len(lst) - 1):
        smoothed.append((lst[number - 1] + lst[number] + lst[number + 1]) / 3)
    
    smoothed.append((lst[-1] + lst[-2]) / 2)  # Edge element at index length - 1
    
    return smoothed

def test_smooth_list() -> None:
    assert smooth_list([1, 2, 3, 4, 5]) == [1.5, 2.0, 3.0, 4.0, 4.5]
    assert smooth_list([10, 20, 30, 40, 50]) == [15.0, 20.0, 30.0, 40.0, 45.0]
    assert smooth_list([1, 1, 1, 1, 1]) == [1.0, 1.0, 1.0, 1.0, 1.0]
    assert smooth_list([1, 2]) == [1.5, 1.5]
    assert smooth_list([5]) == [5]
    print("All tests passed.")

if __name__ == "__main__":
    print("Result of smooth_list for [1, 2, 3, 4, 5]:", smooth_list([1, 2, 3, 4, 5]))
    test_smooth_list()