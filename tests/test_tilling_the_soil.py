# *****************************************************************************
# *                                                                           *
# *   IMPORTANT: DO NOT MODIFY THIS FILE                                      *
# *                                                                           *
# *   This testing file is provided to help you check the functionality of    *
# *   your code and understand the requirements for this assignment.          *
# *                                                                           *
# *   Please review the tests carefully to understand what is expected, but   *
# *   DO NOT make any changes to this file. Modifying this file will          *
# *   interfere with the grading system, lead to incorrect results, and       *
# *   will be flagged as cheating.                                            *
# *                                                                           *
# *   Focus on writing your own code to meet the requirements outlined in the *
# *   tests.                                                                  *
# *                                                                           *
# *****************************************************************************


import subprocess
import math
import random
import subprocess
import pytest
import requests
import json
import socket
from common_setup import pre_test_setup, check_internet_connection, input_data

test_outputs = {}
test_name = None
test_points_awarded = {}
test_response_data = {}

def generate_valid_dimensions():
    return "\n".join(str(random.randint(1, 100)) for _ in range(8)) + "\n"

def compute_area(dimensions):
    dims = list(map(int, dimensions.strip().splitlines()))
    return sum(dims[i] * dims[i + 1] for i in range(0, len(dims), 2))


def compute_fertilizer_cost(area):
    return math.ceil(area / 2000) * 27


def compute_bag_count(area):
    return math.ceil(area / 2000)


def compute_hours_needed(area):
    return math.ceil(area / 2500)


def compute_labor_expense(hours):
    return hours * 20


def compute_nutrients(area):
    return round((area / 2000) * 1.0, 3), round((area / 2000) * 0.125, 3)

# This script runs ALL tests -- if you want to run separate tests, see the .tests folder
# This test has 1,233 tokens calling OpenAI gtp-4o model which costs $2.50 for 1 million tokens
# So it should cost $.004 or about half a penny for each time they run all test here using pytest

# In GitHub it runs each test separately which calls the API 8 times, so it will cost about $.032 each time they push their code

# This script runs ALL tests -- if you want to run separate tests, see the .tests folder
# This test has 1,233 tokens calling OpenAI gtp-4o model which costs $2.50 for 1 million tokens
# So it should cost $.004 or about half a penny for each time they run all test here using pytest

# In GitHub it runs each test separately which calls the API 8 times, so it will cost about $.032 each time they push their code

def test_all():

    test_outputs,test_points_awarded,test_feedback,test_response_data = pre_test_setup()# passing no tests means test everything
    if check_internet_connection():
        assert test_response_data['totalPointsAwarded'] == test_response_data['totalPointsPossible'], test_feedback

    else :
        #Setting up all expected values to compare
        expected_area = compute_area(input_data)
        expected_fertilizer_cost = compute_fertilizer_cost(expected_area)
        expected_bags = compute_bag_count(expected_area)
        expected_hours = compute_hours_needed(expected_area)
        expected_labor_cost = compute_labor_expense(expected_hours)
        expected_total_cost = expected_fertilizer_cost + expected_labor_cost
        expected_nitrogen, _ = compute_nutrients(expected_area)
        _, expected_potassium = compute_nutrients(expected_area)
        output = test_outputs["area"]

        assert str(expected_area) in output, f"Calculation incorrect. Expected area: {expected_area}"

        output = test_outputs["bags"]
        # Check the calculated number of bags
        assert str(expected_bags) in output, f"Calculation incorrect. Expected bags: {expected_bags}"

        output = test_outputs["fertilizer_cost"]
        # Check the calculated cost
        assert str(expected_fertilizer_cost) in output, f"Calculation incorrect. Expected cost: {expected_fertilizer_cost}"

        # Check the formatting of the cost
        assert f"${expected_fertilizer_cost:.2f}" in output, f"Formatting incorrect. Expected cost formatted with two decimal places: ${expected_fertilizer_cost:.2f}"

        output = test_outputs["hours"]
        # Check the calculated number of hours
        assert str(expected_hours) in output, f"Calculation incorrect. Expected hours: {expected_hours}"

        output = test_outputs["labor_cost"]
        # Check the calculated labor cost
        assert str(expected_labor_cost) in output, f"Calculation incorrect. Expected labor cost: {expected_labor_cost}"

        # Check the formatting of the labor cost
        assert f"${expected_labor_cost:.2f}" in output, f"Formatting incorrect. Expected labor cost formatted with a dollar sign and two decimals: ${expected_labor_cost}"

        output = test_outputs["nitrogen"]
        # Check the calculated nitrogen
        assert f"{expected_nitrogen:.3f}" in output, f"Calculation incorrect. Expected nitrogen: {expected_nitrogen:.3f}"

        # Check the formatting of the nitrogen value
        assert f"{expected_nitrogen:.3f}" in output, f"Formatting incorrect. Expected nitrogen formatted to three decimal places: {expected_nitrogen:.3f}"

        output = test_outputs["potassium"]
        # Check the calculated potassium
        assert f"{expected_potassium:.3f}" in output, f"Calculation incorrect. Expected potassium: {expected_potassium:.3f}"

        # Check the formatting of the potassium value
        assert f"{expected_potassium:.3f}" in output, f"Formatting incorrect. Expected potassium formatted to three decimal places: {expected_potassium:.3f}"

        output = test_outputs["total_cost"]
        # Check the calculated total cost
        assert str(expected_total_cost) in output, f"Calculation incorrect. Expected total cost: {expected_total_cost}"

        # Check the formatting of the total cost
        assert f"${expected_total_cost:.2f}" in output, f"Formatting incorrect. Expected total cost formatted with two decimal places and a dollar sign: ${expected_total_cost:.2f}"

if __name__ == '__main__':
    pytest.main()