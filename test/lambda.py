#!/usr/bin/env python

import functools
import time
# def square(x):
#     return(x * x)
square = lambda x: x * x
print(square(10))

class person(object):
    """docstring for person."""
    def __init__(self, name):
        super(person, self).__init__()
        self.name = name



# def sumRGB(r, g, b):
#     return(r + g + b)
#     pass
sumRGB = lambda r, g, b: r + g + b
print(sumRGB(3, 4, 5))


conv_list_int = lambda list: map(int, list)
names = ["1", "2", "3"]
print(names)
names = (list(conv_list_int(names)))
print(names)


evens = lambda list: filter(lambda num: num % 2 == 0, list)
print(list(evens(range(50))))


n = [1, 2, 3, 4, 5, 6]
print(list(map(lambda x: x * 2, n)))


def red(function, list):
    result = function(list[0], list[1])
    for x in list[2:]:
        result = function(result, x)
    return result


def function(x, y):
    def add(x, y):
        fx = lambda x, y: x ** y
        return(fx(x, y))
    return add(x, y)


print(red(function, range(2, 100)))
print(functools.reduce(function, n))

# c++ ***************************************
# int red(int function, int list)
# {
#     int result = function(list[0], list[1])
#     for(int x=2;x < list.size();x++)
#     {
#         result = function(result, x)
#     }
#     return (result)
# }
