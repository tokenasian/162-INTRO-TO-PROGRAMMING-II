# Author: Matthew Armstrong
# Date: 10/10/2021
# Description: raises a TargetNotFound exception when the target value is not in the list.

class TargetNotFound(Exception):
    """error that checks for when the target value is not in the list"""
    pass


def bin_except(a_list, target):
    """
    Searches a_list for an occurrence of target
    If found, returns the index of its position in the list
    If not found, raises a TargetNotFound exception
    """
    first = 0
    last = len(a_list) - 1
    while first <= last:
        middle = (first + last) // 2
        if a_list[middle] == target:
            return middle
        if a_list[middle] > target:
            last = middle - 1
        else:
            first = middle + 1
    raise TargetNotFound
