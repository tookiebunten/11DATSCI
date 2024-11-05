def to_uppercase(input_string) -> str:
    """Takes a string as input and returns a new string where all the characters are 
    converted to uppercase."""
    return input_string.upper()

def test_to_uppercase() -> None:
    assert to_uppercase("Hello World") == "HELLO WORLD"
    assert to_uppercase("python") == "PYTHON"
    assert to_uppercase("123abc") == "123ABC"
    assert to_uppercase("") == ""
    print("All tests passed.")

if __name__ == "__main__":
    print("Result of to_uppercase for 'Hello World':", to_uppercase("Hello World"))
    test_to_uppercase()