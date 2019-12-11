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
        output = []
        intcomputer = Intcomputer(input)
        intcomputer.run(input=[1], output=output)
        print(output)
    elif puzzle == "2":
        output = []
        intcomputer = Intcomputer(input)
        intcomputer.run(input=[2], output=output)
        print(output)
    else:
        print("Input argument 1 needs to be 1 or 2", file=sys.stderr)
        exit(1)
