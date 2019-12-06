#!/usr/bin/env python

import sys
from intcomputer import Intcomputer


def read_input_to_list(path):
    with open(path) as file:
        return [int(x) for x in file.readline().split(",")]

if __name__ == "__main__":
    puzzle = sys.argv[1]
    input = read_input_to_list(sys.argv[2])
    if puzzle == "1":
        intcomputer = Intcomputer(input)
        get_input = lambda : 1
        intcomputer.run(input=get_input)
    elif puzzle == "2":
        intcomputer = Intcomputer(input)
        get_input = lambda : 5
        intcomputer.run(input=get_input)

    else:
        print("Input argument 1 needs to be 1 or 2", file=sys.stderr)
        exit(1)
