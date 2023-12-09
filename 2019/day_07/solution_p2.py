#!/usr/bin/env python
"""
This code holds the solution for part  of day 7 of the Advent of Code for 2019.
"""
import itertools
import sys

class Computer:
    def __init__(self, program, input_code) -> None:
        self.program = program
        self.input_code = [input_code]
        self.output_code = 0
        self.inst_ptr = 0
        self.result = 0

    def run_op(self, program, inst_ptr):
        # print("IP: {} [{}]".format(inst_ptr, len(program)))
        digits = [int(x) for x in str(program[inst_ptr])]
        op = (0 if len(digits) == 1 else digits[-2]) * 10+digits[-1]
        # print(inst_ptr, op)
        digits = digits[:-2]

        if op == 1:
            # print('add', program)
            while (len(digits) < 3):
                digits = [0] + digits

            i1, i2, i3 = program[inst_ptr+1], program[inst_ptr+2], program[inst_ptr+3]
            # print(i2, i2, i3, digits[2], digits[1], program[i1], program[i2])
            program[i3] = (i1 if digits[2] == 1 else program[i1]) + (i2 if digits[1] == 1 else program[i2])

            # print('   ', program)
            return 0, program, inst_ptr + 4
        elif op == 2:
            # print('mult')

            while (len(digits) < 3):
                digits = [0] + digits

            i1,i2,i3 = program[inst_ptr+1], program[inst_ptr+2], program[inst_ptr+3]
            program[i3] = (i1 if digits[2] == 1 else program[i1]) * (i2 if digits[1] == 1 else program[i2])

            # print('    ', program)
            return 0, program, inst_ptr + 4
        elif op == 3:
            # print('set')
            program[program[inst_ptr+1]] = self.input_code.pop()  # special input specified in puzzle
                                                            # representing the system to be
                                                            # diagnosed.

            return 0, program, inst_ptr + 2
        elif op == 4:
            # print('output')
            # print(f'output: {program[program[inst_ptr+1]]}')
            self.output_code = program[program[inst_ptr+1]]

            return 0, program, inst_ptr + 2
        elif op == 5:
            # print('jump-if-true')
            while (len(digits) < 3):
                digits = [0] + digits

            i1, i2 = program[inst_ptr+1], program[inst_ptr+2]
            val = (i1 if digits[2] == 1 else program[i1])
            if val != 0:
                inst_ptr = (i2 if digits[1] == 1 else program[i2])
            else:
                inst_ptr += 3

            return 0, program, inst_ptr
        elif op == 6:
            # print('jump-if-false')
            while (len(digits) < 3):
                digits = [0] + digits

            i1, i2 = program[inst_ptr+1], program[inst_ptr+2]
            val = (i1 if digits[2] == 1 else program[i1])
            if val == 0:
                inst_ptr = (i2 if digits[1] == 1 else program[i2])
            else:
                inst_ptr += 3

            return 0, program, inst_ptr
        elif op == 7:
            # print('less than')
            while (len(digits) < 3):
                digits = [0] + digits

            i1, i2, i3 = program[inst_ptr+1], program[inst_ptr+2], program[inst_ptr+3]
            p1 = (i1 if digits[2] == 1 else program[i1])
            p2 = (i2 if digits[1] == 1 else program[i2])
            p3 = (i3 if digits[0] == 1 else program[i3])

            if p1 < p2:
                program[i3] = 1
            else:
                program[i3] = 0

            return 0, program, inst_ptr + 4
        elif op == 8:
            # print('equals')
            while (len(digits) < 3):
                digits = [0] + digits

            i1, i2, i3 = program[inst_ptr+1], program[inst_ptr+2], program[inst_ptr+3]
            p1 = (i1 if digits[2] == 1 else program[i1])
            p2 = (i2 if digits[1] == 1 else program[i2])
            p3 = (i3 if digits[0] == 1 else program[i3])

            # print('==', i1, i2, i3, p1, p2, p3)

            program[i3] = 1 if p1 == p2 else 0

            return 0, program, inst_ptr + 4
        elif op == 99:
            # print('end')
            return 1, program, inst_ptr + 1
        else:
            # print('???')
            return -1, program, inst_ptr + 1

    def halted(self):
        return self.result == 1
    
    def set_input(self, input_value):
        self.input_code = [input_value] + self.input_code

    def run_program(self):
        # print('-->', self.input_code, self.output_code, self.halted(), self.inst_ptr, self.program[self.inst_ptr:])
        self.output_code = None
        while not self.halted() and self.output_code is None:
            self.result, self.program, self.inst_ptr = self.run_op(self.program, self.inst_ptr)
        
        # print('<--', self.input_code, self.output_code, self.halted(), self.inst_ptr, self.program[self.inst_ptr:])
        
        return self.output_code


def run_test(program_code, amplifier_values, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    print(f'Verifying: {program_code}')

    result = 0
    programs = []
    for amp in amplifier_values:
        programs.append(Computer(program_code[:], amp))
    
    last_output = 0
    while all(not program.halted() for program in programs):
        for program in programs:
            program.set_input(last_output)
            output = program.run_program()
            if not program.halted():
                last_output = output

    result = max(result, last_output)

    if result != expected_solution:
        print("Test FAILED. Got a result of {}, not {}".format(result, expected_solution))
        sys.exit(-1)

    print("Test passed.".format(program_code))

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

run_test([3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5], [9,8,7,6,5], 139629729)

run_test([3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10], [9,7,8,5,6], 18216)

print("")
print("-----------------")
print("All Tests PASSED.")
print("-----------------")
print("")

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    program_code = [int(x) for x in f.readline().split(',')]

    result = 0
    inputs = [5, 6, 7, 8, 9]
    for combination in itertools.permutations(inputs):
        programs = []
        for amp in combination:
            programs.append(Computer(program_code[:], amp))
        
        last_output = 0
        while all(not program.halted() for program in programs):
            for program in programs:
                program.set_input(last_output)
                output = program.run_program()
                if not program.halted():
                    last_output = output

        result = max(result, last_output)

    # 18464004 is wrong
    print('Solution:', result)
