def area_of_circle(radius: float) -> float:
    """Assuming an approximate value PI = 3.142 that is hard-coded inside the function,
    calculates the area of a circle given the radius.
    Example:
    area_of_circle(7)"""
    # calculates the area of a circle given the radius using PI = 3.142.
    PI = 3.142
    # return the radius
    return PI * (radius**2)


def test_area_of_circle() -> None:
    """Tests the area_of_circle function."""
    # test 1 - radius 7
    assert area_of_circle(7) == 153.958
    # test 2 - radius 0
    assert area_of_circle(0) == 0
    # test 3 - radius 1
    assert area_of_circle(1) == 3.142
    # test 4 - radius 10
    assert area_of_circle(10) == 314.2
    print("All tests passed.")


if __name__ == "__main__":
    # example usage
    print(area_of_circle(7))  # Expected output: 153.958
    # run the tests
    test_area_of_circle()
