import json
import sys

low_priority_symbols_list = [
    "bad-indentation",
    "trailing-whitespace",
    "wrong-import-position",
    "bad-whitespace",
    "ungrouped-imports",
    "trailing-newlines",
    "reimported",
]


class Reprioritise:
    @staticmethod
    def exec(input_location):

        json_array: list = None
        with open(input_location) as json_file:
            json_array = json.load(json_file)

            found_positions = []

            # Print the type of json_array variable
            print("Type:", type(json_array))
            for position, obj in enumerate(json_array):
                if obj["symbol"] in low_priority_symbols_list:
                    found_positions.append(position)

            print("found_positions", found_positions)
            print("Original length:", len(json_array))

            for position in found_positions:
                json_array.append(json_array[position])
            print("After append operations length:", len(json_array))

            for position in found_positions:
                json_array.pop(position)
            print("After pop operations length:", len(json_array))

        with open(input_location, 'w') as outfile:
            json.dump(json_array, outfile, indent=4)
