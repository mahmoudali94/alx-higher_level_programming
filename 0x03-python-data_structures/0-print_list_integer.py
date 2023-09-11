#!/usr/bin/python3

#print list fun

def print_list_integer(my_list=[]):
    if my_list:
        for i in len(my_list):
            print("{:d}".format(my_list[i]))
