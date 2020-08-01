import unittest
from assignments.list.FunctionsForListManipulation import FunctionsForListManipulation as fn


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.two_number_elements = [1, 2]
        self.two_string_elements = ['JoJo', 'Obi']
        self.three_string_elements = ['Aunt Sue', 'Aunt Ify', 'Uncle Osy']
        self.empty_list = []
        self.seven_list_of_fruits = ['Banana', 'Apple', 'Pineapple', 'Blackberries', 'Mango', 'Strawberry', 'Orange']

    def test_return_last_element(self):
        assert fn.return_last_element(self.two_number_elements) == 2
        assert fn.return_last_element(self.two_string_elements) == 'Obi'
        assert fn.return_last_element(self.three_string_elements) == 'Uncle Osy'
        assert fn.return_last_element(self.empty_list) == "Error: IndexOutOfBound"
        assert fn.return_last_element(self.seven_list_of_fruits) == 'Orange'

    def test_return_first_element(self):
        assert fn.return_first_element(self.two_number_elements) == 1
        assert fn.return_first_element(self.two_string_elements) == 'JoJo'
        assert fn.return_first_element(self.three_string_elements) == 'Aunt Sue'
        assert fn.return_first_element(self.empty_list) == "Error: IndexOutOfBound"
        assert fn.return_first_element(self.seven_list_of_fruits) == 'Banana'

    def test_return_second_element(self):
        assert fn.return_second_element(self.two_number_elements) == 2
        assert fn.return_second_element(self.two_string_elements) == 'Obi'
        assert fn.return_second_element(self.three_string_elements) == 'Aunt Ify'
        assert fn.return_second_element(self.empty_list) == "Error: IndexOutOfBound"
        assert fn.return_second_element(self.seven_list_of_fruits) == 'Apple'

    def test_return_third_element(self):
        assert fn.return_third_element(self.two_number_elements) == "Error: IndexOutOfBound"
        assert fn.return_third_element(self.two_string_elements) == "Error: IndexOutOfBound"
        assert fn.return_third_element(self.three_string_elements) == 'Uncle Osy'
        assert fn.return_third_element(self.empty_list) == "Error: IndexOutOfBound"
        assert fn.return_third_element(self.seven_list_of_fruits) == 'Pineapple'


if __name__ == '__main__':
    unittest.main()
