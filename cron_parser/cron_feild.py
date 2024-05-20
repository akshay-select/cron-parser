from enum import Enum
from utils.parsers import parse_expression

# Todo - Extract enums to a new class! 
class CronFeildType(Enum):
  MINUTE = "minute"
  HOUR = "hour"
  DAY_OF_MONTH = "day of month"
  MONTH = "month"
  DAY_OF_WEEK = "day of week"
  COMMAND = "command" 

class CronFeildRange(Enum):
    MINUTE = range(0, 60)
    HOUR = range(0, 24)
    DAY_OF_MONTH = range(1, 32)
    MONTH = range(1, 13)
    DAY_OF_WEEK = range(0, 7)


class CronFeild:
    def __init__(self, type:CronFeildType, expression:str):
        self.type = type
        self.expression = expression

    def parse(self):
       return parse_expression(self.expression, list(CronFeildRange[self.type.name].value))