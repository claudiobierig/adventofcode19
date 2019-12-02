#!/usr/bin/env python

import sys
import itertools

class Intcomputer:
    """
    >>> intcomputer = Intcomputer([1,9,10,3,2,3,11,0,99,30,40,50])
    >>> intcomputer.run()
    3500
    >>> intcomputer._memory
    [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
    >>> intcomputer = Intcomputer([1,0,0,0,99])
    >>> intcomputer.run()
    2
    >>> intcomputer._memory
    [2, 0, 0, 0, 99]
    >>> intcomputer = Intcomputer([2,3,0,3,99])
    >>> intcomputer.run()
    2
    >>> intcomputer._memory
    [2, 3, 0, 6, 99]
    >>> intcomputer = Intcomputer([2,4,4,5,99,0])
    >>> intcomputer.run()
    2
    >>> intcomputer._memory
    [2, 4, 4, 5, 99, 9801]
    >>> intcomputer = Intcomputer([1,1,1,4,99,5,6,0,99])
    >>> intcomputer.run()
    30
    >>> intcomputer._memory
    [30, 1, 1, 4, 2, 5, 6, 0, 99]
    >>> input = read_input_to_list("input/02.txt")
    >>> intcomputer = Intcomputer(input)
    >>> intcomputer.set_noun_verb(12, 2)
    >>> intcomputer._memory[1]
    12
    >>> intcomputer._memory[2]
    2
    >>> intcomputer.run()
    5866714
    >>> intcomputer = Intcomputer(input)
    >>> intcomputer.set_noun_verb(52, 8)
    >>> intcomputer.run()
    19690720
    """

    def __init__(self, memory):
        self._memory = memory.copy()
    
    def set_noun_verb(self, noun, verb):
        self._memory[1] = noun
        self._memory[2] = verb
    
    def run(self):
        index = 0
        while index < len(self._memory):
            operation = self._memory[index]
            if operation == 99:
                break
            first = self._memory[index + 1]
            second = self._memory[index + 2]
            third = self._memory[index + 3]
            if operation == 1:
                self._memory[third] = self._memory[first] + self._memory[second]
            elif operation == 2:
                self._memory[third] = self._memory[first] * self._memory[second]
            else:
                return -1
            index += 4
        return self._memory[0]


def read_input_to_list(path):
    with open(path) as file:
        return [int(x) for x in file.readline().split(",")]

if __name__ == "__main__":
    puzzle = sys.argv[1]
    input = read_input_to_list(sys.argv[2])
    if puzzle == "1":
        intcomputer = Intcomputer(input)
        intcomputer.set_noun_verb(12, 2)
        print(intcomputer.run())
    elif puzzle == "2":
        for noun, verb in itertools.product(range(100), range(100)):
            intcomputer = Intcomputer(input)
            intcomputer.set_noun_verb(noun, verb)
            result = intcomputer.run()
            if result == -1:
                print(f"Input {noun}, {verb} invalid", file=sys.stderr)
            if result == 19690720:
                print(100*noun + verb)

    else:
        print("Input argument 1 needs to be 1 or 2", file=sys.stderr)
        exit(1)
