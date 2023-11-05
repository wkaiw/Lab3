import employee_info
import pytest

def test_get_employees_by_age_range():
    result = employee_info.get_employees_by_age_range(30, 40)
    assert len(result) == 2  # Expected number of employees in the age range

def test_calculate_average_salary():
    average_salary = employee_info.calculate_average_salary()
    expected_average = (50000 + 60000 + 56000 + 70000 + 65000 + 60000) / 6
    assert average_salary == expected_average  # Expected average salary

def test_get_employees_by_dept():
    department = "Marketing"  # Choose a department to test
    employees_in_dept = employee_info.get_employees_by_dept(department)

    # Check if all employees in the result have the correct department
    for employee in employees_in_dept:
        assert employee["department"] == department

# Run pytest
if __name__ == '__main__':
    pytest.main()

