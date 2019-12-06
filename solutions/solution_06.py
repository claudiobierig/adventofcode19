#!/usr/bin/env python

import sys


def insert_to_dict(p, d):
    d[p[1]] = p[0]

def get_orbits(d, key):
    orbits = []
    while key in d.keys():
        orbits.append(d[key])
        key = d[key]
    return orbits

def read_input_to_list(path):
    with open(path) as file:
        return [line.strip().split(")") for line in file.readlines()]

if __name__ == "__main__":
    puzzle = sys.argv[1]
    input = read_input_to_list(sys.argv[2])
    d = {}
    for p in input:
        insert_to_dict(p, d)
    if puzzle == "1":
        solution_counter = 0
        depth_counter = 1
        while d:
            keys_to_remove = []
            for key, value in d.items():
                if value not in d.keys():
                    solution_counter +=depth_counter
                    keys_to_remove.append(key)
            for key in keys_to_remove:
                d.pop(key, None)
            depth_counter += 1
        print(solution_counter)
    elif puzzle == "2":
        you_orbits = get_orbits(d, "YOU")
        santa_orbits = get_orbits(d, "SAN")
        while you_orbits[-1] == santa_orbits[-1]:
            you_orbits = you_orbits[:-1]
            santa_orbits = santa_orbits[:-1]
        print(len(you_orbits)+len(santa_orbits))
        
    else:
        print("Input argument 1 needs to be 1 or 2", file=sys.stderr)
        exit(1)
