# Author: Matthew Armstrong
# Date: 10/10/2021
# Description: Modify insertion sort to sorts a list of strings instead of numbers.
# It shouldn't return anything.
# The sorting should ignore case.

def string_sort(string_list):
    for index in range(1, len(string_list)):
        value = string_list[index]
        pos = index - 1
        while pos >= 0 and string_list[pos].lower() > value.lower():
            string_list[pos + 1] = string_list[pos]
            pos -= 1
        string_list[pos + 1] = value


# sort_list = ["Zebra", "apple", "maRker", "marble"]
# string_sort(sort_list)
# print(sort_list)
