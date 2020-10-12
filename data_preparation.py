import pandas as pd
import subprocess

country_codes = {"IR": [], "ID": [], "IN": []}
file_list = []
for day in range(2, 9):
    call_string = "aws s3 --no-sign-request ls s3://ooni-data/autoclaved/jsonl/2020-03-0{}/".format(day)
    file_list.extend(subprocess.check_output(call_string, shell=True).decode('ascii').split("\n"))  
    
for line in file_list:
    for code, file_selection in country_codes.items():
        if "-{}-".format(code) in line:
            file_selection.append(line.split(" ")[-1])   
            
subprocess.run(["mkdir", "ooni"])
for code in country_codes.keys():
    subprocess.call("mkdir ooni/{}".format(code), shell=True)
for code, file_selection in country_codes.items():
    for filename in file_selection:
        call_string = "aws s3 --no-sign-request cp s3://ooni-data/autoclaved/jsonl/2020-03-0{}/{} ./ooni/{}/{}".format(filename[7], filename, code, filename)
        subprocess.call(, shell=True)
