# sum_calculator.py

def calculate_sum(a, b):
    try:
        return a + b
    except TypeError:
        print("Error: Both inputs must be numbers.")
        return None
