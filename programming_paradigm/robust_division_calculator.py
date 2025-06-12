def safe_divide(numerator, denominator):
    try:
        # Convert inputs to floats
        num = float(numerator)
        denom = float(denominator)

        # Perform division
        result = num / denom
        return f"Result: {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Inputs must be numbers."
