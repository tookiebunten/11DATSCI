def elementwise_multiply(list1, list2):
    """Receives list1 and list2. Each element of list1 is multiplied by the corresponding element in list 2 to produce a third list, 
    the result of those element-wise multiples. Ensure that list1 and list2 are the same size, otherwise return an empty list."""
    
    if len(list1) != len(list2):
        return []
    
    result = [a * b for a, b in zip(list1, list2)]
    return result

def test_elementwise_multiply():
    assert elementwise_multiply([1, 2, 3], [4, 5, 6]) == [4, 10, 18]
    assert elementwise_multiply([1, 2], [3, 4, 5]) == []
    assert elementwise_multiply([0, 1], [2, 3]) == [0, 3]
    assert elementwise_multiply([1.5, 2.5], [3.5, 4.5]) == [5.25, 11.25]
    print("All tests passed.")

if __name__ == "__main__":
    print("Result of elementwise_multiply for [1, 2, 3] and [4, 5, 6]:", elementwise_multiply([1, 2, 3], [4, 5, 6]))
    test_elementwise_multiply()