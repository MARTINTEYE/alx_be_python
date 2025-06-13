def safe_divide(numerator, denominator):
    """
    Safely divides two values with error handling.

    Parameters:
        numerator (str): The numerator input (should be convertible to float).
        denominator (str): The denominator input (should be convertible to float).

    Returns:
        str: The result or an appropriate error message.
    """
    try:
        num = float(numerator)
        denom = float(denominator)

        result = num / denom
        return f"Result: {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."  # ✅ Match expected error

