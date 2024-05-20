import unittest
from utils.parsers import parse_expression, parse_comma, parse_range, parse_step, parse_value



class TestParseExpression(unittest.TestCase):
    def setUp(self) -> None:
        self.minutes = list(range(0,60))
        self.hours = list(range(0,24))
        self.days = list(range(1,32))
        return super().setUp()

    def test_valid_expression(self):
        self.assertEqual(parse_expression("0", self.minutes), [0])
        self.assertEqual(parse_expression("1-4/4", self.minutes), [1])
        self.assertEqual(parse_expression("23/2", self.hours), [23])
        self.assertEqual(parse_expression("*/31", self.days), [1])
        self.assertEqual(parse_expression("*/31,22,1-2", self.days), [1,22,1,2])
        self.assertEqual(parse_expression("22,*,28/3", self.days), [22]+self.days[:]+[28,31])
        
    def test_non_int(self):
        with self.assertRaises(ValueError):
            parse_expression("12/3,*,222", self.hours)
        with self.assertRaises(ValueError):
            parse_expression("*/3,*/*", self.hours)
        with self.assertRaises(ValueError):
            parse_expression("3/*,2,3", self.hours)
        with self.assertRaises(ValueError):
            parse_expression("3-2/2", self.hours)
        with self.assertRaises(ValueError):
            parse_expression("13.4,22", self.hours)
        with self.assertRaises(ValueError):
            parse_expression("2,3,5,6,8,8/1-2", self.hours)
        with self.assertRaises(ValueError):
            parse_expression("25/2", self.hours)
        
    def test_out_of_bounds(self):
        with self.assertRaises(ValueError):
            parse_expression("20-60", self.minutes)

        with self.assertRaises(ValueError):
            parse_expression("-1-24", self.hours)

        with self.assertRaises(ValueError):
            parse_expression("32-300", self.days)

class TestParseValue(unittest.TestCase):
    def setUp(self) -> None:
        self.minutes = list(range(0,60))
        self.hours = list(range(0,24))
        self.days = list(range(1,32))
        return super().setUp()

    def test_valid_range(self):
        self.assertEqual(parse_value("0", self.minutes), [0])
        self.assertEqual(parse_value("59", self.minutes), [59])
        self.assertEqual(parse_value("23", self.hours), [23])
        self.assertEqual(parse_value("31", self.days), [31])
    
    def test_non_int(self):
        with self.assertRaises(ValueError):
            parse_value("12/3", self.hours)
        with self.assertRaises(ValueError):
            parse_value("*/3", self.hours)
        with self.assertRaises(ValueError):
            parse_value("1-3", self.hours)
        with self.assertRaises(ValueError):
            parse_value("*", self.hours)
        with self.assertRaises(ValueError):
            parse_value("13.4", self.hours)
        
    def test_out_of_bounds(self):
        with self.assertRaises(ValueError):
            parse_value("60", self.minutes)

        with self.assertRaises(ValueError):
            parse_value("24", self.hours)

        with self.assertRaises(ValueError):
            parse_value("32", self.days)


class TestParseComma(unittest.TestCase):
    def setUp(self) -> None:
        self.minutes = list(range(0,60))
        self.hours = list(range(0,24))
        self.days = list(range(1,32))
        return super().setUp()
    
    def test_no_comma(self):
        self.assertEqual(parse_comma("1-2", self.days), [])
        self.assertEqual(parse_comma("1/2", self.days), [])
        self.assertEqual(parse_comma("*", self.days), [])
    
    def test_valid_commad(self):
        self.assertEqual(parse_comma("1,2,3",self.days), [1,2,3])
        self.assertEqual(parse_comma("*,1", self.days), self.days[:]+[1])
        self.assertEqual(parse_comma("1-2,3", self.days), [1,2,3])
        self.assertEqual(parse_comma("*/15,30", self.days), [1, 16, 31, 30])


class TestParseStep(unittest.TestCase):
    def setUp(self) -> None:
        self.days = list(range(1,32))
        self.day_of_week = list(range(0, 7))
        return super().setUp()
    
    def test_no_step(self):
        self.assertEqual(parse_step("1-2", self.days), [])
        self.assertEqual(parse_step("1,2", self.days), [])
        self.assertEqual(parse_step("*", self.days), [])

    def test_comma_and_step(self):
        self.assertEqual(parse_step("1,2/3", self.days), [])
    
    def test_valid_step(self):
        self.assertEqual(parse_step("*/10",self.days), [1, 11, 21, 31])
        self.assertEqual(parse_step("3/2", self.day_of_week), [3, 5])
        self.assertEqual(parse_step("23/2", self.days), [23, 25, 27, 29, 31])
        self.assertEqual(parse_step("10-12/2", self.days), [10, 12])
        self.assertEqual(parse_step("22-30/30", self.days), [22])
    
    def test_invalid_step(self):
        with self.assertRaises(ValueError):
            parse_step("22-12/30", self.days)
        
        with self.assertRaises(ValueError):
            parse_step("1-9/2", self.day_of_week)
        
        with self.assertRaises(ValueError):
            parse_step("30/2", self.day_of_week)

        # Handled by the parse_expression! 
        # with self.assertRaises(ValueError):
        #     parse_step("*/*", self.day_of_week)

class TestParseRange(unittest.TestCase):
    def setUp(self) -> None:
        self.days = list(range(1,32))
        self.day_of_week = list(range(0, 7))
        return super().setUp()
    
    def test_no_range(self):
        self.assertEqual(parse_range("1/2", self.days), [])
        self.assertEqual(parse_range("1,2", self.days), [])
        self.assertEqual(parse_range("*", self.days), [])
    
    def test_valid_range(self):
        self.assertEqual(parse_range("5-5",self.days), [5])
        self.assertEqual(parse_range("1-3", self.days), [1,2,3])
        self.assertEqual(parse_range("5", self.days), [])

    def test_invalid_range(self):
        with self.assertRaises(ValueError):
            parse_range("20-80",self.days)
        # Handled with parse_expression
        # with self.assertRaises(ValueError):
        #     parse_range("-1-20", self.days)

        with self.assertRaises(ValueError):
            parse_range("5-10", self.day_of_week)