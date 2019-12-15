#!/usr/bin/env python

import sys
from intcomputer import Intcomputer
import matplotlib.pyplot as plt
import numpy as np

def read_input_to_list(path):
    with open(path) as file:
        return [int(x) for x in file.readline().split(",")]

def step(intcomputer, input):
    output = []
    try:
        intcomputer.run(input=input, output=output)
    except Exception as e:
        pass
    out_np = np.array(output)
    elements = np.reshape(out_np, (int(len(output)/3), 3))
    return elements

def update_field(output, field):
    for update in output:
        if update[0] == -1 and update[1] == 0:
            print("Score: {}".format(update[2]))
        else:
            field[update[0], update[1]] = update[2]

def get_plottable_lists(value, field):
    results = [[],[]]
    for i, row in enumerate(field):
        for j, v in enumerate(row):
            if value == v:
                results[0].append(i)
                results[1].append(j)
    return results

def plot(field):
    walls = get_plottable_lists(1, field)
    blocks = get_plottable_lists(2, field)
    paddle = get_plottable_lists(3, field)
    ball = get_plottable_lists(4, field)

    plt.plot(walls[0], walls[1], 'ro')
    plt.plot(blocks[0], blocks[1], 'bo')
    plt.plot(paddle[0], paddle[1], 'go')
    plt.plot(ball[0], ball[1], 'ko')
    plt.show()
    plt.cla()
    plt.clf()
    plt.close()

def find(object, array):
    for i, row in enumerate(array):
        for j, v in enumerate(row):
            if v == object:
                return [i, j]
    return []

def estimate_ball(prev_ball, ball, field):
    next_ball = [2*ball[0]-prev_ball[0],2*ball[1]-prev_ball[1]]
    if next_ball[1] == 21 and field[ball[0], next_ball[1]] == 3:
        return ball[0]
    if field[next_ball[0], next_ball[1]] != 0 and field[ball[0], next_ball[1]] == 0:
        return prev_ball[0]
    if field[next_ball[0], ball[1]] != 0 and field[ball[0], next_ball[1]] != 0:
        return prev_ball[0]
    if field[next_ball[0], ball[1]] != 0:
        return prev_ball[0]
    if field[ball[0], next_ball[1]] != 0 and (field[next_ball[0], prev_ball[1]] != 0 or field[next_ball[0], ball[1]] != 0):
        return prev_ball[0]

    return next_ball[0]

if __name__ == "__main__":
    input = read_input_to_list("input/13.txt")
    intcomputer = Intcomputer(input)
    output = []
    intcomputer.run(output=output)
    out_np = np.array(output)
    elements = np.reshape(out_np, (int(len(output)/3), 3))
    counter = 0
    for row in elements:
        if row[2] == 2:
            counter += 1

    input[0] = 2
    intcomputer = Intcomputer(input)
    out = step(intcomputer, [])
    x = [min(out[:,0]), max(out[:,0])]
    y = [min(out[:,1]), max(out[:,1])]
    field = np.zeros([x[1]-x[0]+1, y[1]-y[0]+1], dtype=int)
    update_field(out, field)
    prev_ball = find(4, field)
    out = step(intcomputer, [0])
    update_field(out, field)
    ball = find(4, field)
    while find(2, field) and ball[1] > 0:
        paddle = find(3, field)
        new_x = estimate_ball(prev_ball, ball, field)
        inp = 0
        if new_x > paddle[0]:
            inp = 1
        elif new_x < paddle[0]:
            inp = -1
        out = step(intcomputer, [inp])
        update_field(out, field)
        prev_ball = ball
        ball = find(4, field)
