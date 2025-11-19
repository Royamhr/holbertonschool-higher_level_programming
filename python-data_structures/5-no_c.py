#!/usr/bin/python3
def no_c(my_string):
    n = list(my_string)
    for i in range(len(n)):
        if n[i] == "c" or n[i] == "C":
            n[i] = ""
    return "".join(n)
