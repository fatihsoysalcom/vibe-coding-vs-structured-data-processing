# This script demonstrates 'vibe coding' (quick, unplanned) versus a more structured, maintainable approach
# for a simple data processing task: calculating the average of numbers from a string.

# --- Vibe Coding Approach (Hızlıca bir şeyler yapalım, çalışsın yeter) ---
# Characterized by:
# - Minimal planning, direct implementation.
# - Ignoring edge cases or handling them silently/poorly.
# - Lack of modularity or clear function boundaries.
# - Focus on immediate functionality, not long-term maintainability.

def vibe_coded_average_calculator(data_string: str):
    """Calculates average quickly, ignoring errors and edge cases."""
    print("\n--- Vibe Coding Approach ---")
    print(f"Input: '{data_string}'")
    
    # Vibe coding: Directly process without much thought for structure or error handling.
    # If data_string is empty or only contains invalid items, this might crash or return unexpected results.
    # Errors are silently skipped, potentially leading to incorrect averages without warning.
    numbers = []
    for item in data_string.split(','):
        try:
            numbers.append(float(item.strip()))
        except ValueError:
            # Vibe coding: Silently ignore invalid data. No warning, no specific handling.
            pass # This hides potential data quality issues.
    
    if not numbers:
        # Vibe coding: This check might be an afterthought, or not present at all.
        # If not present, `sum(numbers) / len(numbers)` would raise ZeroDivisionError.
        print("Result: No valid numbers found to calculate average (vibe coded).")
        return None

    total = sum(numbers)
    count = len(numbers)
    average = total / count # Simple calculation, assumes 'count' is never zero if 'numbers' is not empty.
    print(f"Calculated numbers: {numbers}")
    print(f"Vibe Coded Average: {average:.2f}")
    return average


# --- Structured Coding Approach (Mimari planlama, detaylı tasarım, kapsamlı test) ---
# Characterized by:
# - Clear function definitions with single responsibilities.
# - Explicit error handling and user feedback.
# - Robustness against edge cases (e.g., empty input, invalid data).
# - Readability and maintainability.

def parse_numbers_robustly(data_string: str) -> list[float]:
    """Parses a comma-separated string into a list of floats, providing feedback on invalid items."""
    valid_numbers = []
    invalid_items = []
    for item in data_string.split(','):
        stripped_item = item.strip()
        if not stripped_item: # Handle empty strings resulting from e.g. '10,,20'
            continue
        try:
            valid_numbers.append(float(stripped_item))
        except ValueError:
            # Structured coding: Explicitly report invalid data points.
            invalid_items.append(stripped_item)
            
    if invalid_items:
        print(f"Warning: The following items were invalid and skipped: {', '.join(invalid_items)}")
    return valid_numbers

def calculate_average_safely(numbers: list[float]) -> float | None:
    """Calculates the average of a list of numbers, returns None if the list is empty."""
    if not numbers:
        # Structured coding: Explicitly handle the empty list edge case to prevent ZeroDivisionError.
        return None
    return sum(numbers) / len(numbers)

def structured_average_calculator(data_string: str):
    """Orchestrates robust parsing and safe average calculation."""
    print("\n--- Structured Coding Approach ---")
    print(f"Input: '{data_string}'")
    
    # Structured coding: Break down the problem into smaller, testable functions.
    parsed_data = parse_numbers_robustly(data_string)
    
    if not parsed_data:
        print("Result: No valid numbers found to calculate average (structured).")
        return None

    average = calculate_average_safely(parsed_data)
    print(f"Calculated numbers: {parsed_data}")
    print(f"Structured Average: {average:.2f}")
    return average


# --- Demonstration --- 

# Scenario 1: Valid data with one invalid entry
print("\n--- Scenario 1: Mixed Valid and Invalid Data ---")
vibe_coded_average_calculator("10, 20, invalid, 40, 50")
structured_average_calculator("10, 20, invalid, 40, 50")

# Scenario 2: All valid data
print("\n--- Scenario 2: All Valid Data ---")
vibe_coded_average_calculator("100, 200, 300")
structured_average_calculator("100, 200, 300")

# Scenario 3: Empty string input
print("\n--- Scenario 3: Empty Input String ---")
vibe_coded_average_calculator("")
structured_average_calculator("")

# Scenario 4: Only invalid data
print("\n--- Scenario 4: Only Invalid Data ---")
vibe_coded_average_calculator("abc, def, ghi")
structured_average_calculator("abc, def, ghi")

# Scenario 5: String with extra commas (e.g., '10,,20')
print("\n--- Scenario 5: Data with Extra Commas ---")
vibe_coded_average_calculator("10,,20,30")
structured_average_calculator("10,,20,30")
