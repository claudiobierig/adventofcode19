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
    >>> get_fuel_for_mass(2)
    0
    >>> get_fuel_for_mass(5)
    0
    """
    return max(int(mass/3) - 2, 0)

def get_fuel_for_mass_and_fuel(mass):
    """
    Fuel itself requires fuel just like a module -
    take its mass, divide by three, round down, and subtract 2.
    However, that fuel also requires fuel, and that fuel requires fuel, and so on.
    Any mass that would require negative fuel should instead be treated as if it requires zero fuel;
    the remaining mass, if any, is instead handled by wishing really hard, which has no mass and
    is outside the scope of this calculation.

    >>> get_fuel_for_mass_and_fuel(12)
    2
    >>> get_fuel_for_mass_and_fuel(14)
    2
    >>> get_fuel_for_mass_and_fuel(1969)
    966
    >>> get_fuel_for_mass_and_fuel(100756)
    50346
    """
    fuel = 0
    while mass > 0:
        new_fuel = get_fuel_for_mass(mass)
        fuel += new_fuel
        mass = new_fuel
    
    return fuel

def read_input_to_list(path):
    """
    read inputfile from path and return list of ints
    """
    with open(path) as file:
        return [int(x) for x in file.readlines()]

if __name__ == "__main__":
    puzzle = sys.argv[1]
    input = read_input_to_list(sys.argv[2])
    if puzzle == "1":
        print(sum([get_fuel_for_mass(x) for x in input]))
    elif puzzle == "2":
        print(sum([get_fuel_for_mass_and_fuel(x) for x in input]))
    else:
        print("Input argument 1 needs to be 1 or 2", file=sys.stderr)
        exit(1)

