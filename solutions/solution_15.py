#!/usr/bin/env python

from intcomputer import Intcomputer
import networkx as nx


def read_input_to_list(path):
    with open(path) as file:
        return [int(x) for x in file.readline().split(",")]

def get_neighbours(point):
    """
    >>> get_neighbours((0, 0))
    [(-1, 0), (0, 1), (1, 0), (0, -1)]
    """
    return [(point[0]-1, point[1]), (point[0], point[1]+1), (point[0]+1, point[1]), (point[0], point[1]-1)]

def get_next_to_explore(unexplored):
    keys = list(unexplored.keys())
    keys.reverse()
    for key in keys:
        if len(unexplored[key]) > 0:
            return (key, unexplored[key][0])
    return None

class Robot:
    def __init__(self, intcomputer):
        self._intcomputer = intcomputer
        self._position = (0,0)
    
    def goto(self, G, new_position):
        path = nx.shortest_path(G, self._position, new_position)
        input = []
        for i in range(len(path) - 1):
            old = path[i]
            new = path[i+1]
            input.append(get_direction(old, new))
        output = []
        try:
            self._intcomputer.run(input=input, output=output)
        except:
            pass
        if output[-1] == 0:
            self._position = path[i]
            return 0
        elif output[-1] == 1:
            self._position = new_position
            return 1
        elif output[-1] == 2:
            self._position = new_position
            return 2
        else:
            raise Exception("Unexpected output")

def get_direction(old, new):
    if old[0] == new[0]:
        if old[1] == new[1]-1:
            return 1
        elif old[1] == new[1]+1:
            return 2
    elif old[1] == new[1]:
        if old[0] == new[0]-1:
            return 3
        elif old[0] == new[0]+1:
            return 4
    raise Exception("get_direction not called with neighbouring nodes.")

if __name__ == "__main__":
    input = read_input_to_list("input/15.txt")
    intcomputer = Intcomputer(input)
    robot = Robot(intcomputer)
    unexplored = {(0,0) : get_neighbours((0,0))}

    G = nx.Graph()
    G.add_node((0,0), type=0)
    to_explore = get_next_to_explore(unexplored)
    while to_explore is not None:
        G.add_node(to_explore[1], type=-1)
        G.add_edge(to_explore[0], to_explore[1])
        result = robot.goto(G, to_explore[1])
        if result == 0:
            G.remove_edge(to_explore[0], to_explore[1])
            G.remove_node(to_explore[1])
        else:
            G.nodes[to_explore[1]]['type'] = result
            neighbours = get_neighbours(to_explore[1])
            unexplored[to_explore[1]] = []
            for n in neighbours:
                if n in G.nodes:
                    G.add_edge(to_explore[1], n)
                else:
                    unexplored[to_explore[1]].append(n)
        unexplored[to_explore[0]].remove(to_explore[1])
        to_explore = get_next_to_explore(unexplored)

    oxygen = [n[0] for n in G.nodes(data='type') if n[1]==2]
    path = nx.shortest_path(G, (0,0), oxygen[0])
    print("Solution 1:")
    print(len(path) - 1)

    print("Solution 2:")
    print(max(nx.shortest_path_length(G, oxygen[0]).values()))
