#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new1 = []
    for i in my_list:
        if i == search:
            new1 += [replace]
        else:
            new1 += [i]
    return new1
