#!/usr/bin/env python

import sys
import numpy as np
import itertools

def get_layered_array(input, rows, columns):
    """
    >>> get_layered_array([1,2,3,4,5,6,7,8,9,0,1,2], 2, 3)
    array([[[1, 2, 3],
            [4, 5, 6]],
    <BLANKLINE>
           [[7, 8, 9],
            [0, 1, 2]]])
    """
    number_of_layers = int(len(input)/(rows*columns))
    return np.array(input).reshape(number_of_layers, rows, columns)

def count_numbers(layer, numbers):
    result = np.zeros(len(numbers), dtype=int)
    for el in layer.flatten():
        for i, n in enumerate(numbers):
            if el == n:
                result[i] += 1
    return result

def get_solution_one(input, rows, columns):
    a = get_layered_array(input, rows, columns)
    min_zeros = rows*columns + 1
    solution = []
    for layer in a:
        r = count_numbers(layer, [0, 1, 2])
        if r[0] < min_zeros:
            min_zeros = r[0]
            solution = r
    return solution[1]*solution[2]

def stack_pixel(pixel_top, pixel_bottom):
    """
    >>> stack_pixel(1, 0)
    1
    >>> stack_pixel(1, 1)
    1
    >>> stack_pixel(1, 2)
    1
    >>> stack_pixel(2, 0)
    0
    >>> stack_pixel(2, 1)
    1
    >>> stack_pixel(2, 2)
    2
    >>> stack_pixel(0, 0)
    0
    >>> stack_pixel(0, 1)
    0
    >>> stack_pixel(0, 2)
    0
    """
    if pixel_top == 2:
        return pixel_bottom
    return pixel_top

def stack_layer(layer_top, layer_bottom):
    shape = np.shape(layer_top)
    layer = np.zeros(shape, dtype=int)
    for i, j in itertools.product(range(shape[0]), range(shape[1])):
        layer[i, j] = stack_pixel(layer_top[i][j], layer_bottom[i][j])
    return layer

def stack_all_layers(input, rows, columns):
    """
    >>> s = '0222112222120000'
    >>> input = [int(c) for c in s]
    >>> layer = stack_all_layers(input, 2, 2)
    >>> layer[0][0]
    0
    >>> layer[0][1]
    1
    >>> layer[1][0]
    1
    >>> layer[1][1]
    0
    """
    a = get_layered_array(input, rows, columns)
    number_of_layers = np.shape(a)[0]
    layer = a[0]
    for i in range(1, number_of_layers):
        layer = stack_layer(layer, a[i])
    return layer

def read_input_to_list(path):
    with open(path) as file:
        return [int(c) for c in file.readline().strip()]

if __name__ == "__main__":
    puzzle = sys.argv[1]
    input = read_input_to_list(sys.argv[2])
    if puzzle == "1":
        print(get_solution_one(input, 6, 25))
    elif puzzle == "2":
        print(stack_all_layers(input, 6, 25))
    else:
        print("Input argument 1 needs to be 1 or 2", file=sys.stderr)
        exit(1)
