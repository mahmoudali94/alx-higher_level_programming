#!/usr/bin/python3

#print list fun

def print_list_integer(my_list=[]):
    if my_list:
        for item in reversed(my_list):
            print("{:d}".format(item))
