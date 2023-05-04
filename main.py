import json
import yaml


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
    except ValueError as e:
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
                case _: print("[Error 03] Wrong extension. Program accept only .json, .yml")
        else:
            print("[Error 02] This file is not JSON file.")
    case 'yaml' | 'yml':
        if isYaml(readFile(firstArgument)):
            match secondArg.lower():
                case 'json': ymlToJSON(firstArgument,secondArgument)
                case 'yaml' | 'yml' : justCopy(readFile(firstArgument),secondArgument)
                case _: print("[Error 03] Wrong extension. Program accept only .json, .yml")

    case _:
        print("[Error 01] Wrong extension. Program accept only .json, .yml")

input("PRESS [ENTER TO LEAVE]")
