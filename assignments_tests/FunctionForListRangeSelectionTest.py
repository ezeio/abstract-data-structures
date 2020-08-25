import unittest

from assignments.list.FunctionsForListRangeSelection import FunctionForListRangeSelection as fn


class FunctionForListRangeSelectionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.two_random_numbers = [69, 3]
        self.three_random_numbers = [6, 3, 4]
        self.five_random_characters = ['a', 'z', 'g', 'e', 'q']
        self.eight_random_characters = ['c', 'a', 'r', 'p', 'f', 'b', 'y', 'm']

    def test_should_return_sorted_element(self):
        assert fn.sort_list(self.two_random_numbers) == [3, 69]
        assert fn.sort_list(self.three_random_numbers) == [3, 4, 6]
        assert fn.sort_list(self.five_random_characters) == ['a', 'e', 'g', 'q', 'z']
        assert fn.sort_list(self.eight_random_characters) == ['a', 'b', 'c', 'f', 'm', 'p', 'r', 'y']

    def test_should_return_list_of_first_three_elements_in_a_sorted_list(self):
        assert fn.get_list_of_first_three_sorted_elements(self.two_random_numbers) == [3, 69]
        assert fn.get_list_of_first_three_sorted_elements(self.three_random_numbers) == [3, 4, 6]
        assert fn.get_list_of_first_three_sorted_elements(self.five_random_characters) == ['a', 'e', 'g']
        assert fn.get_list_of_first_three_sorted_elements(self.eight_random_characters) == ['a', 'b', 'c']

    def test_should_return_list_of_last_two_elements_in_a_sorted_list(self):
        assert fn.get_list_of_last_two_sorted_elements(self.two_random_numbers) == [3, 69]
        assert fn.get_list_of_last_two_sorted_elements(self.three_random_numbers) == [4, 6]
        assert fn.get_list_of_last_two_sorted_elements(self.five_random_characters) == ['q', 'z']
        assert fn.get_list_of_last_two_sorted_elements(self.eight_random_characters) == ['r', 'y']
