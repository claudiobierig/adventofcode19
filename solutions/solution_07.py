#!/usr/bin/env python

import sys
import itertools
from intcomputer import Intcomputer


class Amplifier:
    """
    """
    def __init__(self, input, phase):
        self._intcomputer = Intcomputer(input)
        self._phase = phase

    def has_finished(self):
        return self._intcomputer.has_finished()

    def run(self, inp):
        out = []
        def save_output(res):
            out.append(res)
        try:
            self._intcomputer.run(input=inp, output=save_output)
        except Exception as e:
            pass
        return out


def read_input_to_list(path):
    with open(path) as file:
        return [int(x) for x in file.readline().split(",")]

if __name__ == "__main__":
    puzzle = sys.argv[1]
    input = read_input_to_list(sys.argv[2])
    if puzzle == "1":
        thrusts = []
        for perm in itertools.permutations(range(5)):
            inp = [0]
            for phase in perm:
                amplifier = Amplifier(input, phase)
                inp = amplifier.run([phase] + inp)
            thrusts.append(inp[0])
        print(max(thrusts))

    elif puzzle == "2":
        thrusts = []
        for perm in itertools.permutations(range(5,10)):
            amps = [Amplifier(input, phase) for phase in perm]
            inp = [0]
            for amp in amps:
                inp = amp.run([amp._phase] + inp)
            while not amps[-1].has_finished():
                for amp in amps:
                    inp = amp.run(inp)
            thrusts.append(inp[0])
        print(max(thrusts))


    else:
        print("Input argument 1 needs to be 1 or 2", file=sys.stderr)
        exit(1)
