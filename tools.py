COURSE_FEES = {
    "CS101": 12000,
    "AI202": 18000,
    "DS303": 15000
}


def get_course_fee(course_code):
    """Get the fee of a course."""
    return COURSE_FEES.get(course_code)


def calculator(expression):
    """Calculate a mathematical expression."""
    try:
        return eval(expression, {"__builtins__": {}})
    except Exception as e:
        return f"Calculation error: {e}"