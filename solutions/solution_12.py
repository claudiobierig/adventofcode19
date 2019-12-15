#!/usr/bin/env python

import sys
import itertools
import re
import math
import copy

def read_input(path):
    with open(path) as file:
        return [[[int(x) for x in re.findall(r'[-]?\d+', line)],[0,0,0]] for line in file.readlines()]

def adapt_valocity(moon1, moon2):
    """
    """
    for i in range(3):
        if moon1[0][i] > moon2[0][i]:
            moon1[1][i] -= 1
            moon2[1][i] += 1
        elif moon1[0][i] < moon2[0][i]:
            moon1[1][i] += 1
            moon2[1][i] -= 1

def adapt_position(moon):
    """
    >>> moon = [[1,2,3],[-1,2,7]]
    >>> adapt_position(moon)
    >>> moon
    [[0, 4, 10], [-1, 2, 7]]
    """
    for i in range(3):
        moon[0][i] += moon[1][i]

def compute_energy(moon):
    """
    >>> compute_energy([[8,-12,-9], [-7,3,0]])
    290
    >>> compute_energy([[13,16,-3],[3,11,5]])
    608
    """
    kin_energy = 0
    pot_energy = 0
    for i in range(3):
        kin_energy += abs(moon[1][i])
        pot_energy += abs(moon[0][i])

    return kin_energy*pot_energy

def step(input):
    for moon1, moon2 in itertools.combinations(input, r=2):
        adapt_valocity(moon1, moon2)
    for moon in input:
        adapt_position(moon)

def the_same(one, two, i):
    """
    >>> input = [[[-1,0,2],[0,0,0]],[[2,-10,-7],[0,0,0]],[[4,-8,8],[0,0,0]],[[3,5,-1],[0,0,0]]]
    >>> the_same(input, input, 0)
    True
    >>> the_same(input, input, 1)
    True
    >>> the_same(input, input, 2)
    True
    """
    return all([moon1[0][i] == moon2[0][i] and moon1[1][i] == moon2[1][i] for (moon1, moon2) in zip(one, two)])

def repeats(input):
    """
    >>> input = [[[-1,0,2],[0,0,0]],[[2,-10,-7],[0,0,0]],[[4,-8,8],[0,0,0]],[[3,5,-1],[0,0,0]]]
    >>> repeats(input)
    2772
    """
    start = copy.deepcopy(input)
    result = []
    for i in range(3):
        current = copy.deepcopy(input)
        n = 1
        step(current)    
        while not the_same(current, start, i):
            step(current)
            n += 1
        result.append(n)

    gcd1 = math.gcd(result[0], result[1])
    lcm1 = int(result[0]*result[1]/gcd1)
    gcd2 = math.gcd(lcm1, result[2])
    lcm2 = int(lcm1*result[2]/gcd2)
    
    return lcm2


if __name__ == "__main__":
    input = read_input("input/12.txt")
    for _ in range(1000):
        step(input)

    total_energy = 0
    for moon in input:
        total_energy += compute_energy(moon)
    
    print(total_energy)
    
    input = read_input("input/12.txt")
    print(repeats(input))
    
    