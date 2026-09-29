import math

def calculate_bmi(weight, height_cm):
    return weight / ((height_cm / 100) ** 2)

def test_bmi():
    bmi = calculate_bmi(60, 165)
    assert math.isclose(bmi, 22.0386, rel_tol=1e-3)

if __name__ == "__main__":
    test_bmi()
    print("TC01 BMI test passed.")
