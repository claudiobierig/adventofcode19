#!/usr/bin/env python

def get_mode(operation, i):
    """
    >>> get_mode(101, 0)
    1
    >>> get_mode(1, 0)
    0
    >>> get_mode(1101, 0)
    1
    >>> get_mode(1001, 0)
    0
    >>> get_mode(1101, 1)
    1
    >>> get_mode(1001, 1)
    1
    
    """
    if len(str(operation)) > i + 2:
        mode = int(str(operation)[-i-3])
    else:
        mode = 0
    return mode

class Intcomputer:

    def __init__(self, memory):
        self._memory = memory.copy()
        self._index = 0
        self._finished = False
        self._relative_base = 0
    
    def get_memory(self, i):
        if i<0:
            raise Exception("tried to get memory below 0")
        if i >= len(self._memory):
            return 0
        return self._memory[i]
    
    def set_memory(self, i, value):
        if i >= len(self._memory):
            self._memory += [0]*(i-len(self._memory)+1)
        self._memory[i] = value

    def set_noun_verb(self, noun, verb):
        self.set_memory(1, noun)
        self.set_memory(2, verb)
    
    def get_start(self):
        return self.get_memory(0)

    def has_finished(self):
        return self._finished

    def get_instruction_values(self, number):
        operation =  self.get_memory(self._index)
        values = []
        for i in range(number):
            value = self.get_memory(self._index + i + 1)
            mode = get_mode(operation, i)#int(operation/(pow(10,i+2)))%10
            if mode == 0:
                value = self.get_memory(value)
            elif mode == 2:
                value = self.get_memory(value + self._relative_base)
            values.append(value)
        return values

    def get_relative_only_value(self, number):
        operation =  self.get_memory(self._index)
        value = self.get_memory(self._index + number)
        mode = get_mode(operation, number - 1)
        if mode == 2:
            value = value + self._relative_base
        return value

    def run(self, input=None, output=None):
        if input is None:
            input = []
        if output is None:
            output = []
        while not self._finished:
            operation = self.get_memory(self._index)
            if operation % 100 == 1:
                values = self.get_instruction_values(2)
                values.append(self.get_relative_only_value(3))
                self.set_memory(values[2], values[0] + values[1])
                self._index += 4
            elif operation % 100 == 2:
                values = self.get_instruction_values(2)
                values.append(self.get_relative_only_value(3))
                self.set_memory(values[2], values[0] * values[1])
                self._index += 4
            elif operation % 100 == 3:
                value = self.get_relative_only_value(1)
                self.set_memory(value, input.pop(0))
                self._index += 2
            elif operation % 100 == 4:
                values = self.get_instruction_values(1)
                output.append(values[0])
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
                values.append(self.get_relative_only_value(3))
                if values[0] < values[1]:
                    self.set_memory(values[2], 1)
                else:
                    self.set_memory(values[2], 0)
                self._index += 4
            elif operation % 100 == 8:
                values = self.get_instruction_values(2)
                values.append(self.get_relative_only_value(3))
                if values[0] == values[1]:
                    self.set_memory(values[2], 1)
                else:
                    self.set_memory(values[2], 0)
                self._index += 4
            elif operation % 100 == 9:
                values = self.get_instruction_values(1)
                self._relative_base += values[0]
                self._index += 2
            elif operation % 100 == 99:
                self._finished = True
                break
            else:
                raise Exception("invalid intcomputer")
