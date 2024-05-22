import re

# Capture - (digits{1-99}) - (digits{1-99})
RANGE_PATTERN = r"^(\d{1,2})-(\d{1,2})$"

# Capture -  */num or num1/num2 or num1-num2/num3
STEP_PATTERN = r"^(\*|\d{1,2}|\d{1,2}\-\d{1,2})\/(\d+)$"


def parse_expression(exp, values=[]) -> list:
    """
    Parses a cron feild expression. 

    :return: List of integers. 
    :raises ValueError: If the expression is invalid. 
    """
    # print(exp, values)
    if exp == "*":
        return values

    comma_res = parse_comma(exp, values)
    if comma_res:
        return comma_res

    step_res = parse_step(exp, values)
    if step_res:
        return step_res
    
    range_res = parse_range(exp, values)
    if range_res:
        return range_res
    
    return parse_value(exp, values)

def parse_value(exp:str, values:list[int]) -> list[int]:
    """
    Parses a single value expression and returns and integer value. 

    :raises ValueError: If the exp is not an integer or out of range.
    """
    if not exp.isdigit():
        raise ValueError(f"value should an integer - {exp}")
    
    val = int(exp)
    if val < values[0] or val > values[-1]:
            raise ValueError(f"invalid value {exp}, should be with in the range of {values[0]} - {values[-1]}")
    return [val]

def parse_comma(exp:str, values:list[int]) -> list[int]:
    """
    Parse a comma-separated list of expressions. 
    
    :return: List of integers. 
    :raises ValueError: If any of the sub-expressions are invalid. 
    """    
    if "," not in exp:
        return []
    
    parts = exp.split(",")
    result = []
    for part in parts:
        result.extend(parse_expression(part, values))
    
    return result

def parse_range(exp:str, values:list[int]) -> list[int]:
    """
    Parse a range expression.

    :return: List of integers representing the parsed range.
    :raises ValueError: If the range is invalid or out of bounds.
    """
    match = re.match(RANGE_PATTERN, exp)

    if not match:
        return []
    
    start, end = int(match.group(1)), int(match.group(2))
    if start > end or start < values[0] or end > values[-1]:
        raise ValueError(f"invalid range '{start}-{end}', should be within the range of {values[0]} - {values[-1]}")
        
    return list(range(start, end+1))

def parse_step(exp:str, values:list[int]) -> list[int]:
    """
    Parse a step expression.

    :return: List of integers representing the parsed step expression.
    :raises ValueError: If the step value is not an integer.
    """
    match = re.match(STEP_PATTERN, exp)

    if not match:
        return []

    base = match.group(1)
    step = match.group(2)
    filtered_values = parse_expression(base, values)

    # If only a single value is given, consider it as the start of a range
    # that extends to the end of the allowed values.
    if len(filtered_values) == 1 and base.isdigit():
        filtered_values = list(range(filtered_values[0], values[-1]+1))

    if not step.isdigit():
        raise ValueError(f"invalid value {exp}, should be an integer with in the range of {values[0]} - {values[-1]}")
    step_value = int(step)
    
    return filtered_values[::step_value]

    
    

