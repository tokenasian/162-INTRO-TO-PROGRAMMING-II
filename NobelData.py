
# Author: Matthew Armstrong
# Date: 10/26/2021
# Description: Write a class named NobelData that reads a JSON file containing data on Nobel Prizes
# and allows the user to search that data.

import json


class NobelData:
    def __init__(self):
        """initializes class"""
        with open("nobels.json", "r") as infile:
            self._file_name = json.load(infile)

    def search_nobel(self, year, category):
        """takes year and category and returns a sorted list of winners of that year"""
        sorted_list = []
        for i in self._file_name["prizes"]:
            if i["year"] == year and i["category"] == category:
                for laureate in i["laureates"]:
                    surname = laureate["surname"]
                    sorted_list.append(surname)
        sorted_list.sort()
        return sorted_list


# def main():
    # nd = NobelData()
    # result = nd.search_nobel("2001", "economics")
    # print(result)


# if __name__ == '__main__':
    # main()
