# Author: Matthew Armstrong
# Date: 11/14/2021
# Description: Use the time module to write a decorator function named sort_timer
# that times how many seconds it takes the decorated function to run.
# Since sort functions don't need to return anything,
# have the decorator's wrapper function return that elapsed time.

import time
import random
from matplotlib import pyplot
from functools import wraps


def sort_timer(func):
    """decoding function for determining amount of seconds needed for the function to run"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        """wrapper function"""
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        elapsed_time = end - start
        return elapsed_time

    return wrapper


@sort_timer
def bubble_sort(a_list):
    """returns a list in ascending order"""
    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp


@sort_timer
def insertion_sort(a_list):
    """returns a list in ascending order"""
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value


def compare_sorts(func_1, func_2):
    """returns a plot which compares the bubble sort and insertion sort length of time"""
    size = []
    bubble_time = []
    insertion_time = []
    for list_size in range(1000, 10000 + 1, 1000):
        # print(list_size)
        list_1 = []
        size.append(list_size)
        for i in range(list_size):
            list_1.append(random.randint(1, 10000))
        list_2 = list(list_1)

        bubble_timer = func_1(list_1)
        bubble_time.append(bubble_timer)

        insertion_timer = func_2(list_2)
        insertion_time.append(insertion_timer)

    pyplot.plot(size, bubble_time, 'ro--', label="bubble sort", linewidth=2)
    pyplot.plot(size, insertion_time, 'go--', label="insertion sort", linewidth=2)
    pyplot.xlabel("The Number of Elements (X)")
    pyplot.ylabel("The Time in Seconds (Y)")
    pyplot.legend()
    pyplot.show()


compare_sorts(bubble_sort, insertion_sort)
