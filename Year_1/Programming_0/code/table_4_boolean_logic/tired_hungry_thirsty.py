def determine_action(tired, hungry, thirsty) -> str:
    """Takes three states (tired, hungry, thirsty) and returns the corresponding action."""
    
    if tired:
        if hungry:
            if thirsty:
                return "eat and drink in bed"
            else:
                return "eat in bed"
        else:
            if thirsty:
                return "drink in bed"
            else:
                return "sleep"
    else:
        if hungry:
            if thirsty:
                return "drink and eat"
            else:
                return "eat"
        else:
            if thirsty:
                return "drink"
            else:
                return "do nothing"

def test_determine_action() -> None:
    assert determine_action(False, False, False) == "do nothing"
    assert determine_action(False, False, True) == "drink"
    assert determine_action(False, True, False) == "eat"
    assert determine_action(False, True, True) == "drink and eat"
    assert determine_action(True, False, False) == "sleep"
    assert determine_action(True, False, True) == "drink in bed"
    assert determine_action(True, True, False) == "eat in bed"
    assert determine_action(True, True, True) == "eat and drink in bed"
    print("All tests passed.")

if __name__ == "__main__":
    print("Result of determine_action for (False, False, False):", determine_action(False, False, False))
    test_determine_action()
