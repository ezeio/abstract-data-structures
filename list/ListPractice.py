# # 1. ordered
# # 2. changeable
# # 3. Allows duplicate members
#
# # Creating a list with values and assigning it to the variable "this_list"
# # "apple" - index 0 reading from the back
# # "banana" - index 1 reading from the back
# # "cherry" - index 2 reading from the back
# list_of_fruits = ["apple", "banana", "cherry"]
# print(list_of_fruits)
#
# this_list_of_numbers = [1, 2, 3, 4, 5]
# print(this_list_of_numbers)
#
# # Access Items
# # print the third item in the list of fruits
# # The index of a list starts with 0
# print("The third item of the list is:  " + list_of_fruits[2])
#
# # Negative Indexing
# # "apple" - index -1 reading from the back
# # "banana" - index -2 reading from the back
# # "cherry" - index -3 reading from the back
# print("The last item in the list is: " + list_of_fruits[-1])
# print("The second item in the list starting from the back: " + list_of_fruits[-2])
# print("The third item in the list starting from the back: " + list_of_fruits[-3])
#
# # Range of Indexes
#
# print(f"first and second fruits in the list are: {list_of_fruits[0:2]}")
# # Note: The search will start at index 0 (included) and end at index 3 (not included).
#
#
#
# def print_the_last_element(list_of_elements):
#     length_of_list = len(list_of_elements)
#     print(f" Last element in the list! {list_of_elements[length_of_list - 1]}")
#
#
# list_of_random_people = ["baba", "luka", "smith", "fela"]
#
# print_the_last_element(list_of_random_people)
# print_the_last_element([1, 2, 3, 4, 5, 6, 7])
# print_the_last_element([1])

eze_family_members = ['Sue', 'Ngo', 'Chris', 'Emmy', 'Ify', 'Chi', 'Osy']
ezeonu = ['JoJo', 'Emma']
no_child_yet = []


def return_last_born(list_of_family_members):
    total_number_of_members = len(list_of_family_members)
    if total_number_of_members > 0:
        return list_of_family_members[total_number_of_members - 1]
    else:
        return "There are no members in the family"


def return_1():
    return 3


assert return_1() == 1
