# Author: Matthew Armstrong
# Date: 10/26/2021
# Description: Write a class named NeighborhoodPets
# that has methods for adding a pet, deleting a pet, searching for the owner of a pet,
# saving data to a JSON file, loading data from a JSON file,
# and getting a set of all pet species.

import json


class NeighborhoodPets:
    def __init__(self):
        """initializes class"""
        self._pets = {}

    def add_pet(self, pet_name, pet_species, pet_owner):
        """adds pet values"""
        if pet_name not in self._pets:
            self._pets[pet_name] = {"species": pet_species, "owner": pet_owner}

    def delete_pet(self, pet_name):
        """deletes pet"""
        if pet_name in self._pets:
            del self._pets[pet_name]

    def get_owner(self, pet_name):
        """gets owner"""
        if pet_name in self._pets:
            return self._pets[pet_name]["owner"]

    def save_as_json(self, json_file):
        """saves as json"""
        with open(json_file, 'w') as outfile:
            json.dump(self._pets, outfile)

    def read_json(self, json_file):
        """reads json file"""
        with open(json_file, 'r') as infile:
            self._pets = json.load(infile)

    def get_all_species(self):
        """gets all species"""
        pet_species = set()
        for pet_name in self._pets.values():
            pet_species.add(pet_name["species"])
        return pet_species


# np = NeighborhoodPets()
# np.add_pet("Fluffy", "gila monster", "Oksana")
# np.add_pet("Morgana", "cat", "Joker")
# np.add_pet("Morgana", "cat", "Joker")
# np.add_pet("Tiny", "stegasaurus", "Rachel")
# np.add_pet("Spot", "zebra", "Farrokh")
# np.save_as_json("pets.json")
# np.delete_pet("Fluffy")
# fluffy_owner = np.get_owner("Fluffy")
# print("fluffy owner:", fluffy_owner)
# np.read_json("other_pets.json")  # where other_pets.json is a file it saved in some previous session
# species_set = np.get_all_species()
# print("species_set:", species_set)
