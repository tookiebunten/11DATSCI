def to_lowercase(input_string) -> str:
    """Takes a string as input and returns a new string where all the characters are 
    converted to lowercase."""
    return input_string.lower()

def test_to_lowercase() -> None:
    assert to_lowercase("Hello World") == "hello world"
    assert to_lowercase("PYTHON") == "python"
    assert to_lowercase("123ABC") == "123abc"
    assert to_lowercase("") == ""
    print("All tests passed.")

if __name__ == "__main__":
    print("Result of to_lowercase for 'Hello World':", to_lowercase("Hello World"))
    test_to_lowercase()