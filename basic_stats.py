# Author: Matthew Armstrong
# Date: 09/22/2021
# Description: learning how to use the import module.
import statistics


class Student:
    """init method to initial private fields for name and grade"""
    def __init__(self, name, grade):
        """setting the name and grade"""
        self._name = name
        self._grade = grade

    def get_grade(self):
        """returning the grade"""
        return self._grade


def basic_stats(student_list):
    """function returns a tuple containing mean, median, and mode of all grades"""
    grade = [student._grade for student in student_list]

    mean = statistics.mean(grade)
    median = statistics.median(grade)
    mode = statistics.mode(grade)
    my_tuple = (mean, median, mode)

    return my_tuple
