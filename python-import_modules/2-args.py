#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    argc = len(args)

    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc))

    for i in range(argc):
        print("{}: {}".format(i + 1, args[i]))
