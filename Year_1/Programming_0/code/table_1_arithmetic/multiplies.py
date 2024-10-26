def multiply_and_sum(list1, list2):
    """Receives list1 and list2, multiplies each element of list1, multiplies 
    each element of list2. This results in two numbers. The function returns 
    the sum of these numbers."""
    
    product1 = 1
    for number in list1:
        product1 *= number
    
    product2 = 1
    for number in list2:
        product2 *= number
    
    return product1 + product2

def test_multiply_and_sum():
    assert multiply_and_sum([1, 2, 3], [4, 5, 6]) == 126
    assert multiply_and_sum([1, 2], [3, 4]) == 14
    assert multiply_and_sum([0, 1], [2, 3]) == 6 
    assert multiply_and_sum([1.5, 2.5], [3.5, 4.5]) == 19.5
    print("All tests passed.")

if __name__ == "__main__":
    print("Result of multiplying and summing [1, 2, 3] and [4, 5, 6] = ", multiply_and_sum([1, 2, 3], [4, 5, 6]))
    test_multiply_and_sum()