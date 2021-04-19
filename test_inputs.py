import unittest

#tests for a specific exception

def symbol(symbol_input):
    contains_digit = any(map(str.isdigit, symbol_input))
    contains_lower = any(map(str.islower, symbol_input))
    if contains_digit == True:
        raise ValueError("Symbol cannot contain a number")
    elif contains_lower == True:
        raise ValueError("Symbol cannot have lowercase letters")
    return symbol_input


def chart_type(chart_input):
    if chart_input not in range(1,3):    
        raise ValueError("Integer is not in range 1-2 or is a string, please try again")
    else:
        return chart_input

def time_series(series_input):
    if series_input not in range(1,5):    
        raise ValueError("Integer is not in range 1-4 or is a string, please try again")
    else:
        return series_input

def start_date(date_input):
    contains_letter = any(map(str.isalpha, date_input))
    if contains_letter == True:
        raise ValueError("Date cannot have any letters in it")
    if len(date_input) != 10:
        raise ValueError("Date format is not correct, remember to put it in YYYY-MM-DD format")
    # realDate = datetime.datetime.strptime(date_input, "%Y-%m-%d")
    date_list = date_input.split("-")
    if (len(date_list[0]) != 4) or (len(date_list[1]) != 2) or (len(date_list[2]) != 2):
        raise ValueError("Date format is not correct, remember to put it in YYYY-MM-DD format")
    else:
        return date_input

def end_date(date_input):
    contains_letter = any(map(str.isalpha, date_input))
    if contains_letter == True:
        raise ValueError("Date cannot have any letters in it")
    if len(date_input) != 10:
        raise ValueError("Date format is not correct, remember to put it in YYYY-MM-DD format")
    # realDate = datetime.datetime.strptime(date_input, "%Y-%m-%d")
    date_list = date_input.split("-")
    if (len(date_list[0]) != 4) or (len(date_list[1]) != 2) or (len(date_list[2]) != 2):
        raise ValueError("Date format is not correct, remember to put it in YYYY-MM-DD format")
    else:
        return date_input
class MyExcept(Exception):
    def __init__(self, msg, error_code):
        super().__init__(msg)
        self.error_code = error_code
    
def throw_ex(var):
    if var.isalpha:
        raise MyExcept("The symbol contains numbers", 4444)
    else:
        return True

class TestInputs(unittest.TestCase):

    def setUp(self):
        print("setUp")
        self.num = 1

    def test_symbol(self):
        # tests if the symbol contains numbers
        #symbol("AA4L")

        #tests if the symbol contains lowercase letters
        #symbol("aPPl")

        #This test case should work
        symbol("AAPL")



    def test_chart_type(self):
        result = chart_type(self.num)
        self.assertEqual(result, 1)

        self.num = 2
        result2 = chart_type(self.num)
        self.assertEqual(result2, 2)

        #this is not in the range from 1-2
        # self.num = 3
        # result3 = chart_type(self.num)
        #self.assertEqual(result3, 3)

        #also not in specified range
        # self.num = 0
        # result4 = chart_type(self.num)
        #self.assertEqual(result2, 1)

        #this is a string
        # self.num = "test"
        # result3 = chart_type(self.num)

    def test_time_series(self):
        result = time_series(self.num)
        self.assertEqual(result, 1)

        self.num = 4
        result2 = time_series(self.num)
        self.assertEqual(result2, 4)

        #this is a string
        # self.num = "test"
        # result3 = time_series(self.num)

    def test_start_date(self):
        self.testDate = "2021-03-07"
        result = start_date(self.testDate)
        self.assertEqual(result, self.testDate)

        #check if you can put in an invalid month or day
        # self.testDate = "2021-038-07"
        # result = start_date(self.testDate)
        # self.assertEqual(result, self.testDate)

        #check if you can put letters in the date
        # self.testDate = "20ab-03-07"
        # result = start_date(self.testDate)
        # self.assertEqual(result, self.testDate)

    def test_end_date(self):
        self.testDate = "2021-03-07"
        result = start_date(self.testDate)
        self.assertEqual(result, self.testDate)

        #check if you can put in an invalid month or day
        # self.testDate = "2021-038-07"
        # result = start_date(self.testDate)
        # self.assertEqual(result, self.testDate)

        #check if you can put letters in the date
        # self.testDate = "20ab-03-07"
        # result = start_date(self.testDate)
        # self.assertEqual(result, self.testDate)



if __name__ == '__main__':
    unittest.main()