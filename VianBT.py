import subprocess
import json
import datetime

list_of_data = []
dict = {}

def getBashOutput(command):
    output = subprocess.check_output(command, shell = True)
    output = str(output).split('\\n')
    return output

def getName_and_MAC():
    output = getBashOutput("hcitool scan")
    for i in range(1, len(output) - 1):
        name_add_list = output[i].split('\\t')
        dict = {"name" : name_add_list[2], "mac" : name_add_list[1]}
        list_of_data.append(dict)

def getDevice_class():
    output = getBashOutput("hcitool inq")
    for i in range(1, len(output) - 1):
        dev_class_list = output[i].split('\\t')
        for j in list_of_data:
            if dev_class_list[1] in j.values():
                list_of_data[list_of_data.index(j)]["deviceClass"] = dev_class_list[3].split(' ')[1]

def getBT_VerAndTime():
    for device in list_of_data:
        mac = device["mac"]
        output = getBashOutput("sudo hcitool info " + mac)
        for string in output:
            if string.find("LMP") != -1:
                output = string.split('\\t')[1]
        device["communicationStandard"] = output
        device["timestamp"] = datetime.datetime.now().replace(microsecond=0).isoformat()


def getRSSI():
    output = getBashOutput("sudo btmgmt find")
    for string in output:
        if string.find("rssi") != -1:
            str_list = string.split(" ")
            for device in list_of_data:
                if str_list[2] in device.values():
                    device["level"] = abs(int(str_list[6]))

def getServiceClasses():
    for device in list_of_data:
        mac = device["mac"]
        device["serviceType"] = []
        output = getBashOutput("sdptool browse " + mac)
        for string in output:
            if string.find("Service Name") != -1:
                service = string.split(":")[1]
                device["serviceType"].append(service)
                    
getName_and_MAC()
getDevice_class()
getBT_VerAndTime()
getRSSI()
getServiceClasses()
for i in list_of_data:
    print(i)

with open("data_file.json", "w") as write_file:
    json.dump(list_of_data, write_file)
