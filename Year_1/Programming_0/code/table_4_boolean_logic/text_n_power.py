def text_n_power(text, power) -> int:
    """Converts text to its corresponding numerical value and raises it to the power of the given integer."""
    
    if text == "one":
        num = 1
    elif text == "two":
        num = 2
    elif text == "three":
        num = 3
    else:
        raise ValueError("Invalid text input. Expected 'one', 'two', or 'three'.")
    
    if power not in {1, 2, 3, 4, 5}:
        raise ValueError("Invalid power input. Expected an integer between 1 and 5.")
    
    return num ** power

def test_text_n_power() -> None:
    assert text_n_power("one", 2) == 1
    assert text_n_power("two", 3) == 8
    assert text_n_power("three", 2) == 9
    assert text_n_power("two", 4) == 16
    assert text_n_power("one", 5) == 1
    print("All tests passed.")

if __name__ == "__main__":
    # Simulate command line input
    args = ["three", 2]
    text = args[0]
    power = args[1]
    try:
        result = text_n_power(text, power)
        print(f"Result: {result}")
    except ValueError as e:
        print(e)
    test_text_n_power()
