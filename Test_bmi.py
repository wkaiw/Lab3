import Lab2.Lab2 as bmi
import pytest

def test_bmi_under_weight():
    # Test BMI < 18.5 for Underweight
    bmi_val, classification = bmi.calculate_bmi(weight=50, height=1.75)
    assert classification == -1

def test_bmi_normal_weight():
    # Test 18.5 <= BMI <= 25.0 for Normal Weight
    bmi_val, classification = bmi.calculate_bmi(weight=70, height=1.75)
    assert classification == 0

def test_bmi_over_weight():
    # Test BMI > 25.0 for Overweight
    bmi_val, classification = bmi.calculate_bmi(weight=90, height=1.75)
    assert classification == 1

if __name__ == '__main':
    pytest.main()
