import pytest
from common_setup import run_test

def test_area():

    # the first parameter is the name of the test file in /tests
    # the second parameter is the name of the test in autograding.json
    # the third parameter is the error message to display if the test fails
    run_test("total_cost", "Student's total cost calculation is correct", "Calculation incorrect or incorrect formatting for total cost")

if __name__ == '__main__':
    pytest.main()