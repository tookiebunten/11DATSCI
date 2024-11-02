def process_lists(list1, list2) -> float:
    """Receives list1 and list2. Each element of list1 is multiplied to obtain the 
    product of the numbers. Each value of list2 is multiplied by the 
    aforementioned product. Then, the sum of the elements in list2 is multiplied 
    by the approximate value π (PI) = 3.14159 contained in the function."""
    
    if not list1 or not list2:
        raise ValueError("Both lists must contain at least one element.")
    
    product_list1 = 1
    for num in list1:
        product_list1 *= num
    
    modified_list2 = [num * product_list1 for num in list2]
    sum_modified_list2 = sum(modified_list2)
    
    result = sum_modified_list2 * 3.14159
    return result

def test_process_lists() -> None:
    assert process_lists([1, 2, 3], [4, 5, 6]) == 282.74309999999997  # (1*2*3) * (4+5+6) * 3.14159
    assert process_lists([2, 3], [1, 2, 3]) == 113.09724  # (2*3) * (1+2+3) * 3.14159
    assert process_lists([1], [1, 1, 1]) == 9.42477  # (1) * (1+1+1) * 3.14159
    assert process_lists([1, 2], [0, 0, 0]) == 0.0  # (1*2) * (0+0+0) * 3.14159
    print("All tests passed.")

if __name__ == "__main__":
    print("Result of process_lists for [1, 2, 3] and [4, 5, 6]:", process_lists([1, 2, 3], [4, 5, 6]))
    test_process_lists()