# common_setup.py
import subprocess
import requests
import json
import socket
import os
import random
import math

def generate_valid_dimensions():
    return "\n".join(str(random.randint(1, 100)) for _ in range(8)) + "\n"

# Define input_data here
input_data = generate_valid_dimensions()


def check_internet_connection():
    """Check if there is an active internet connection."""
    try:
        # Try to connect to a known server (Google's public DNS server)
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except OSError:
        return False

def run_program(input_data):
    """Run the student's program using subprocess and return the output."""

    # Run the student's program and capture output
    result = subprocess.run(
        ['python3', 'tilling_the_soil.py'],  # Adjust this command if using a different Python version or path
        input=input_data,
        text=True,
        capture_output=True,
        check=True  # If check is True and the exit code was non-zero, it raises a
                    # CalledProcessError. The CalledProcessError object will have the return code
                    # in the returncode attribute, and output & stderr attributes if those streams
                    # were captured.
    )

    return result.stdout  # Capture standard output

# Test for area calculation
def logic_area(input_data):
    output = run_program(input_data)
    return output

# Test for fertilizer cost calculation
def logic_fertilizer_cost(input_data):
    output = run_program(input_data)
    return output


# Test for bags calculation
def logic_bags(input_data):
    output = run_program(input_data)
    return output

# Test for labor hours calculation
def logic_hours(input_data):
    output = run_program(input_data)
    return output

# Test for labor cost calculation
def logic_labor_cost(input_data):
    output = run_program(input_data)
    return output

    # Test for total cost calculation
def logic_total_cost(input_data):
    output = run_program(input_data)
    return output

# Test for nitrogen calculation
def logic_nitrogen(input_data):
   output = run_program(input_data)
   return output


# Test for potassium calculation
def logic_potassium(input_data):
    output = run_program(input_data)
    return output


def pre_test_setup(test_name=None):
    test_outputs={}
    test_points_awarded={}
    test_feedback={}

    test_response_data = None
    if test_name:
        if test_name == "area":
            test_outputs["area"] = logic_area(input_data)
        elif test_name == "bags":
            test_outputs["bags"] = logic_bags(input_data)
        elif test_name == "fertilizer_cost":
            test_outputs["fertilizer_cost"] = logic_fertilizer_cost(input_data)
        elif test_name == "hours":
            test_outputs["hours"] = logic_hours(input_data)
        elif test_name == "labor_cost":
            test_outputs["labor_cost"] = logic_labor_cost(input_data)
        elif test_name == "nitrogen":
            test_outputs["nitrogen"] = logic_nitrogen(input_data)
        elif test_name == "potassium":
            test_outputs["potassium"] = logic_potassium(input_data)
        elif test_name == "total_cost":
            test_outputs["total_cost"] = logic_total_cost(input_data)
    else:
        test_outputs = {
            "area": logic_area(input_data),
            "bags": logic_bags(input_data),
            "fertilizer_cost": logic_fertilizer_cost(input_data),
            "hours": logic_hours(input_data),
            "labor_cost": logic_labor_cost(input_data),
            "nitrogen": logic_nitrogen(input_data),
            "potassium": logic_potassium(input_data),
            "total_cost": logic_total_cost(input_data),
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

            # Determine which test is being run
            if test_name:
                print(f"Running test: {test_name}")
                # Filter the autograding config to include only the relevant section - this avoids grading on unnecessary criteria
                relevant_tests = [test for test in autograding_config["tests"] if f"/{test_name}.py" in test["run"]]
                autograding_config["tests"] = relevant_tests
               # print('Autograding Config: '+json.dumps(autograding_config))


            # Prepare the data for the POST request
            data = {
                "studentCode": student_code,
                "pytestCode": pytest_code,
                "autogradingConfig": json.dumps(autograding_config),
                "terminalOutputs": list(test_outputs.values())
            }

            # Send the POST request
            response = requests.post('https://autograding-api-next.vercel.app/api/autograde', json=data)
            response.raise_for_status()  # Raise an exception for HTTP errors

            # Parse the response
            test_response_data = response.json()

            # Store the points awarded for each test
            test_points_awarded.update({test['name']: test['pointsAwarded'] for test in test_response_data["tests"]})

        except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
            print(f"API call failed: {e}")
            print("Proceeding without API response. Run the test again with a working API to receive more user-friendly feedback.")


    if check_internet_connection() and test_response_data:
        # Print the results in a well-formatted manner
        test_feedback = (
            "\nTest Results:\n"
            + "\n".join(
                [
                    f"Test Name: {test['name']}\nPoints Awarded: {test['pointsAwarded']}\nFeedback: {test['feedback']}\n"
                    for test in test_response_data["tests"]
                ]
            )
            + f"\nTotal Points Awarded: {test_response_data['totalPointsAwarded']}\n"
            + f"Total Points Possible: {test_response_data['totalPointsPossible']}\n"
            + "\nSpecific Code Feedback:\n"
            + "\n".join(
                [
                    f"Line {feedback['line']}: {feedback['feedback']}\nRecommendation: {feedback['recommendation']}\n"
                    for feedback in test_response_data["specificCodeFeedback"]["code"]
                ]
            )
            + "\nGeneral Feedback:\n"
            + test_response_data["specificCodeFeedback"]["general"]
        )

    else:
        print("No active internet connection or API response. Run the test again with an active internet connection and a working API to receive more user-friendly feedback.")

    return test_outputs,test_points_awarded,test_feedback, test_response_data

def run_test(test_name, test_point_key, offline_feedback):
    test_outputs, test_points_awarded, test_feedback, test_response_data = pre_test_setup(test_name=test_name)
    output = test_outputs[test_name]

    # Load points from autograding.json
    with open('.github/classroom/autograding.json', 'r') as f:
        autograding_config = json.load(f)

    # Find the points for the specific test
    test_config = next((test for test in autograding_config["tests"] if test["name"] == test_point_key), None)
    expected_points = test_config["points"] if test_config else 0

    if check_internet_connection():
        assert test_points_awarded.get(test_point_key, 0) == expected_points, test_feedback
    else:
        assert offline_feedback in output.strip(), offline_feedback