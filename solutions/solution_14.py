#!/usr/bin/env python

import math

def read_input(path):
    with open(path) as file:
        reactions = [line.strip().split('=>') for line in file.readlines()]
        reactions2 = [[r[0].strip().split(","), r[1].strip()] for r in reactions]
        result = {}
        for reaction in reactions2:
            goal = reaction[1].strip().split()
            goal_resource = goal[1]
            goal_amount = int(goal[0])
            start = [r.strip().split() for r in reaction[0]]
            start2 = [[int(s[0]), s[1]] for s in start]
            result[goal_resource] = [goal_amount, start2]
        return result

def get_amount(resource, amount_needed, reactions, leftovers):
    reaction = reactions[resource]
    leftover = leftovers.get(resource, 0)
    number_of_reactions = math.ceil((amount_needed - leftover)/reaction[0])
    leftovers[resource] = leftover + number_of_reactions*reaction[0] - amount_needed
    return [[number_of_reactions*r[0], r[1]] for r in reaction[1]]

def need_reaction(required_resources):
    for resource in required_resources:
        if resource[1] != "ORE":
            return True
    return False

def reduce_leftovers(leftovers, reactions):
    """
    >>> reactions = read_input("input/14.txt")
    >>> leftovers = {"DWBL": 10}
    >>> reduce_leftovers(leftovers, reactions)
    >>> leftovers
    {'DWBL': 1, 'ORE': 149}
    >>> leftovers = {"ZKZHV": 9}
    >>> reduce_leftovers(leftovers, reactions)
    >>> leftovers
    {'ZKZHV': 1, 'KFKWH': 0, 'DWBL': 2, 'ORE': 532}
    >>> reduce_leftovers(leftovers, reactions)
    >>> leftovers
    {'ZKZHV': 1, 'KFKWH': 0, 'DWBL': 2, 'ORE': 532}
    >>> leftovers = {'FUEL': 0, 'BRTX': 1, 'CFBP': 1, 'HJPD': 3, 'HDRMK': 1, 'LWGNJ': 2, 'JVGRC': 2, 'CVZLJ': 2, 'PZRSQ': 2, 'LQBJP': 1, 'DVRS': 4, 'TNRGW': 2, 'QGVJV': 0, 'NSWDH': 6, 'XMHN': 0, 'PDKZ': 1, 'NDNP': 3, 'DBKL': 1, 'RLKDF': 0, 'DQPX': 0, 'BWHKF': 0, 'QMQB': 0, 'QZMZ': 3, 'HJFV': 0, 'SLQN': 2, 'XHKG': 6, 'KXHQW': 3, 'GHNG': 1, 'CSNS': 1, 'JVRQ': 0, 'PHBMP': 6, 'LZWR': 1, 'JKRZH': 0, 'WKFTZ': 2, 'GFDP': 3, 'ZKZHV': 0, 'XJFQR': 3, 'JQFM': 0, 'WQCT': 0, 'QMTMN': 0, 'QDJD': 0, 'FRTK': 2, 'MLJN': 8, 'LHXN': 2, 'DWBL': 1, 'MCWF': 2, 'VCMPS': 0, 'SVTK': 7, 'XNGTQ': 2, 'MXQF': 2, 'XCMJ': 3, 'NHVQD': 6, 'WGLN': 1, 'KFKWH': 0, 'VMDSG': 2, 'BMSNV': 0, 'WCMV': 4, 'ZJKB': 2, 'TDPN': 0}
    >>> reduce_leftovers(leftovers, reactions)
    >>> leftovers
    {'FUEL': 0, 'BRTX': 1, 'CFBP': 1, 'HJPD': 3, 'HDRMK': 1, 'LWGNJ': 2, 'JVGRC': 2, 'CVZLJ': 2, 'PZRSQ': 2, 'LQBJP': 1, 'DVRS': 4, 'TNRGW': 2, 'QGVJV': 0, 'NSWDH': 6, 'XMHN': 0, 'PDKZ': 1, 'NDNP': 3, 'DBKL': 1, 'RLKDF': 0, 'DQPX': 0, 'BWHKF': 0, 'QMQB': 0, 'QZMZ': 3, 'HJFV': 0, 'SLQN': 2, 'XHKG': 6, 'KXHQW': 3, 'GHNG': 1, 'CSNS': 1, 'JVRQ': 0, 'PHBMP': 6, 'LZWR': 1, 'JKRZH': 0, 'WKFTZ': 2, 'GFDP': 3, 'ZKZHV': 0, 'XJFQR': 3, 'JQFM': 0, 'WQCT': 0, 'QMTMN': 0, 'QDJD': 0, 'FRTK': 2, 'MLJN': 8, 'LHXN': 2, 'DWBL': 1, 'MCWF': 2, 'VCMPS': 0, 'SVTK': 7, 'XNGTQ': 2, 'MXQF': 2, 'XCMJ': 3, 'NHVQD': 6, 'WGLN': 1, 'KFKWH': 0, 'VMDSG': 2, 'BMSNV': 0, 'WCMV': 4, 'ZJKB': 2, 'TDPN': 0}
    >>> leftovers = {"ZKZHV": 8, 'DWBL': 7}
    >>> reduce_leftovers(leftovers, reactions)
    >>> leftovers
    {'ZKZHV': 0, 'DWBL': 0, 'KFKWH': 0, 'ORE': 681}
    """
    can_reduce = True
    while can_reduce:
        can_reduce = False
        to_add = {}
        for key in leftovers.keys():
            if key == "ORE":
                continue
            if reactions[key][0] <= leftovers[key]:
                times = int(leftovers[key]/reactions[key][0])
                can_reduce = True
                leftovers[key] -= times*reactions[key][0]
                for r in reactions[key][1]:
                    to_add[r[1]] = to_add.get(r[1], 0) + times*r[0]
        for key, value in to_add.items():
            leftovers[key] = leftovers.get(key, 0) + value
    
if __name__ == "__main__":
    input = read_input("input/14.txt")
    leftovers = {}
    required_resources = get_amount("FUEL", 1, input, leftovers)
    while need_reaction(required_resources):
        i = 0
        while required_resources[i][1] == "ORE":
            i += 1
        required_resources += get_amount(required_resources[i][1], required_resources[i][0], input, leftovers)
        required_resources.pop(i)
        

    required_ore = 0
    for r in required_resources:
        required_ore += r[0]
    print("Solution1")
    print(required_ore)
    


    max_ore = 1000000000000
    without_problems = int(max_ore/required_ore)
    leftovers2 = {k:without_problems*leftovers[k] for k in leftovers.keys()}
    ore = required_ore*without_problems
    fuel = without_problems
    reduce_leftovers(leftovers2, input)
    ore -= leftovers2.get("ORE", 0)
    leftovers2["ORE"] = 0

    while without_problems > 0:
        without_problems = int((max_ore-ore)/required_ore)
        for key, value in leftovers.items():
            leftovers2[key] = leftovers2.get(key, 0) + value*without_problems
        ore += required_ore*without_problems
        fuel += without_problems
        reduce_leftovers(leftovers2, input)
        ore -= leftovers2.get("ORE", 0)
        leftovers2["ORE"] = 0

    leftovers2["FUEL"] = 1
    reduce_leftovers(leftovers2, input)
    ore -= leftovers2.get("ORE", 0)
    if ore<=max_ore:
        fuel += 1

    print("Solution 2")
    print(fuel)
