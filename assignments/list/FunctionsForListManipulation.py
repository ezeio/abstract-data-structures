# Task 1
# Create a function that accepts a list of elements and returns the last element

# Task 2
# Create a function that accepts a list of elements and returns the first element

# Task 3
# Create a function that accepts a list of elements and returns the second element

# Task 4
# Create a function that accepts a list of elements and returns the third element


# Note! if the length of the list passed in is below the index expected, then print Error: IndexOutOfBound

class FunctionsForListManipulation:

    # Task 1
    @staticmethod
    def return_last_element(list_of_elements):
        pass

    # Task 2
    @staticmethod
    def return_first_element(list_of_elements):
        pass

    # Task 3
    @staticmethod
    def return_second_element(list_of_elements):
        size_of_list = len(list_of_elements)
        if size_of_list < 2:
            return "Error: IndexOutOfBound"
        else:
            return list_of_elements[1]


    # Task 4
    @staticmethod
    def return_third_element(list_of_elements):
        size_of_list = len(list_of_elements)
        if size_of_list < 3:
            return "Error: IndexOutOfBound"
        else:
            return list_of_elements[2]

