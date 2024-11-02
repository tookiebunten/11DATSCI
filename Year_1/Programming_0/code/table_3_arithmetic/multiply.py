def multiply_and_check_sign(*args):
    """Receives an arbitrary number of arguments (e.g. use *args, for example, 
    as a function argument). The function should multiply the arguments 
    together and return the string: 
    
    “is_signed”  
    
    …if the value is either negative or positive or: otherwise return the string: 
    
    “unsigned”"""
    
    if not args:
        return "unsigned"
    
    product = 1
    for num in args:
        product *= num
    
    if product != 0:
        return "is_signed"
    else:
        return "unsigned"

def test_multiply_and_check_sign():
    assert multiply_and_check_sign(1, 2, 3) == "is_signed"
    assert multiply_and_check_sign(-1, 2, 3) == "is_signed"
    assert multiply_and_check_sign(0, 2, 3) == "unsigned"
    assert multiply_and_check_sign() == "unsigned"
    print("All tests passed.")

if __name__ == "__main__":
    print("Result of multiply_and_check_sign for (1, 2, 3):", multiply_and_check_sign(1, 2, 3))
    test_multiply_and_check_sign()