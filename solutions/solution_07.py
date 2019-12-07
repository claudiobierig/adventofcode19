#!/usr/bin/env python

import sys
import itertools
from intcomputer import Intcomputer


class Amplifier:
    def __init__(self, input, phase):
        self._intcomputer = Intcomputer(input)
        self._phase = phase

    def has_finished(self):
        return self._intcomputer.has_finished()

    def get_phase(self):
        return self._phase

    def run(self, inp):
        out = []
        def save_output(res):
            out.append(res)
        try:
            self._intcomputer.run(input=inp, output=save_output)
        except Exception as e:
            pass
        return out

def get_maximum_thrust_without_loop(input, inp, phases):
    """
    >>> input = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
    >>> inp = [0]
    >>> phases = range(5)
    >>> get_maximum_thrust_without_loop(input, inp.copy(), phases)
    43210
    >>> input = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
    >>> get_maximum_thrust_without_loop(input, inp.copy(), phases)
    54321
    >>> input = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
    >>> get_maximum_thrust_without_loop(input, inp.copy(), phases)
    65210
    """
    thrusts = []
    save_inp = inp.copy()
    for perm in itertools.permutations(phases):
        inp = save_inp.copy()
        for phase in perm:
            amplifier = Amplifier(input, phase)
            inp = amplifier.run([phase] + inp)
        thrusts.append(inp[0])
    return max(thrusts)


def get_maximum_thrust_with_loop(input, inp, phases):
    """
    >>> input = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
    >>> inp = [0]
    >>> phases = range(5, 10)
    >>> get_maximum_thrust_with_loop(input, inp.copy(), phases)
    139629729
    >>> input = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
    >>> get_maximum_thrust_with_loop(input, inp.copy(), phases)
    18216
    """
    thrusts = []
    save_inp = inp.copy()
    for perm in itertools.permutations(phases):
        amps = [Amplifier(input, phase) for phase in perm]
        inp = save_inp.copy()
        for amp in amps:
            inp = amp.run([amp.get_phase()] + inp)
        while not amps[-1].has_finished():
            for amp in amps:
                inp = amp.run(inp)
        thrusts.append(inp[0])
    return max(thrusts)



def read_input_to_list(path):
    with open(path) as file:
        return [int(x) for x in file.readline().split(",")]

if __name__ == "__main__":
    puzzle = sys.argv[1]
    input = read_input_to_list(sys.argv[2])
    if puzzle == "1":
        print(get_maximum_thrust_without_loop(input, [0], range(5)))
    elif puzzle == "2":
        print(get_maximum_thrust_with_loop(input, [0], range(5,10)))
    else:
        print("Input argument 1 needs to be 1 or 2", file=sys.stderr)
        exit(1)
