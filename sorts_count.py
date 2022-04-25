
# Author: Matthew Armstrong
# Date: 10/09/2021
# Description: write a bubble sort
# that counts the number of comparisons
# and the number of exchanges made while sorting a list
# and returns a tuple of the two values (comparisons first, exchanges second).
# do the same for insertion sort.

def bubble_count(a_list):
    """returns bubble count as a tuple"""
    comparisons = 0  # sets comparisons
    exchanges = 0  # sets exchanges

    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            comparisons += 1
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp
                exchanges += 1
    return comparisons, exchanges


def insertion_count(a_list):
    """returns insertion count as a tuple"""
    comparisons = 0  # sets comparisons
    exchanges = 0  # sets exchanges

    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0:
            comparisons += 1
            if a_list[pos] > value:
                exchanges += 1
                a_list[pos + 1] = a_list[pos]
                pos -= 1
            else:
                break
        a_list[pos + 1] = value
    return comparisons, exchanges
