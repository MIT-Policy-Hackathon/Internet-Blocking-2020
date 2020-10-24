import os
import json
iran_measurements = {}
for filename in os.listdir(".")[:10]:
    with open(filename, 'r') as infile:
        try:
            iran_measurements[filename] = json.load(infile)
        except Exception as e:
            print(line, e)
