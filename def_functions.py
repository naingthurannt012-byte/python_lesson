def is_valid_email(email):
    # ... (Validation logic)
    return True  # Or False based on validation

def has_sufficient_balance(account):
    # ... (Balance check logic)
    return True  # Or False based on balance

def can_access_resource(user, resource):
    # ... (Permission check logic)
    return True  # Or False based on permissions


def calculate_monthly_payment(principal: float, interest_rate: float, loan_term_years: int) -> float:
    """
    Calculates the monthly payment for a fixed-rate loan.

    Args:
        principal: The total amount borrowed (float).
        interest_rate: The annual interest rate (as a decimal, float).
        loan_term_years: The loan term in years (int).

    Returns:
        The monthly payment amount (float).

    Raises:
        ValueError: If any of the inputs are negative or zero.

    Example:
        >>> calculate_monthly_payment(100000, 0.05, 30)
        530.33 
    """
    if principal <= 0 or interest_rate <= 0 or loan_term_years <= 0:
        raise ValueError("All input values must be positive.")

    monthly_interest_rate = interest_rate / 12
    number_of_payments = loan_term_years * 12
    
    # Calculation logic for monthly payment (omitted for brevity)

    return monthly_payment

global_sum = 0  # Global variable

def calculate_mean_with_side_effect(numbers):
    global global_sum  # Modifying a global variable
    global_sum = sum(numbers)
    return global_sum / len(numbers)

calculate_mean_with_side_effect([5, 3, 4, 1, 1])

def calculate_mean(numbers):
    """Calculates the mean of a list of numbers."""
    return sum(numbers) / len(numbers)

calculate_mean([5, 3, 4, 1, 1])