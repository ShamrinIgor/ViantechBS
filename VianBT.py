import subprocess
import json

list_of_data = []
output = subprocess.check_output("hcitool scan", shell = True )
output = str(output)
output = output.split('\\n')
for i in range(1, len(output) - 1):
    name_add_list = output[i].split('\\t')
    dict = {"Name" : name_add_list[2], "MAC-address" : name_add_list[1]}
    list_of_data.append(dict)

for i in list_of_data:
    print(i)

with open("data_file.json", "w") as write_file:
    json.dump(list_of_data, write_file)
