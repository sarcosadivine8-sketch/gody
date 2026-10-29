# common_setup.py
import subprocess
import requests
import json
import socket
import os
import platform
import sys
import random
sys.path.append('..')
from central_setup.central_setup import (
    execute_logic,
    check_internet_connection,
    run_program,
    run_single_test,  # this function is called by the test files that import it from this file: common_setup.py
)

program_name = 'tilling_the_soil.py'

def run_test(test_name, test_description, error_message):
    run_single_test(test_name, test_description, error_message, pre_test_setup)

def generate_valid_dimensions():
    return [str(random.randint(1, 100)) for _ in range(8)]

# Define input data here as a list of strings (not joined with newlines)
input_data = generate_valid_dimensions()

# Test for area calculation
def logic_area():
    """Test for area calculation."""
    return run_program(input_data, program_name)

# Test for fertilizer cost calculation
def logic_fertilizer_cost():
    """Test for fertilizer cost calculation."""
    return run_program(input_data, program_name)

# Test for bags calculation
def logic_bags():
    """Test for bags calculation."""
    return run_program(input_data, program_name)

# Test for labor hours calculation
def logic_hours():
    """Test for labor hours calculation."""
    return run_program(input_data, program_name)

# Test for labor cost calculation
def logic_labor_cost():
    """Test for labor cost calculation."""
    return run_program(input_data, program_name)

# Test for total cost calculation
def logic_total_cost():
    """Test for total cost calculation."""
    return run_program(input_data, program_name)

# Test for nitrogen calculation
def logic_nitrogen():
    """Test for nitrogen calculation."""
    return run_program(input_data, program_name)

# Test for potassium calculation
def logic_potassium():
    """Test for potassium calculation."""
    return run_program(input_data, program_name)

def pre_test_setup(test_name=None):
    test_outputs = {}
    test_points_awarded = {}
    test_feedback = ""
    test_response_data = None

    if test_name:
        if test_name == "area":
            test_outputs["area"] = logic_area()
        elif test_name == "bags":
            test_outputs["bags"] = logic_bags()
        elif test_name == "fertilizer_cost":
            test_outputs["fertilizer_cost"] = logic_fertilizer_cost()
        elif test_name == "hours":
            test_outputs["hours"] = logic_hours()
        elif test_name == "labor_cost":
            test_outputs["labor_cost"] = logic_labor_cost()
        elif test_name == "nitrogen":
            test_outputs["nitrogen"] = logic_nitrogen()
        elif test_name == "potassium":
            test_outputs["potassium"] = logic_potassium()
        elif test_name == "total_cost":
            test_outputs["total_cost"] = logic_total_cost()
    else:
        test_outputs = {
            "area": logic_area(),
            "bags": logic_bags(),
            "fertilizer_cost": logic_fertilizer_cost(),
            "hours": logic_hours(),
            "labor_cost": logic_labor_cost(),
            "nitrogen": logic_nitrogen(),
            "potassium": logic_potassium(),
            "total_cost": logic_total_cost(),
        }

    if check_internet_connection():
        try:
            # Read the contents of the files
            with open('tilling_the_soil.py', 'r') as f:
                student_code = f.read()
            with open('tests/test_tilling_the_soil.py', 'r') as f:
                pytest_code = f.read()
            with open('.github/classroom/autograding.json', 'r') as f:
                autograding_config = json.load(f)

            # Pass the logic to the central_setup module
            test_outputs, test_points_awarded, test_feedback, test_response_data = execute_logic(
                test_name, test_outputs, student_code, pytest_code, autograding_config
            )

        except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
            print(f"API call failed: {e}")
            print("Proceeding without API response. Run the test again with a working API to receive more user-friendly feedback.")

    return test_outputs, test_points_awarded, test_feedback, test_response_data
