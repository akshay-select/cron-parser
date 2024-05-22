from utils.parsers import parse_expression
from .cron_enums import CronFeildRange, CronFeildType

class CronFeild:
    def __init__(self, type: CronFeildType, expression:str):
        self.type = type
        self.expression = expression

    def parse(self) -> list:
       field_range = list(CronFeildRange[self.type.name].value)
       return parse_expression(self.expression, field_range)