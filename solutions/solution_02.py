#!/usr/bin/env python

import sys
import itertools
from intcomputer import Intcomputer


def read_input_to_list(path):
    with open(path) as file:
        return [int(x) for x in file.readline().split(",")]

if __name__ == "__main__":
    puzzle = sys.argv[1]
    input = read_input_to_list(sys.argv[2])
    if puzzle == "1":
        intcomputer = Intcomputer(input)
        intcomputer.set_noun_verb(12, 2)
        intcomputer.run()
        print(intcomputer.get_start())
    elif puzzle == "2":
        for noun, verb in itertools.product(range(100), range(100)):
            intcomputer = Intcomputer(input)
            intcomputer.set_noun_verb(noun, verb)
            intcomputer.run()
            result = intcomputer.get_start()
            if result == 19690720:
                print(100*noun + verb)

    else:
        print("Input argument 1 needs to be 1 or 2", file=sys.stderr)
        exit(1)
