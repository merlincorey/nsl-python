'''Simple circle maths module in terms of tau where simplest'''

from math import pi


def double(x):
    '''Return twice the value given.'''
    return x * 2

tau = double(pi)


def square(x):
    '''Return the square of the value given.'''
    return x * x


def diameter(radius):
    '''Return the diameter of a circle given the radius.'''
    return double(radius)


def circumfrence(radius):
    '''Return the circumfrence of a circle given the radius.'''
    return tau * radius


def area(radius):
    '''Return the area of a circle given the radius.'''
    return pi * square(radius)
