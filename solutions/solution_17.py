#!/usr/bin/env python

from intcomputer import Intcomputer
import networkx as nx
import itertools


NODECHARS = '#><^v'

def read_input_to_list(path):
    with open(path) as file:
        return [int(x) for x in file.readline().split(",")]

def intoutput_to_charlists(output):
    return ''.join([chr(i) for i in output]).split('\n')

def get_direction_change(old, current, new):
    """
    >>> get_direction_change((0,-1),(0,0),(1,0))
    'R'
    >>> get_direction_change((0,-1),(0,0),(0,1))
    'L'
    >>> get_direction_change((0,1),(0,0),(1,0))
    'L'
    >>> get_direction_change((0,1),(0,0),(0,1))
    'R'
    >>> get_direction_change((-1,0),(0,0),(0,1))
    'L'
    >>> get_direction_change((-1,0),(0,0),(0,-1))
    'R'
    >>> get_direction_change((1,0),(0,0),(0,1))
    'R'
    >>> get_direction_change((1,0),(0,0),(1,-1))
    'L'
    """
    if old[0] == current[0]:
        if (old[1] < current[1]) == (current[0] < new[0]):
            return 'R'
        else:
            return 'L'
    elif old[1] == current[1]:
        if (old[0] < current[0]) == (current[1] > new[1]):
            return 'R'
        else:
            return 'L'

def get_next_part(G, old, current):
    for n in G.neighbors(current):
        if n != old:
            break
    
    if n == old:
        return None

    direction = get_direction_change(old, current, n)
    diff = (n[0] - current[0], n[1] - current[1])
    dist = 1
    while (current[0] + dist*diff[0], current[1] + dist*diff[1]) in G.nodes:
        dist += 1
    dist -= 1
    return [
        (direction, str(dist)),
        (current[0] + (dist-1)*diff[0], current[1] + (dist-1)*diff[1]),
        (current[0] + dist*diff[0], current[1] + dist*diff[1])
        ]


def is_allowed(full, sub1, sub2):
    """
    >>> is_allowed("aeyceayaeyyecaeyaeyyecceayyecceay", "aey", "cea")
    >>> is_allowed("aeyceayaeyyecaeyaeyyecceayyecceay", "aey", "ceay")
    'yec'
    """
    i = len(sub1)
    j = len(sub2)
    start = i+j
    remainings1 = []
    result = full.find(sub1, start)
    while result > 0:
        if result > start:
            remainings1.append(full[start:result])
        start = result+i
        result = full.find(sub1, start)
    if start < len(full):
        remainings1.append(full[start:])
    
    remainings2 = []
    for r in remainings1:
        start = 0
        result = r.find(sub2, start)
        while result > 0:
            if result > start:
                remainings2.append(r[start:result])
            start = result+j
            result = r.find(sub2, start)
        if start < len(r):
            remainings2.append(r[start:])

    if len(set(remainings2)) == 1 and len(remainings2[0]) < 9:
        return remainings2[0]


def get_pattern(full, sub1, sub2, sub3):
    """
    >>> get_pattern("aeyceayaeyyecaeyaeyyecceayyecceay", "aey", "ceay", "yec")
    [65, 44, 66, 44, 65, 44, 67, 44, 65, 44, 65, 44, 67, 44, 66, 44, 67, 44, 66, 10]
    """
    result = []
    position = 0
    while position < len(full):
        r1 = full.find(sub1, position)
        if r1 == position:
            result.append(65)
            result.append(44)
            position += len(sub1)
            continue
        r2 = full.find(sub2, position)
        if r2 == position:
            result.append(66)
            result.append(44)
            position += len(sub2)
            continue
        r3 = full.find(sub3, position)
        if r3 == position:
            result.append(67)
            result.append(44)
            position += len(sub3)
            continue
    result[-1] = 10
    return result

def get_moves(movecommands):
    result = []
    for step in movecommands:
        result.append(ord(step[0]))
        result.append(44)
        for c in step[1]:
            result.append(ord(c))
        result.append(44)
    result[-1] = 10
    return result

if __name__ == "__main__":
    input = read_input_to_list("input/17.txt")
    intcomputer = Intcomputer(input)
    output = []
    intcomputer.run(output=output)
    ascii = intoutput_to_charlists(output)
    G = nx.Graph()
    for row, line in enumerate(ascii):
        for column, c in enumerate(line):
            if c in NODECHARS:
                G.add_node((row,column), type=c)
                if column > 0 and ascii[row][column-1] in NODECHARS:
                    G.add_edge((row, column), (row, column -1))
                if row > 0 and ascii[row-1][column] in NODECHARS:
                    G.add_edge((row, column), (row-1, column))
    
    counter = 0
    for node in G.nodes:
        if len(G.edges(node)) > 2:
            counter += node[0]*node[1]
    print("Solution 1:")
    print(counter)

    start = [n for n in G.nodes(data='type') if n[1]!='#'][0]
    current = start[0]
    if start[1] == '^':
        old = (current[0]+1, current[1])
    elif start[1] == 'v':
        old = (current[0]-1, current[1])
    elif start[1] == '>':
        old = (current[0], current[1]-1)
    elif start[1] == '<':
        old = (current[0], current[1]+1)
    
    path = []
    next_part = get_next_part(G, old, current)
    while next_part is not None:
        path.append(next_part[0])
        old = next_part[1]
        current = next_part[2]
        next_part = get_next_part(G, old, current)

    tolookat = ""
    for step in path:
        if step[0] == 'L':
            tolookat += chr(-int(step[1]) + 109)
        else:
            tolookat += chr(int(step[1]) + 109)

    for i, j in itertools.product(range(3,9), range(3,9)):
        sub1 = tolookat[:i]
        sub2 = tolookat[i:i+j]
        sub3 = is_allowed(tolookat, sub1, sub2)
        if sub3 is not None:
            break
    position = tolookat.find(sub3)
    k = len(sub3)

    pattern = get_pattern(tolookat, sub1, sub2, sub3)
    A = get_moves(path[:i])
    B = get_moves(path[i:i+j])
    C = get_moves(path[position:position+k])
    inp = pattern + A + B + C + [ord('n')] + [10]

    input[0] = 2
    intcomputer = Intcomputer(input)
    output = []
    intcomputer.run(input=inp, output=output)
    print("Solution 2:")
    print(output[-1])