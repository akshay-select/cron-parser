import re

# Capture - (digits{1-99}) - (digits{1-99})
range_pattern = r"^(\d{1,2})-(\d{1,2})$"

# Capture -  */num or num1/num2 or num1-num2/num3
step_pattern = r"^(\*|\d{1,2}|\d{1,2}\-\d{1,2})\/(\d+)$"


def parse_expression(exp, values=[]):
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

def parse_value(exp, values):
    if not exp.isdigit():
        raise ValueError(f"value should an integer - {exp}")
    
    val = int(exp)
    if val < values[0] or val > values[-1]:
            raise ValueError(f"invalid value {exp}, should be with in the range of {values[0]} - {values[-1]}")
    return [val]

def parse_comma(exp, values):
    if "," not in exp:
        return []
    
    vals = exp.split(",")
    res = []
    for val in vals:
        res.extend(parse_expression(val, values))
    
    return res

def parse_range(exp, values):
    match = re.match(range_pattern, exp)

    if not match:
        return []
    
    start, end = int(match.group(1)), int(match.group(2))
    if start > end or start < values[0] or end > values[-1]:
        # invalid
        raise ValueError(f"invalid range '{start}-{end}', should be within the range of {values[0]} - {values[-1]}")
        
    return list(range(start, end+1))

def parse_step(exp, values):
    match = re.match(step_pattern, exp)

    if not match:
        return []

    filtered_values = parse_expression(match.group(1), values)
    # This can be ommited for now!
    if len(filtered_values) == 1 and match.group(1).isdigit():
        # Consider as start with end as rest of the items
        filtered_values = list(range(filtered_values[0], values[-1]+1))

    if not match.group(2).isdigit():
        raise ValueError(f"invalid value {exp}, should be an integer with in the range of {values[0]} - {values[-1]}")
    step_value = int(match.group(2))
    
    # start, step = int(match.groups[0]), int(match.groups[0])
    return filtered_values[::step_value]

    
    

