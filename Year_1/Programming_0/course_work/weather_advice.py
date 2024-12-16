def weather_advice(
    sunny: bool, rainy: bool, windy: bool, temperature: float
) -> list[str]:
    """The function evaluates weather conditions based on three boolean
    inputs: sunny, rainy, and windy, and one float temperature.

    It returns a list of advice strings based on these inputs using predefined advice strings provided in the script.

    If it is sunny, the function adds "Wear sun cream."
    If it is sunny and hot (temperature greater than 25°C), it also adds "It's hot and sunny! Eat some ice cream."
    If it is rainy, the function adds "Carry an umbrella." to the advice.
    If it is both rainy and windy, it adds "It's windy! Hold onto your umbrella tightly."
    Lastly, if it's windy (regardless of rain or sun), the function adds "Hold on to your hat."

    The advice is built dynamically based on the input conditions, and no changes are made to the predefined,
    provided advice strings (these will be used in tests and you will lose marks if you change them)."""
    advice = []

    if sunny:
        advice.append("Wear sun cream.")
        if temperature > 25:
            advice.append("It's hot and sunny! Eat some ice cream.")

    if rainy:
        advice.append("Carry an umbrella.")
        if windy:
            advice.append("It's windy! Hold onto your umbrella tightly.")

    if windy:
        advice.append("Hold on to your hat.")

    return advice


def test_weather_advice() -> None:
    """Tests the weather_advice function."""
    # test 1 - sunny and hot
    assert weather_advice(True, False, False, 30) == [
        "Wear sun cream.",
        "It's hot and sunny! Eat some ice cream.",
    ]
    # test 2 - rainy and windy
    assert weather_advice(False, True, True, 20) == [
        "Carry an umbrella.",
        "It's windy! Hold onto your umbrella tightly.",
        "Hold on to your hat.",
    ]
    # test 3 - Windy only
    assert weather_advice(False, False, True, 15) == ["Hold on to your hat."]
    # test 4 - Sunny, rainy, and windy
    assert weather_advice(True, True, True, 22) == [
        "Wear sun cream.",
        "Carry an umbrella.",
        "It's windy! Hold onto your umbrella tightly.",
        "Hold on to your hat.",
    ]
    print("All tests passed.")


if __name__ == "__main__":
    # example usage
    print(
        weather_advice(True, False, False, 30)
    )  # expected output - ["Wear sun cream.", "It's hot and sunny! Eat some ice cream."]
    print(
        weather_advice(False, True, True, 20)
    )  # expected output - ["Carry an umbrella.", "It's windy! Hold onto your umbrella tightly.", "Hold on to your hat."]
    # run the test cases
    test_weather_advice()
