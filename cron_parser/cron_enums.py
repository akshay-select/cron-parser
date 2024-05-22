from enum import Enum

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
