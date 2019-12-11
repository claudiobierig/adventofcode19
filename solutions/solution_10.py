#!/usr/bin/env python

import sys
import itertools
import math

def get_asteroids_in_sight(current, asteroids):
    result = {}
    for asteroid in asteroids.keys():
        diff = (-current[0]+asteroid[0], current[1]-asteroid[1])
        gcd = math.gcd(diff[0], diff[1])
        if gcd == 0:
            continue
        diff = (int(diff[0]/gcd), int(diff[1]/gcd))
        if diff in result.keys():
            result[diff].append(asteroid)
        else:
            result[diff] = [asteroid]
    return result

def read_input(path):
    with open(path) as file:
        input = {}
        for i, line in enumerate(file.readlines()):
            for j, char in enumerate(line):
                if char == "#":
                    input[(j,i)] = []
    return input

def get_angle(coords):
    """
    >>> get_angle((0,1)) > get_angle((1,1)) > get_angle((1,0)) > get_angle((1,-1)) > get_angle((0,-1)) > get_angle((-1,-1)) > get_angle((-1,0)) > get_angle((-1,1))
    True
    """
    x = -coords[1]
    y = coords[0]
    r = math.sqrt(x*x + y*y)
    if y>=0:
        return math.acos(x/r)
    return -math.acos(x/r)

if __name__ == "__main__":
    input = read_input("input/10.txt")
    for key in input:
        input[key] = get_asteroids_in_sight(key, input)
    max_asteroids = 0
    station = None
    for key in input:
        if len(input[key].keys()) > max_asteroids:
            max_asteroids = len(input[key])
            station = key
    print("Solution 1: {}".format(max_asteroids))
    asteroids = input[station]
    def distance(asteroid):
        x = asteroid[0]-station[0]
        y = asteroid[1]-station[1]
        return x*x + y*y

    for angle in asteroids.keys():
        asteroids[angle].sort(key=distance)

    angles = list(asteroids.keys())
    angles.sort(key=get_angle, reverse=True)
    counter = 0
    while counter < 200:
        for angle in angles:
            if asteroids[angle]:
                shot = asteroids[angle].pop(0)
                counter += 1
                if counter == 200:
                    print("Solution 2: {}".format(shot[0]*100 + shot[1]))
                    break
    