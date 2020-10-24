import os
import json

FILE_PATH = "."

iran_measurements = {}
for filename in os.listdir(FILE_PATH)[:100]:
    with open(filename, 'r') as infile:
        lines = infile.readlines()
        if len(lines) > 1:
            # This is a web connectivity probe, make a list
            iran_measurements[filename] = [json.loads(line) for line in lines]
        elif len(lines) > 0:
            # This is another probe
            iran_measurements[filename] = json.loads(lines[0])
        else:
            print("Cannot read file {}".format(filename))
            
# Example exploration
list(iran_measurements.values())[0]['test_keys']
