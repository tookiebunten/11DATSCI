def list_variable_types(input_list) -> list:
    """Receives a list and returns a corresponding list containing the types of the variables 
    held in the received list."""
    return [type(item) for item in input_list]

def test_list_variable_types() -> None:
    assert list_variable_types([1, "string", 3.14, True]) == [int, str, float, bool]
    assert list_variable_types([None, [], {}, ()]) == [type(None), list, dict, tuple]
    assert list_variable_types(["a", "b", "c"]) == [str, str, str]
    assert list_variable_types([1, 2, 3]) == [int, int, int]
    print("All tests passed.")

if __name__ == "__main__":
    print("Result of list_variable_types for [1, 'string', 3.14, True]:", list_variable_types([1, "string", 3.14, True]))
    test_list_variable_types()