import price_info
import pytest

# Test total_cost_shopping function
def test_total_cost_shopping():
    price_info.total_cost_shopping()  # Call the function without arguments
    expected_cost = 34.0

# Test cost_of_fruits function
def test_cost_of_fruits():
    price_info.cost_of_fruits('apple', 10)  # Call the function without arguments
    expected_cost = 12.0

if __name__ == '__main':
    pytest.main()

