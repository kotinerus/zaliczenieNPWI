import json


def readFile(file):
    openedFile = open(file, 'r')
    return openedFile.read()


def isJson(JSON):
    try:
        json.loads(JSON)
    except ValueError as e:
        return False
    return True


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
            print("It works!")


        else:
            print("[Error 02] This file is not JSON file.")


    case _:
        print("[Error 01] Wrong extension. Program accept only .json")

input("PRESS [ENTER TO LEAVE]")
