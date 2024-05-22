import sys
from cron_parser import CronExpression
from utils import  print_table
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def main():
  if len(sys.argv) != 2:
    logging.error("Invalid input! please provide a valid cron expression along with the command!")
    return
  
  inp_exp = sys.argv[1]
  print(f"The given expression is: {inp_exp}")
  try:
    result = CronExpression(expression=inp_exp).parse()
    print_table(result)
  except ValueError as v_err:
     logging.error(f"Failed to parse the expression: \"{inp_exp}\", error: {v_err}")
  except Exception as err:
     logging.error(f"An unexpected error occurred: {err}")

if __name__ == "__main__":
    main()