def is_vowel(character: str) -> bool:
    """Checks if a given character is a vowel.
    Example:
    is_vowel('a') should return the boolean value True.
    If the character is not a vowel, it returns False."""
    # checks if a given character is a vowel.
    vowels = "AEIOU"
    # returns True if the character is a vowel
    return character.upper() in vowels


def test_is_vowel() -> None:
    """Tests the is_vowel function."""
    # test 1 - lowercase vowel
    assert is_vowel("a") is True
    # test 2 - uppercase vowel
    assert is_vowel("E") is True
    # test 3 - non-vowel character
    assert is_vowel("b") is False
    # test 4 - digit
    assert is_vowel("1") is False
    print("All tests passed.")


if __name__ == "__main__":
    # example usage
    print(is_vowel("a"))  # expected output - True
    print(is_vowel("b"))  # expected output - False
    # run the tests
    test_is_vowel()
