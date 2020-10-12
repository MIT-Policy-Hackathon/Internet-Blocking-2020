import os 
import json

iran_measurements = {}
for filename in os.listdir("./ooni/IR"):
    with open(filename, 'w') as infile:
        iran_measurements[filename] = json.load("filename")
