#!/usr/bin/env python

import sys

def get_fuel_for_mass(mass):
    """
    Fuel required to launch a given module is based on its mass.
    Specifically, to find the fuel required for a module, take its mass,
    divide by three, round down, and subtract 2.

    >>> get_fuel_for_mass(12)
    2
    >>> get_fuel_for_mass(14)
    2
    >>> get_fuel_for_mass(1969)
    654
    >>> get_fuel_for_mass(100756)
    33583
    """
    return int(mass/3) - 2

def read_input_to_list(path):
    """
    read inputfile from path and return list of ints
    """
    with open(path) as file:
        return [int(x) for x in file.readlines()]

if __name__ == "__main__":
    input = read_input_to_list(sys.argv[1])
    print(sum([get_fuel_for_mass(x) for x in input]))
