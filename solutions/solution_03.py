#!/usr/bin/env python

import sys
import itertools

def get_end_point(starting_point, direction_distance):
    """
    Helper to compute endpoint from starting point and direction
    >>> get_end_point((1, 2), 'L1')
    (0, 2)
    >>> get_end_point((3, 4), 'R2')
    (5, 4)
    >>> get_end_point((5, 6), 'D3')
    (5, 3)
    >>> get_end_point((6, 7), 'U4')
    (6, 11)
    """
    direction = direction_distance[0]
    distance = int(direction_distance[1:])
    if direction == 'D':
        return (starting_point[0], starting_point[1] - distance)
    elif direction == 'U':
        return (starting_point[0], starting_point[1] + distance)
    elif direction == 'L':
        return (starting_point[0] - distance, starting_point[1])
    elif direction == 'R':
        return (starting_point[0] + distance, starting_point[1])

def get_points(wire):
    """
    get all points (including starting point), where the wire bends
    >>> get_points(["R75","D30","R83","U83","L12","D49","R71","U7","L72"])
    [((0, 0), (75, 0)), ((75, 0), (75, -30)), ((75, -30), (158, -30)), ((158, -30), (158, 53)), ((158, 53), (146, 53)), ((146, 53), (146, 4)), ((146, 4), (217, 4)), ((217, 4), (217, 11)), ((217, 11), (145, 11))]
    >>> get_points(["U62","R66","U55","R34","D71","R55","D58","R83"])
    [((0, 0), (0, 62)), ((0, 62), (66, 62)), ((66, 62), (66, 117)), ((66, 117), (100, 117)), ((100, 117), (100, 46)), ((100, 46), (155, 46)), ((155, 46), (155, -12)), ((155, -12), (238, -12))]
    >>> get_points(["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"])
    [((0, 0), (98, 0)), ((98, 0), (98, 47)), ((98, 47), (124, 47)), ((124, 47), (124, -16)), ((124, -16), (157, -16)), ((157, -16), (157, 71)), ((157, 71), (95, 71)), ((95, 71), (95, 51)), ((95, 51), (128, 51)), ((128, 51), (128, 104)), ((128, 104), (179, 104))]
    >>> get_points(["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"])
    [((0, 0), (0, 98)), ((0, 98), (91, 98)), ((91, 98), (91, 78)), ((91, 78), (107, 78)), ((107, 78), (107, 11)), ((107, 11), (147, 11)), ((147, 11), (147, 18)), ((147, 18), (162, 18)), ((162, 18), (162, 24)), ((162, 24), (169, 24))]
    """
    starting_point = (0, 0)
    result = []
    for part in wire:
        end_point = get_end_point(starting_point, part)
        result.append((starting_point, end_point))
        starting_point = end_point
    return result

def get_intersection_point(part1, part2):
    """
    both parts are a pair of pairs
    returns the intersection point, if the parts are intersecting, None otherwise
    >>> get_intersection_point(((1,2),(1,3)),((4,2),(4,3)))
    []
    >>> get_intersection_point(((1,2),(1,4)),((0,3),(2,3)))
    [(1, 3)]
    >>> get_intersection_point(((2,1),(4,1)),((3,0),(3,2)))
    [(3, 1)]
    >>> get_intersection_point(((2,1),(4,1)),((3,1),(3,2)))
    [(3, 1)]
    >>> get_intersection_point(((2,1),(4,1)),((2,1),(2,2)))
    [(2, 1)]
    >>> get_intersection_point(((2,1),(4,1)),((2,1),(5,1)))
    [(2, 1), (3, 1), (4, 1)]
    >>> get_intersection_point(((0, 0), (1009, 0)), ((0, 0), (-1010, 0)))
    [(0, 0)]
    >>> get_intersection_point(((0, 0), (-1010, 0)), ((225, 0), (225, 0)))
    []
    """
    x1_1 = min(part1[0][0], part1[1][0])
    x2_1 = max(part1[0][0], part1[1][0])
    y1_1 = min(part1[0][1], part1[1][1])
    y2_1 = max(part1[0][1], part1[1][1])

    x1_2 = min(part2[0][0], part2[1][0])
    x2_2 = max(part2[0][0], part2[1][0])
    y1_2 = min(part2[0][1], part2[1][1])
    y2_2 = max(part2[0][1], part2[1][1])

    if x1_1 == x1_2 == x2_1 == x2_2:
        l = [y1_1, y2_1, y1_2, y2_2]
        if y2_1 < y1_2 or y2_2 < y1_1:
            return []
        l.sort()
        return [(x1_1, y) for y in range(l[1], l[2] + 1)]
    if y1_1 == y1_2 == y2_1 == y2_2:
        l = [x1_1, x2_1, x1_2, x2_2]
        if x2_1 < x1_2 or x2_2 < x1_1:
            return []
        l.sort()
        return [(x, y1_1) for x in range(l[1], l[2] + 1)]
    if x1_1 <= x1_2 == x2_2 <= x2_1 and y1_2 <= y1_1 == y2_1 <= y2_2:
        return [(x1_2, y1_1)]
    if x1_2 <= x1_1 == x2_1 <= x2_2 and y1_1 <= y1_2 == y2_2 <= y2_1:
        return [(x1_1, y1_2)]

    return []


def collect_intersection_points(wires):
    """
    >>> collect_intersection_points([["R75","D30","R83","U83","L12","D49","R71","U7","L72"], ["U62","R66","U55","R34","D71","R55","D58","R83"]])
    [(0, 0), (158, -12), (146, 46), (155, 4), (155, 11)]
    >>> collect_intersection_points([["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"],["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"]])
    [(0, 0), (107, 47), (124, 11), (157, 18), (107, 71), (107, 51)]
    """
    points = []
    wire1 = get_points(wires[0])
    wire2 = get_points(wires[1])
    for part1, part2 in itertools.product(wire1, wire2):
        points += get_intersection_point(part1, part2)
    return points

def get_nearest_point(points):
    """
    >>> get_nearest_point([(0, 0), (158, -12), (146, 46), (155, 4), (155, 11)])
    159
    >>> get_nearest_point([(0, 0), (107, 47), (124, 11), (157, 18), (107, 71), (107, 51)])
    135
    """
    points.sort(key=manhattan)
    return manhattan(points[1])

def manhattan(point):
    return abs(point[0]) + abs(point[1])

def get_nearest_point_distance(points, wire1, wire2):
    """
    >>> get_nearest_point_distance([(0, 0), (158, -12), (146, 46), (155, 4), (155, 11)], [((0, 0), (75, 0)), ((75, 0), (75, -30)), ((75, -30), (158, -30)), ((158, -30), (158, 53)), ((158, 53), (146, 53)), ((146, 53), (146, 4)), ((146, 4), (217, 4)), ((217, 4), (217, 11)), ((217, 11), (145, 11))], [((0, 0), (0, 62)), ((0, 62), (66, 62)), ((66, 62), (66, 117)), ((66, 117), (100, 117)), ((100, 117), (100, 46)), ((100, 46), (155, 46)), ((155, 46), (155, -12)), ((155, -12), (238, -12))])
    610
    >>> get_nearest_point_distance([(0, 0), (107, 47), (124, 11), (157, 18), (107, 71), (107, 51)], [((0, 0), (98, 0)), ((98, 0), (98, 47)), ((98, 47), (124, 47)), ((124, 47), (124, -16)), ((124, -16), (157, -16)), ((157, -16), (157, 71)), ((157, 71), (95, 71)), ((95, 71), (95, 51)), ((95, 51), (128, 51)), ((128, 51), (128, 104)), ((128, 104), (179, 104))], [((0, 0), (0, 98)), ((0, 98), (91, 98)), ((91, 98), (91, 78)), ((91, 78), (107, 78)), ((107, 78), (107, 11)), ((107, 11), (147, 11)), ((147, 11), (147, 18)), ((147, 18), (162, 18)), ((162, 18), (162, 24)), ((162, 24), (169, 24))])
    410
    """
    def get_distance(point):
        d = 0
        for wire in (wire1, wire2):
            for part in wire:
                intersection = get_intersection_point(part, (point, point))
                if intersection == []:
                    d += abs(part[0][0] - part[1][0]) + abs(part[0][1] - part[1][1])
                else:
                    d += abs(part[0][0] - point[0]) + abs(part[0][1] - point[1])
                    break
        return d
    
    points.sort(key=get_distance)
    return get_distance(points[1])

def read_input_to_lists(path):
    with open(path) as file:
        return [line.strip().split(",") for line in file.readlines()]

if __name__ == "__main__":
    puzzle = sys.argv[1]
    input = read_input_to_lists(sys.argv[2])
    if puzzle == "1":
        intersections = collect_intersection_points(input)
        print(intersections)
        print(get_nearest_point(intersections))
    elif puzzle == "2":
        intersections = collect_intersection_points(input)
        wire1 = get_points(input[0])
        wire2 = get_points(input[1])
        print(intersections)
        print(get_nearest_point_distance(intersections, wire1, wire2))
    else:
        print("Input argument 1 needs to be 1 or 2", file=sys.stderr)
        exit(1)
