# Author: Matthew Armstrong
# Date: 10/28/2021
# Description: Write a recursive function named is_subsequence that takes two string parameters
# and returns True if the first string is a subsequence of the second string, but returns False otherwise.

def is_subsequence(string_a, string_b):
    """function which tests if the first string is a subsequence of the second string,
    returns true if it is, but returns false otherwise"""
    if len(string_a) == 0:
        return True
    if len(string_b) == 0:
        return False
    if string_a[0] == string_b[0]:
        return is_subsequence(string_a[1:], string_b[1:])
    elif string_a[0] != string_b[0]:
        return is_subsequence(string_a[0], string_b[+1:])
    else:
        return False


# string_a = "goodbye"
# string_b = "hello world"
# print(is_subsequence(string_a, string_b))
