# Author: Matthew Armstrong
# Date: 10/10/2021
# Description: write a Box class
# whose init method takes three parameters
# and uses them to initialize the private length, width and height data members of a Box.

class Box:
    """represents the box class"""
    def __init__(self, length, width, height):
        """initializes length, width, height"""
        self._length = length
        self._width = width
        self._height = height

    def get_length(self):
        """returns the length"""
        return self._length

    def get_width(self):
        """returns the width"""
        return self._width

    def get_height(self):
        """returns the height"""
        return self._height

    def volume(self):
        """returns the volume of the box"""
        volume = self._length * self._width * self._height
        return volume


def box_sort(boxes):
    """function that uses insertion sort
    to sort a list of Boxes
    from greatest volume to least volume."""
    for index in range(1, len(boxes)):
        box = boxes[index]
        pos = index - 1
        while pos >= 0 and box.volume() > boxes[pos].volume():
            boxes[pos + 1] = boxes[pos]
            pos -= 1
        boxes[pos + 1] = box


# b1 = Box(3.4, 19.8, 2.1)
# b2 = Box(1.0, 1.0, 1.0)
# b3 = Box(8.2, 8.2, 4.5)
# box_list = [b1, b2, b3]
# box_sort(box_list)
