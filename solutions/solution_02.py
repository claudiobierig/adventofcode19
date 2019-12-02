#!/usr/bin/env python

import sys

def change_list(l):
    """
    >>> change_list([1,9,10,3,2,3,11,0,99,30,40,50])
    3500
    >>> change_list([1,0,0,0,99])
    2
    >>> change_list([2,3,0,3,99])
    2
    >>> change_list([2,4,4,5,99,0])
    2
    >>> change_list([1,1,1,4,99,5,6,0,99])
    30
    """
    index = 0
    while index < len(l):
        operation = l[index]
        if operation == 99:
            break
        first = l[index + 1]
        second = l[index + 2]
        third = l[index + 3]
        if operation == 1:
            l[third] = l[first] + l[second]
        elif operation == 2:
            l[third] = l[first] * l[second]
        else:
            return -1
        index += 4
    return l[0]


def read_input_to_list(path):
    with open(path) as file:
        return [int(x) for x in file.readline().split(",")]

if __name__ == "__main__":
    puzzle = sys.argv[1]
    input = read_input_to_list(sys.argv[2])
    if puzzle == "1":
        input[1] = 12
        input[2] = 2
        print(change_list(input))
    elif puzzle == "2":
        for i in range(100):
            for j in range(100):
                current_input = input.copy()
                current_input[1] = i
                current_input[2] = j
                result = change_list(current_input)
                if result == -1:
                    print(f"Input {i}, {j} invalid", file=sys.stderr)
                if result == 19690720:
                    print(100*i + j)

    else:
        print("Input argument 1 needs to be 1 or 2", file=sys.stderr)
        exit(1)
