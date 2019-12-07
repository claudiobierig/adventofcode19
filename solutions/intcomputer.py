#!/usr/bin/env python

class Intcomputer:

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
