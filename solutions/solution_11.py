#!/usr/bin/env python

import sys
from intcomputer import Intcomputer
import matplotlib.pyplot as plt

def turn(direction, output):
    if direction == 'U':
        if output == 0:
            return 'L'
        elif output == 1:
            return 'R'
    elif direction == 'D':
        if output == 0:
            return 'R'
        elif output == 1:
            return 'L'
    elif direction == 'L':
        if output == 0:
            return 'D'
        elif output == 1:
            return 'U'
    elif direction == 'R':
        if output == 0:
            return 'U'
        elif output == 1:
            return 'D'


def get_new_position(position, direction):
    if direction == 'U':
        return (position[0], position[1]+1)
    elif direction == 'D':
        return (position[0], position[1]-1)
    elif direction == 'L':
        return (position[0]-1, position[1])
    elif direction == 'R':
        return (position[0]+1, position[1])

def read_input_to_list(path):
    with open(path) as file:
        return [int(x) for x in file.readline().split(",")]

if __name__ == "__main__":
    puzzle = sys.argv[1]
    input = read_input_to_list("input/11.txt")
    ship_color = {}
    position = (0,0)
    if puzzle == "2":
        ship_color[position] = 1
    direction = 'U'
    intcomputer = Intcomputer(input)
    while not intcomputer.has_finished():
        output = []
        try:
            intcomputer.run(input=[ship_color.get(position, 0)], output=output)
        except Exception as e:
            pass
        ship_color[position] = output[0]
        direction = turn(direction, output[1])
        position = get_new_position(position, direction)
    
    if puzzle == "1":
        print(len(ship_color.keys()))
    elif puzzle == "2":
        whites = [p[0] for p in ship_color.items() if p[1] == 1]
        x = [v[0] for v in whites]
        y = [v[1] for v in whites]
        plt.plot(x,y, 'ko')
        plt.show()
    