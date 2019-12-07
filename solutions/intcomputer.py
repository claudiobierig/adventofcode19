#!/usr/bin/env python

def sysinput():
    return input("Input requested:")

class Intcomputer:
    """
    >>> intcomputer = Intcomputer([1,9,10,3,2,3,11,0,99,30,40,50])
    >>> intcomputer.run()
    >>> intcomputer._memory
    [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
    >>> intcomputer = Intcomputer([1,0,0,0,99])
    >>> intcomputer.run()
    >>> intcomputer._memory
    [2, 0, 0, 0, 99]
    >>> intcomputer = Intcomputer([2,3,0,3,99])
    >>> intcomputer.run()
    >>> intcomputer._memory
    [2, 3, 0, 6, 99]
    >>> intcomputer = Intcomputer([2,4,4,5,99,0])
    >>> intcomputer.run()
    >>> intcomputer._memory
    [2, 4, 4, 5, 99, 9801]
    >>> intcomputer = Intcomputer([1,1,1,4,99,5,6,0,99])
    >>> intcomputer.run()
    >>> intcomputer._memory
    [30, 1, 1, 4, 2, 5, 6, 0, 99]
    >>> intcomputer = Intcomputer([3,0,4,0,99])
    >>> intcomputer.run(input=[3])
    3
    >>> intcomputer = Intcomputer([1002,4,3,4,33])
    >>> intcomputer.run()
    >>> intcomputer._memory
    [1002, 4, 3, 4, 99]
    >>> intcomputer = Intcomputer([1101,100,-1,4,0])
    >>> intcomputer.run()
    >>> intcomputer._memory
    [1101, 100, -1, 4, 99]
    >>> input = [3,9,8,9,10,9,4,9,99,-1,8]
    >>> intcomputer = Intcomputer(input)
    >>> intcomputer.run(input=[3])
    0
    >>> intcomputer = Intcomputer(input)
    >>> intcomputer.run(input=[8])
    1
    >>> input = [3,9,7,9,10,9,4,9,99,-1,8]
    >>> intcomputer = Intcomputer(input)
    >>> intcomputer.run(input=[8])
    0
    >>> intcomputer = Intcomputer(input)
    >>> intcomputer.run(input=[7])
    1
    >>> intcomputer = Intcomputer(input)
    >>> intcomputer.run(input=[9])
    0
    >>> input = [3,3,1108,-1,8,3,4,3,99]
    >>> intcomputer = Intcomputer(input)
    >>> intcomputer.run(input=[9])
    0
    >>> intcomputer = Intcomputer(input)
    >>> intcomputer.run(input=[8])
    1
    >>> input = [3,3,1107,-1,8,3,4,3,99]
    >>> intcomputer = Intcomputer(input)
    >>> intcomputer.run(input=[8])
    0
    >>> intcomputer = Intcomputer(input)
    >>> intcomputer.run(input=[7])
    1
    >>> input = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
    >>> intcomputer = Intcomputer(input)
    >>> intcomputer.run(input=[7])
    1
    >>> intcomputer = Intcomputer(input)
    >>> intcomputer.run(input=[0])
    0
    >>> input = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
    >>> intcomputer = Intcomputer(input)
    >>> intcomputer.run(input=[0])
    0
    >>> intcomputer = Intcomputer(input)
    >>> intcomputer.run(input=[1])
    1
    >>> input = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
    >>> intcomputer = Intcomputer(input)
    >>> intcomputer.run(input=[1])
    999
    >>> intcomputer = Intcomputer(input)
    >>> intcomputer.run(input=[8])
    1000
    >>> intcomputer = Intcomputer(input)
    >>> intcomputer.run(input=[9])
    1001
    """

    def __init__(self, memory):
        self._memory = memory.copy()
        self._index = 0
        self._finished = False
    
    def set_noun_verb(self, noun, verb):
        self._memory[1] = noun
        self._memory[2] = verb
    
    def get_start(self):
        return self._memory[0]

    def has_finished(self):
        return self._finished or self._index >= len(self._memory)

    def get_instruction_values(self, number):
        operation = self._memory[self._index]
        values = []
        for i in range(number):
            value = self._memory[self._index + i + 1]
            if int(operation/(pow(10,i+2)))%10 == 0:
                value = self._memory[value]
            values.append(value)
        return values


    def run(self, input=[], output=print):
        while self._index < len(self._memory):
            operation = self._memory[self._index]
            if operation % 100 == 1:
                values = self.get_instruction_values(2)
                values.append(self._memory[self._index + 3])
                self._memory[values[2]] = values[0] + values[1]
                self._index += 4
            elif operation % 100 == 2:
                values = self.get_instruction_values(2)
                values.append(self._memory[self._index + 3])
                self._memory[values[2]] = values[0] * values[1]
                self._index += 4
            elif operation % 100 == 3:
                self._memory[self._memory[self._index + 1]] = input.pop(0)
                self._index += 2
            elif operation % 100 == 4:
                values = self.get_instruction_values(1)
                output(values[0])
                self._index += 2
            elif operation % 100 == 5:
                values = self.get_instruction_values(2)
                if values[0] != 0:
                    self._index = values[1]
                else:
                    self._index += 3
            elif operation % 100 == 6:
                values = self.get_instruction_values(2)
                if values[0] == 0:
                    self._index = values[1]
                else:
                    self._index += 3
            elif operation % 100 == 7:
                values = self.get_instruction_values(2)
                values.append(self._memory[self._index + 3])
                if values[0] < values[1]:
                    self._memory[values[2]] = 1
                else:
                    self._memory[values[2]] = 0
                self._index += 4
            elif operation % 100 == 8:
                values = self.get_instruction_values(2)
                values.append(self._memory[self._index + 3])
                if values[0] == values[1]:
                    self._memory[values[2]] = 1
                else:
                    self._memory[values[2]] = 0
                self._index += 4
            elif operation % 100 == 99:
                self._finished = True
                break
            else:
                raise Exception("invalid intcomputer")
