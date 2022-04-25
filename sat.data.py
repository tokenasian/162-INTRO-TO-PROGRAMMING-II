
# Author: Matthew Armstrong
# Date: 10/26/2021
# Description: Write a class named SatData that reads a JSON file containing data on 2010 SAT results for New York City
# and writes the data to a text file in CSV format.
import json


class SatData:
    def __init__(self):
        """initializes SatData class, reads the json file"""
        with open("sat.json", "r") as infile:
            self._sat = json.load(infile)

    def save_as_csv(self, dbns_list):
        """saves a CSV file"""
        header_list = ["DBN", "School Name", "Number of Test Takers", "Critical Reading Mean", "Mathematics Mean",
                       "Writing Mean"]
        header_string = ','.join([str(x) for x in header_list])
        with open('output.csv', 'w') as outfile:
            outfile.write(str(header_string) + '\n')

        for data in self._sat["data"]:
            for i in data:
                for dbns in dbns_list:
                    if i == dbns:
                        values = ','.join([str(f'"{data[index]}"') for index in range(data.index(dbns), len(data))])
                        with open('output.csv', 'a') as outfile:
                            outfile.write(str(values) + '\n')


# sd = SatData()
# dbns = ["02M303", "02M294", "01M450", "02M418"]
# sd.save_as_csv(dbns)
