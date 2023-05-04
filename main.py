import json
import xml.parsers.expat
import xml.etree.ElementTree as ET
import yaml
from xml.dom import minidom
import xmltodict


def readFile(file):
    openedFile = open(file, 'r')
    return openedFile.read()


def isJson(JSON):
    try:
        json.loads(JSON)
    except ValueError as e:
        return False
    return True

def isYaml(YAML):
    try:
        yaml.safe_load(YAML)
    except Exception as e:
        return False
    return True

def isXML(XML):
    try:
        minidom.parse(XML)
    except xml.parsers.expat.ExpatError as e:
        return False
    return True

def justCopy(firstFile,newFile ):
    file = open(newFile,'a')
    file.write(firstFile)
    file.close()

def ymlToJSON(firstFile,secondFile):
    with open(firstFile, 'r') as file:
        yamlFile = yaml.safe_load(file)

    with open(secondFile, 'w') as fileTwo:
        json.dump(yamlFile,fileTwo)

def JSONtoyml(firstFile,secondFile):
    with open(firstFile, 'r') as file:
        JSONFile = json.load(file)

    with open(secondFile,'w') as file:
        yaml.dump(JSONFile, file)



firstArgument = input("Insert first file: ")
secondArgument = input("Insert second file: ")

# Extension of the first file
dot = firstArgument.rfind('.')
firstArg = firstArgument[dot + 1:]

# Extension of the second file
dot = secondArgument.rfind('.')
secondArg = secondArgument[dot + 1:]

match firstArg.lower():
    case 'json':
        if isJson(readFile(firstArgument)):
            match secondArg.lower():
                case 'json': justCopy(readFile(firstArgument),secondArgument)
                case 'yaml' | 'yml' : JSONtoyml(firstArgument,secondArgument)
                case 'xml':
                    with open(firstArgument,'r') as jsonFile:
                        data_dict = json.load(jsonFile)
                        xml_string = xmltodict.unparse(data_dict)
                        with open(secondArgument,'w') as xmlFile:
                            xmlFile.write(xml_string)
                case _: print("[Error 03] Wrong extension. Program accept only .json, .yml, .xml")
        else:
            print("[Error 02] This file is not JSON file.")
    case 'yaml' | 'yml':
        if isYaml(readFile(firstArgument)):
            match secondArg.lower():
                case 'json': ymlToJSON(firstArgument,secondArgument)
                case 'yaml' | 'yml' : justCopy(readFile(firstArgument),secondArgument)
                case 'xml':
                    with open(firstArgument, 'r') as yamlFile:
                        data = yamlFile.read()
                        data_dict = yaml.load(data, Loader=yaml.FullLoader)
                        xml_string = xmltodict.unparse(data_dict)
                        with open(secondArgument, 'w') as xmlFile:
                            xmlFile.write(xml_string)
                case _: print("[Error 03] Wrong extension. Program accept only .json, .yml, .xml")
        else:
            print("[Error 04] This file is not yaml file.")
    case 'xml':
        if isXML(firstArgument):
            match secondArg.lower():
                case 'json':
                    with open(firstArgument) as xml:
                        data_dict = xmltodict.parse(xml.read())
                        json_data = json.dumps(data_dict)
                        with open(secondArgument, "w") as json_file:
                            json_file.write(json_data)

                case 'yaml' | 'yml':
                    with open(firstArgument) as xml:
                        data_dict = xmltodict.parse(xml.read())
                        yaml_data = yaml.dump(data_dict)
                        with open(secondArgument, "w") as yaml_file:
                            yaml_file.write(yaml_data)
                case 'xml' :
                    tree = ET.parse(firstArgument)
                    root = tree.getroot()
                    newTree = ET.ElementTree(root)
                    newTree.write(secondArgument)
                case _: print("[Error 03] Wrong extension. Program accept only .json, .yml, .xml")
        else:
            print("[Error 05] This file is not xml file.")
    case _:
        print("[Error 01] Wrong extension. Program accept only .json, .yml, .xml")

input("PRESS [ENTER TO LEAVE]")
