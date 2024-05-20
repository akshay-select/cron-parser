import sys
from cron_parser import CronExpression
from utils import  print_table
import logging

def main():
  if len(sys.argv) != 2:
    logging.error("invalid input! please provide a valid cron expression followed by the command!")
    return
  
  inp_exp = sys.argv[1]
  print(f"The given expression is: {inp_exp}")
  try:
    result = CronExpression(expression=inp_exp).parse()
    print_table(result)
  except Exception as err:
     #Todo: Custom exception for invalid strings
     logging.error(f"an error occurred while parsing the expression. Error - {err}")
     return

if __name__ == "__main__":
    main()