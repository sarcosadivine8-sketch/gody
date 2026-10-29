import subprocess
import math
import random

command = ["python", "tilling_the_soil.py"]


def execute_program(input_data):
    result = subprocess.run(command, input=input_data, text=True, capture_output=True)
    return result.stdout


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


# Test for area calculation
def test_area():
    input_data = generate_valid_dimensions()
    expected_area = compute_area(input_data)
    output = execute_program(input_data)

    # Check the calculated area
    assert str(expected_area) in output, f"Calculation incorrect. Expected area: {expected_area}"


# Test for fertilizer cost calculation
def test_fertilizer_cost():
    input_data = generate_valid_dimensions()
    expected_area = compute_area(input_data)
    expected_cost = compute_fertilizer_cost(expected_area)
    output = execute_program(input_data)

    # Check the calculated cost
    assert str(expected_cost) in output, f"Calculation incorrect. Expected cost: {expected_cost}"

    # Check the formatting of the cost
    assert f"${expected_cost:.2f}" in output, f"Formatting incorrect. Expected cost formatted with two decimal places: ${expected_cost:.2f}"


# Test for bags calculation
def test_bags():
    input_data = generate_valid_dimensions()
    expected_area = compute_area(input_data)
    expected_bags = compute_bag_count(expected_area)
    output = execute_program(input_data)

    # Check the calculated number of bags
    assert str(expected_bags) in output, f"Calculation incorrect. Expected bags: {expected_bags}"


# Test for labor hours calculation
def test_hours():
    input_data = generate_valid_dimensions()
    expected_area = compute_area(input_data)
    expected_hours = compute_hours_needed(expected_area)
    output = execute_program(input_data)

    # Check the calculated number of hours
    assert str(expected_hours) in output, f"Calculation incorrect. Expected hours: {expected_hours}"

# Test for labor cost calculation
def test_labor_cost():
    input_data = generate_valid_dimensions()
    expected_area = compute_area(input_data)
    expected_hours = compute_hours_needed(expected_area)
    expected_labor_cost = compute_labor_expense(expected_hours)
    output = execute_program(input_data)

    # Check the calculated labor cost
    assert str(expected_labor_cost) in output, f"Calculation incorrect. Expected labor cost: {expected_labor_cost}"

    # Check the formatting of the labor cost
    assert f"${expected_labor_cost:.2f}" in output, f"Formatting incorrect. Expected labor cost formatted with a dollar sign and two decimals: ${expected_labor_cost}"

    # Test for total cost calculation
def test_total_cost():
    input_data = generate_valid_dimensions()
    expected_area = compute_area(input_data)

    # Compute fertilizer cost and labor cost
    expected_fertilizer_cost = compute_fertilizer_cost(expected_area)
    expected_hours = compute_hours_needed(expected_area)
    expected_labor_cost = compute_labor_expense(expected_hours)

    # Total cost is the sum of fertilizer and labor cost
    expected_total_cost = expected_fertilizer_cost + expected_labor_cost
    output = execute_program(input_data)

    # Check the calculated total cost
    assert str(expected_total_cost) in output, f"Calculation incorrect. Expected total cost: {expected_total_cost}"

    # Check the formatting of the total cost
    assert f"${expected_total_cost:.2f}" in output, f"Formatting incorrect. Expected total cost formatted with two decimal places and a dollar sign: ${expected_total_cost:.2f}"

# Test for total cost calculation
def test_total_cost():
    input_data = generate_valid_dimensions()
    expected_area = compute_area(input_data)

    # Compute fertilizer cost and labor cost
    expected_fertilizer_cost = compute_fertilizer_cost(expected_area)
    expected_hours = compute_hours_needed(expected_area)
    expected_labor_cost = compute_labor_expense(expected_hours)

    # Total cost is the sum of fertilizer and labor cost
    expected_total_cost = expected_fertilizer_cost + expected_labor_cost
    output = execute_program(input_data)

    # Check the calculated total cost
    assert str(expected_total_cost) in output, f"Calculation incorrect. Expected total cost: {expected_total_cost}"

    # Check the formatting of the total cost
    assert f"${expected_total_cost:.2f}" in output, f"Formatting incorrect. Expected total cost formatted with two decimal places and a dollar sign: ${expected_total_cost:.2f}"


# Test for nitrogen calculation
def test_nitrogen():
    input_data = generate_valid_dimensions()
    expected_area = compute_area(input_data)
    expected_nitrogen, _ = compute_nutrients(expected_area)
    output = execute_program(input_data)

    # Check the calculated nitrogen
    assert f"{expected_nitrogen:.3f}" in output, f"Calculation incorrect. Expected nitrogen: {expected_nitrogen:.3f}"

    # Check the formatting of the nitrogen value
    assert f"{expected_nitrogen:.3f}" in output, f"Formatting incorrect. Expected nitrogen formatted to three decimal places: {expected_nitrogen:.3f}"


# Test for potassium calculation
def test_potassium():
    input_data = generate_valid_dimensions()
    expected_area = compute_area(input_data)
    _, expected_potassium = compute_nutrients(expected_area)
    output = execute_program(input_data)

    # Check the calculated potassium
    assert f"{expected_potassium:.3f}" in output, f"Calculation incorrect. Expected potassium: {expected_potassium:.3f}"

    # Check the formatting of the potassium value
    assert f"{expected_potassium:.3f}" in output, f"Formatting incorrect. Expected potassium formatted to three decimal places: {expected_potassium:.3f}"
