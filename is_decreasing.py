# Author: Matthew Armstrong
# Date: 10/28/2021
# Description: Write a recursive function named is_decreasing
# that takes as its parameter a list of numbers.
# It should return True if the elements of the list are strictly decreasing
# (each element in the array is strictly less than the previous one),
# but return False otherwise.
# You can assume the array contains at least two elements.

def is_decreasing(num_list, pos=0):
    """function that returns true if elements in the list are decreasing, bu returns false otherwise"""
    if pos == len(num_list)-1:
        return True
    if num_list[pos] > num_list[pos+1]:
        return is_decreasing(num_list, pos+1)
    else:
        return False


# testing_list = ([12, 10, 8, 6, 4, 2])
# print(is_decreasing(testing_list))
# true
# testing_list = ([2, 4, 8, 10, 12])
# print(is_decreasing(testing_list))
# false
# testing_list = ([12, 2])
# print(is_decreasing(testing_list))
# true
# testing_list = ([7, 7, 7, 7, 7, 6])
# print(is_decreasing(testing_list))
# false
# testing_list = ([10, 9.5, 5, 3.5, 1])
# print(is_decreasing(testing_list))
# true
# testing_list = ([12, 10, 8, 6, 12, 2])
# print(is_decreasing(testing_list))
# false
