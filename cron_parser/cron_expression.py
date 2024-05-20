from .cron_feild import CronFeild, CronFeildType


# Todo - Avoid using indeces for order! 
class CronExpression:
    def __init__(self, expression):
        self.raw_expression = expression.strip()
        self.cron_feilds_raw = self.raw_expression.split(" ")

        if len(self.cron_feilds_raw) != 6:
            raise ValueError("Invalid cron expression, should have 6 feilds seperated by space")
        
        self.cron_feilds = []
        # Note: Order is important here! 
        for i, type in enumerate(list(CronFeildType)):
            self.cron_feilds.append(CronFeild(type, self.cron_feilds_raw[i]))
        
    def parse(self):
        resMap = {}
        for feild in self.cron_feilds[:-1]:
            feildName = feild.type.value
            resMap[feildName] = feild.parse()
        
        # Adding the command feild as well! 
        resMap[CronFeildType.COMMAND.value] = self.cron_feilds_raw[-1]
        return resMap