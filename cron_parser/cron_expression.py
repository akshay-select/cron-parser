from .cron_feild import CronFeild
from .cron_enums import CronFeildType

EXPECTED_CRON_FIELDS = 6
class CronExpression:
    def __init__(self, expression: str):
        self.raw_expression = expression.strip()
        self.cron_feilds_raw = self.raw_expression.split(" ")

        if len(self.cron_feilds_raw) != EXPECTED_CRON_FIELDS:
            raise ValueError(f"Invalid cron expression, should have {EXPECTED_CRON_FIELDS} feilds seperated by space")
        
        self.cron_feilds = []
        # Note: Order is important here! 
        for field_type, raw_field in zip(CronFeildType, self.cron_feilds_raw):
            self.cron_feilds.append(CronFeild(field_type, raw_field))
        
    def parse(self) -> dict[str, list]:
        result_map = {}
        # Exclude the last command field
        for feild in self.cron_feilds[:-1]:
            feildName = feild.type.value
            result_map[feildName] = feild.parse()
        
        # Adding the command feild! 
        result_map[CronFeildType.COMMAND.value] = [self.cron_feilds_raw[-1]]
        return result_map