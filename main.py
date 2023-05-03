import sys

args = sys.argv
if(len(args)!=3):
    print("#Error 01# Wrong amount of arguments. Program requires exactly two.")
else:
    primary = args[1]
    secondary = args[2]
    print(primary, secondary)