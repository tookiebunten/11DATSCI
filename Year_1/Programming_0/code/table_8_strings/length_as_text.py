def length_as_text(input_string) -> str:
    """Takes a string of length in the inclusive range between 1 and 4, and returns a string 
    (either "one", "two", "three", "four" or "error: string out of range")."""
    
    length_to_text = {
        1: "one",
        2: "two",
        3: "three",
        4: "four"
    }
    
    return length_to_text.get(len(input_string), "error: string out of range")

def test_length_as_text() -> None:
    assert length_as_text("a") == "one"
    assert length_as_text("ab") == "two"
    assert length_as_text("abc") == "three"
    assert length_as_text("abcd") == "four"
    assert length_as_text("") == "error: string out of range"
    assert length_as_text("abcde") == "error: string out of range"
    print("All tests passed.")

if __name__ == "__main__":
    print("Result of length_as_text for 'abc':", length_as_text("abc"))
    test_length_as_text()