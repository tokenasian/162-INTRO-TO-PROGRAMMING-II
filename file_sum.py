# Author: Matthew Armstrong
# Date: 10/26/2021
# Description: Write a function named file_sum
# that takes as a parameter the name of a text file that contains a list of numbers.

def file_sum(num_list):
    """function that sums the values in the file
    and write the sum to a text file name sum.txt."""
    total_value = 0
    try:
        with open(num_list, 'r')as infile:
            for number in infile:
                total_value += float(number.strip())
    except FileNotFoundError:
        print("file not found")
    finally:
        with open('sum.txt', 'w') as outfile:
            outfile.write(str(total_value))
