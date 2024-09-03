import json
from lecture import Lecture


def read(FILE_PATH: str) -> dict:

    classes = {}

    with open(FILE_PATH, 'r') as file:
        json_data = json.load(file)

        # go through the keys of the json file
        for group in json_data.keys():
            # create a list of classes for each subject
            classes[group] = [
                Lecture(**lecture, group=group) for lecture in json_data[group]
            ]

    return classes
