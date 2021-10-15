import json
import sys

# 1. Read file
# 2. Parse json
# 3. Read nested ranking configuration
#


if __name__ == "__main__":
    parsed = []
    file_name = sys.argv[1]
    print("file_name", file_name)
    with open(file_name) as json_file:
        data = json.loads(json_file)

        # Print the type of data variable
        print("Type:", type(data))
