def concatenate_strings(*args) -> str:
    """Takes two or more strings as input and returns a new string that is the result of joining 
    them together in the order they were passed."""
    return ''.join(args)

def test_concatenate_strings() -> None:
    assert concatenate_strings("Hello", " ", "World") == "Hello World"
    assert concatenate_strings("Python", "3") == "Python3"
    assert concatenate_strings("123", "ABC", "xyz") == "123ABCxyz"
    assert concatenate_strings("") == ""
    print("All tests passed.")

if __name__ == "__main__":
    print("Result of concatenate_strings for 'Hello', ' ', 'World':", concatenate_strings("Hello", " ", "World"))
    test_concatenate_strings()