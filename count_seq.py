
# Author: Matthew Armstrong
# Date: 11/14/2021
# Description: generator function named count_seq that doesn't take any parameters
# and generates a sequence that starts like this:
# 2, 12, 1112, 3112, 132112, 1113122112, 311311222112, 13211321322112, ...

def count_seq():
    """function which starts with '2' and has no parameters"""
    seq = '2'  # starting the sequence
    while True:
        yield seq
        seq = next_seq(seq)


def next_seq(seq):
    """helper function for the count seq method"""
    result = ""
    index = seq[0]
    count = 1

    for val in range(1, len(seq)):
        if seq[val] == index:
            count += 1
        else:
            result += str(count) + index
            index = seq[val]
            count = 1

    result += str(count) + index

    return result
