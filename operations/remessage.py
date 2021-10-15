import json

overriden_symbols = {
    "too-many-arguments": "Too many arguments, consider moving hyperparameters to a config file."
}

class Remessage:
    @staticmethod
    def exec(input_location):

        json_array: list = None
        with open(input_location) as json_file:
            json_array = json.load(json_file)
            for obj in json_array:
                if obj["symbol"] in overriden_symbols:
                    obj["message"] = overriden_symbols["symbol"]

        with open(input_location, 'w') as outfile:
            json.dump(json_array, outfile, indent=4)
