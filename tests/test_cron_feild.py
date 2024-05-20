import unittest
from cron_parser.cron_feild import CronFeild, CronFeildType

# Todo - Add more tests! 
class TestCronField(unittest.TestCase):
  def test_minute_field(self):
    field = CronFeild(CronFeildType.MINUTE, "*")
    parsed_values = field.parse()
    self.assertEqual(parsed_values, list(range(0, 60)))

  def test_day_of_month(self):
    field = CronFeild(CronFeildType.DAY_OF_MONTH, "15-20/3")
    parsed_values = field.parse()
    self.assertEqual(parsed_values, [15, 18])

  def test_day_of_week(self):
    field = CronFeild(CronFeildType.DAY_OF_WEEK, "1,3,4-5/1")
    parsed_values = field.parse()
    self.assertEqual(parsed_values, [1,3,4,5])

  def test_hour_feild(self):
    field = CronFeild(CronFeildType.HOUR, "1,21-23/2")
    parsed_values = field.parse()
    self.assertEqual(parsed_values, [1,21,23])

  def test_month_feild(self):
    field = CronFeild(CronFeildType.MONTH, "1-11/3")
    parsed_values = field.parse()
    self.assertEqual(parsed_values, [1, 4, 7, 10])
  
  def test_invalid_feild_expression(self):
    with self.assertRaises(ValueError):
       field = CronFeild(CronFeildType.MONTH, "4-3/3")
       field.parse() 
    
    with self.assertRaises(ValueError):
       field = CronFeild(CronFeildType.MINUTE, "100")
       field.parse() 
    
    with self.assertRaises(ValueError):
       field = CronFeild(CronFeildType.DAY_OF_MONTH, "32")
       field.parse() 
    
    with self.assertRaises(ValueError):
       field = CronFeild(CronFeildType.MONTH, "-1/2")
       field.parse() 
    
