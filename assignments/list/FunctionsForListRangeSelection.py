# Task 1
# Sort the list of elements into its natural order and return sorted list
# If I pass a list of character elements ['z', 'f', 'r'] then I want the function to return ['f', 'r', 'z']
# If I pass a list of number elements [2,1,8] then I want the function to return [1,2,8]
# See https://www.w3schools.com/python/ref_list_sort.asp for for how to use the sort method

# Task 2 and Task 3
# These tasks deal on range of indexes.
# You first have to sort the elements by calling the method sort_list and then use the range
# notation [2:5] (you can use negative range notation too [:-1])


class FunctionForListRangeSelection:

    # Task 1
    @staticmethod
    def sort_list(list_of_elements):
        list_of_elements.sort()
        return list_of_elements

    # Task 2
    @staticmethod
    def get_list_of_first_three_sorted_elements(list_of_elements):
        list_of_elements.sort()
        return list_of_elements[:3]

    # Task 3
    @staticmethod
    def get_list_of_last_two_sorted_elements(list_of_elements):
        list_of_elements.sort()
        return list_of_elements[-2:]
