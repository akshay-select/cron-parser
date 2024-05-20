import unittest
from cron_parser import CronExpression

class TestCronExpression(unittest.TestCase):
    def test_valid_expression(self):
        expression = "*/15 0 1 1 * /usr/bin/find"
        cron_expr = CronExpression(expression)
        parsed = cron_expr.parse()
        expected = {
            "minute": [0, 15, 30, 45],
            "hour": [0],
            "day of month": [1],
            "month": [1],
            "day of week": [0,1,2,3,4,5,6],
            "command": "/usr/bin/find"
        }
        self.assertEqual(parsed, expected)

    def test_invalid_expression_length(self):
        with self.assertRaises(ValueError) as context:
            CronExpression("*/15 0 1 1 *")
        with self.assertRaises(ValueError) as context:
            CronExpression("*/15 0 1 1 * * command")

    def test_empty_expression(self):
        with self.assertRaises(ValueError) as context:
            CronExpression("")

    def test_edge_case_max_values(self):
        expression = "59 23 31 12 6 /usr/bin/find"
        cron_expr = CronExpression(expression)
        parsed = cron_expr.parse()
        expected = {
            "minute": [59],
            "hour": [23],
            "day of month": [31],
            "month": [12],
            "day of week": [6],
            "command": "/usr/bin/find"
        }
        self.assertEqual(parsed, expected)

    def test_edge_case_min_values(self):
        expression = "0 0 1 1 0 /usr/bin/find"
        cron_expr = CronExpression(expression)
        parsed = cron_expr.parse()
        expected = {
            "minute": [0],
            "hour": [0],
            "day of month": [1],
            "month": [1],
            "day of week": [0],
            "command": "/usr/bin/find"
        }
        self.assertEqual(parsed, expected)