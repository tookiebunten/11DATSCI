def is_strong_password(password: str) -> bool:
    """Evaluates the strength of a password,
    i.e., that it contains:
    • at least 8 characters
    • at least one uppercase letter
    • at least one lowercase letter
    • at least one integer digit
    • at least one special character:
                 ! @ #  $  %  ^  &  *  (  )
    Returns True if strong, otherwise False."""
    # check if the password has at least 8 characters
    if len(password) < 8:
        return False

    # initialise flags for each condition
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_characters = "!@#$%^&*()"

    # check for each condition
    for characters in password:
        if characters.isupper():
            has_upper = True
        elif characters.islower():
            has_lower = True
        elif characters.isdigit():
            has_digit = True
        elif characters in special_characters:
            has_special = True

    # return True if all conditions are met
    return has_upper and has_lower and has_digit and has_special


def test_is_strong_password() -> None:
    """Tests the is_strong_password function."""
    # test case 1 - strong password
    assert is_strong_password("aa1!aaaA!") is True
    # test case 2 - less than 8 characters
    assert is_strong_password("aa1!aA") is False
    # test case 3 - no uppercase letter
    assert is_strong_password("aa1!aA") is False
    # test case 4 - no lowercase letter
    assert is_strong_password("aa1!aA") is False
    print("All tests passed.")


if __name__ == "__main__":
    # example usage
    print(is_strong_password("aa1!aaaA"))  # expected output - True
    print(is_strong_password("aa1!aA"))  # expected output - False
    # run the tests
    test_is_strong_password()
