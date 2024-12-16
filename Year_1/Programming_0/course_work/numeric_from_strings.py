def numeric_from_strings(list_of_strings: list) -> int:
    """Converts a list of strings representing numbers ('zero' to 'nine') into a single integer.
    Example: Input: ['one', 'zero', 'two', 'nine', 'zero']
    Returns: 10290."""
    # mapping of words to numbers
    number_map = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    # join the numbers to form a single string
    result = "".join(number_map[word] for word in list_of_strings)
    # convert the string to an integer
    return int(result)


def test_numeric_from_strings():
    """Tests the numeric_from_strings function."""
    # test 1 - normal case
    assert numeric_from_strings(["one", "zero", "two", "nine", "zero"]) == 10290
    # test 2 single digit
    assert numeric_from_strings(["five"]) == 5
    # test 3 - all digits
    assert (
        numeric_from_strings(
            [
                "zero",
                "one",
                "two",
                "three",
                "four",
                "five",
                "six",
                "seven",
                "eight",
                "nine",
            ]
        )
        == 123456789
    )
    # test 4 - repeated digits
    assert numeric_from_strings(["nine", "nine", "nine"]) == 999
    print("All tests passed.")


if __name__ == "__main__":
    # example usage
    print(
        numeric_from_strings(["one", "zero", "two", "nine", "zero"])
    )  # expected output - 10290
    # run the tests
    test_numeric_from_strings()
