#!/usr/bin/env python

import sys

def does_not_decrease(s):
    """
    >>> does_not_decrease('1234')
    True
    >>> does_not_decrease('111123')
    True
    >>> does_not_decrease('135679')
    True
    >>> does_not_decrease('223450')
    False
    >>> does_not_decrease('111111')
    True
    >>> does_not_decrease('123789')
    True
    """
    l = [int(c) for c in s]
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True

def has_a_double(s):
    """
    >>> has_a_double('1234')
    False
    >>> has_a_double('111123')
    True
    >>> has_a_double('135679')
    False
    >>> has_a_double('223450')
    True
    >>> has_a_double('111111')
    True
    >>> has_a_double('123789')
    False
    """
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False

def has_a_double_not_in_larger_group(s):
    """
    >>> has_a_double_not_in_larger_group('1234')
    False
    >>> has_a_double_not_in_larger_group('111123')
    False
    >>> has_a_double_not_in_larger_group('135679')
    False
    >>> has_a_double_not_in_larger_group('223450')
    True
    >>> has_a_double_not_in_larger_group('111111')
    False
    >>> has_a_double_not_in_larger_group('123789')
    False
    >>> has_a_double_not_in_larger_group('112233')
    True
    >>> has_a_double_not_in_larger_group('123444')
    False
    >>> has_a_double_not_in_larger_group('111122')
    True
    """
    l = [int(c) for c in s]
    while len(l) > 0:
        current_l = []
        current_l.append(l.pop(0))
        while len(l) > 0:
            if l[0] == current_l[0]:
                current_l.append(l.pop(0))
            else:
                break
        if len(current_l) == 2:
            return True
    return False
           
def is_valid(x):
    """
    >>> is_valid('1233')
    False
    >>> is_valid('111123')
    True
    >>> is_valid('135679')
    False
    >>> is_valid('223450')
    False
    >>> is_valid('111111')
    True
    >>> is_valid('123789')
    False
    """
    s = str(x)
    return does_not_decrease(s) and has_a_double(s) and len(s) == 6

def is_valid_2(x):
    """
    >>> is_valid_2('1233')
    False
    >>> is_valid_2('111123')
    False
    >>> is_valid_2('135679')
    False
    >>> is_valid_2('223450')
    False
    >>> is_valid_2('223456')
    True
    >>> is_valid_2('111111')
    False
    >>> is_valid_2('123789')
    False
    >>> is_valid_2('111122')
    True
    >>> is_valid_2('123444')
    False
    >>> is_valid_2('144444')
    False
    >>> is_valid_2('444445')
    False
    """
    s = str(x)
    return does_not_decrease(s) and has_a_double_not_in_larger_group(s) and len(s) == 6

def count_valid_numbers(input_ints, puzzle):
    counter = 0
    for x in range(input_ints[0], input_ints[1]+1):
        if puzzle == "1" and is_valid(x):
            counter += 1
        elif puzzle == "2" and is_valid_2(x):
            counter += 1
    return counter

if __name__ == "__main__":
    puzzle = sys.argv[1]
    input = "248345-746315"
    input_ints = [int(x) for x in input.split("-")]
    print(count_valid_numbers(input_ints, puzzle))