#!/usr/bin/env python

import unittest
from intcomputer import Intcomputer

class TestIntcomputer(unittest.TestCase):

    def test_basic_run_1(self):
        intcomputer = Intcomputer([1,9,10,3,2,3,11,0,99,30,40,50])
        intcomputer.run()
        self.assertEqual(intcomputer.get_start(), 3500)

    def test_basic_run_2(self):
        intcomputer = Intcomputer([1,0,0,0,99])
        intcomputer.run()
        self.assertEqual(intcomputer.get_start(), 2)        

    def test_basic_run_3(self):
        intcomputer = Intcomputer([2,3,0,3,99])
        intcomputer.run()
        self.assertEqual(intcomputer.get_start(), 2)

    def test_basic_run_4(self):
        intcomputer = Intcomputer([2,4,4,5,99,0])
        intcomputer.run()
        self.assertEqual(intcomputer.get_start(), 2)

    def test_basic_run_5(self):
        intcomputer = Intcomputer([1,1,1,4,99,5,6,0,99])
        intcomputer.run()
        self.assertEqual(intcomputer.get_start(), 30)

    def test_input_output(self):
        output = []
        intcomputer = Intcomputer([3,0,4,0,99])
        intcomputer.run(input=[3], output=output)
        self.assertEqual(output[-1], 3)
    
    def test_parameter_value_mode(self):
        intcomputer = Intcomputer([1002,4,3,4,33])
        intcomputer.run()
        self.assertEqual(intcomputer._memory, [1002, 4, 3, 4, 99])
    
    def test_negative(self):
        intcomputer = Intcomputer([1101,100,-1,4,0])
        intcomputer.run()
        self.assertEqual(intcomputer._memory, [1101, 100, -1, 4, 99])
    
    def test_comparision_1(self):
        output = []
        input = [3,9,8,9,10,9,4,9,99,-1,8]
        intcomputer = Intcomputer(input)
        intcomputer.run(input=[3], output=output)
        self.assertEqual(0, output[-1])
        intcomputer = Intcomputer(input)
        intcomputer.run(input=[8], output=output)
        self.assertEqual(1, output[-1])
    
    def test_comparision_2(self):
        output = []
        input = [3,9,7,9,10,9,4,9,99,-1,8]
        intcomputer = Intcomputer(input)
        intcomputer.run(input=[8], output=output)
        self.assertEqual(0, output[-1])

        intcomputer = Intcomputer(input)
        intcomputer.run(input=[7], output=output)
        self.assertEqual(1, output[-1])
        
        intcomputer = Intcomputer(input)
        intcomputer.run(input=[9], output=output)
        self.assertEqual(0, output[-1])
    
    def test_comparision_3(self):
        output = []
        input = [3,3,1108,-1,8,3,4,3,99]
        intcomputer = Intcomputer(input)
        intcomputer.run(input=[8], output=output)
        self.assertEqual(1, output[-1])

        intcomputer = Intcomputer(input)
        intcomputer.run(input=[0], output=output)
        self.assertEqual(0, output[-1])

    def test_comparision_4(self):
        output = []
        input = [3,3,1107,-1,8,3,4,3,99]
        intcomputer = Intcomputer(input)
        intcomputer.run(input=[8], output=output)
        self.assertEqual(0, output[-1])

        intcomputer = Intcomputer(input)
        intcomputer.run(input=[7], output=output)
        self.assertEqual(1, output[-1])

    def test_comparision_5(self):
        output = []
        input = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
        intcomputer = Intcomputer(input)
        intcomputer.run(input=[7], output=output)
        self.assertEqual(1, output[-1])

        intcomputer = Intcomputer(input)
        intcomputer.run(input=[0], output=output)
        self.assertEqual(0, output[-1])

    def test_comparision_6(self):
        output = []
        input = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
        intcomputer = Intcomputer(input)
        intcomputer.run(input=[0], output=output)
        self.assertEqual(0, output[-1])

        intcomputer = Intcomputer(input)
        intcomputer.run(input=[1], output=output)
        self.assertEqual(1, output[-1])

    def test_comparision_7(self):
        output = []
        input = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
        intcomputer = Intcomputer(input)
        intcomputer.run(input=[1], output=output)
        self.assertEqual(999, output[-1])

        intcomputer = Intcomputer(input)
        intcomputer.run(input=[8], output=output)
        self.assertEqual(1000, output[-1])

        intcomputer = Intcomputer(input)
        intcomputer.run(input=[9], output=output)
        self.assertEqual(1001, output[-1])

    def test_it_throws_on_not_enough_input_and_continues_when_input_is_provided(self):
        output = []
        intcomputer = Intcomputer([3,0,4,0,99])
        with self.assertRaises(IndexError):
            intcomputer.run(input=[], output=output)

        intcomputer.run(input=[3], output=output)
        self.assertEqual(output[-1], 3)

    def test_it_handles_relative_mode(self):
        output = []
        input = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
        intcomputer = Intcomputer(input)
        intcomputer.run(output=output)
        self.assertEqual(output, input)

    def test_it_can_write_to_memory_outside(self):
        output = []
        intcomputer = Intcomputer([1102,34915192,34915192,7,4,7,99])
        intcomputer.run(output=output)
        self.assertEqual(output, [34915192*34915192])
    
    def test_it_can_read_from_memory_outside(self):
        output = []
        intcomputer = Intcomputer([101,34915192,100,7,4,7,99,0])
        intcomputer.run(output=output)
        self.assertEqual(output, [34915192])

    def test_it_handles_large_numbers(self):
        output = []
        intcomputer = Intcomputer([104,1125899906842624,99])
        intcomputer.run(output=output)
        self.assertEqual(output, [1125899906842624])

if __name__ == "__main__":
    unittest.main()