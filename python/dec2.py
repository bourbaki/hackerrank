#!/usr/bin/env python
import operator

def print_array_with_format(format):
    def f(array):
        for x in array:
            print(format(x))
    return f

@print_array_with_format
def pretty_name_print(person):
    prefix = "Mr." if person[3] == "M" else "Ms."
    return "{} {} {}".format(prefix, person[0], person[1])

if __name__ == '__main__':
    n = int(input())
    persons = (tuple(input().strip().split()) for _ in range(n))
    pretty_name_print(sorted(persons, key=lambda p: p[2]))
    