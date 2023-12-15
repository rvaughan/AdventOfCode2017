#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 9 of the Advent of Code for 2019.
"""
import itertools
import sys


class Computer:
    def __init__(self, program, input_code) -> None:
        self.program = program
        self.memory = program[:] + ([0] * 1000)
        self.input_code = [input_code]
        self.output_code = 0
        self.inst_ptr = 0
        self.result = 0
        self.relative_base = 0

    def get_param(self, op, param_num, param):
        # print(f'   ? {op} {param_num} {param}')
        code = f'{op:05}'

        if param_num == 1:
            mode = code[2]
        elif param_num == 2:
            mode = code[1]
        else:
            mode = code[0]

        if mode == '0':
            # print(f'  pm {code} {param_num} {mode} - {self.memory[self.inst_ptr + param]}')
            return self.memory[param]

        if mode == '1':
            # print(f'  pm {code} {param_num} {mode} * {param}')
            return param
        
        print(f'  pm {code} {param_num} {mode} ^ {self.memory[self.relative_base + param]}')
        return self.memory[param + self.relative_base]

    def run_op(self):
        # print('--RUN')

        # Read the next 5 instructions for the program...
        digits = [x for x in self.memory[self.inst_ptr:self.inst_ptr+4]]
        if len(digits) < 2:
            self.result = 1
            return -1
        
        op = digits[0] % 100
        op_code = digits[0]
        # print(f'IP: {self.inst_ptr:03} [{len(self.memory)}], {op_code} {op}, {digits}')

        if op == 1:
            i1 = self.get_param(op_code, 1, self.memory[self.inst_ptr+1])
            i2 = self.get_param(op_code, 2, self.memory[self.inst_ptr+2])
            i3 = self.memory[self.inst_ptr+3]

            print(f'  ADD {i1} + {i2} = {i1+i2} -> {i3}')

            self.memory[i3] = i1 + i2

            # print('   ', self.memory)
            self.inst_ptr += 4
            return 0
        elif op == 2:
            i1 = self.get_param(op_code, 1, self.memory[self.inst_ptr+1])
            i2 = self.get_param(op_code, 2, self.memory[self.inst_ptr+2])
            i3 = self.memory[self.inst_ptr+3]

            print(f'  MULT {i1} * {i2} = {i1*i2} -> {i3}')

            self.memory[i3] = i1 * i2

            # print('    ', program)
            self.inst_ptr += 4
            return 0
        elif op == 3:
            # print('  SET')
            self.memory[self.inst_ptr+1] = self.input_code.pop()   # special input specified in puzzle
                                                                                # representing the system to be
                                                                                # diagnosed.

            self.inst_ptr += 2
            return 0
        elif op == 4:
            self.output_code = self.get_param(op_code, 1, self.memory[self.inst_ptr+1])
            
            print(f'  OUT {self.output_code}')

            self.inst_ptr += 2
            return 0
        elif op == 5:
            i1 = self.get_param(op_code, 1, self.memory[self.inst_ptr+1])
            i2 = self.get_param(op_code, 2, self.memory[self.inst_ptr+2])

            print(f'  jump-if-true {i1} {i2}')

            if i1 != 0:
                self.inst_ptr = i2
            else:
                self.inst_ptr += 3

            return 0
        elif op == 6:        
            i1 = self.get_param(op_code, 1, self.memory[self.inst_ptr+1])
            i2 = self.get_param(op_code, 2, self.memory[self.inst_ptr+2])

            print(f'  jump-if-false {i1} {i2}')

            if i1 == 0:
                self.inst_ptr = i2
            else:
                self.inst_ptr += 3

            return 0
        elif op == 7:
            i1 = self.get_param(op_code, 1, self.memory[self.inst_ptr+1])
            i2 = self.get_param(op_code, 2, self.memory[self.inst_ptr+2])
            i3 = self.memory[self.inst_ptr+3]

            print(f'  LESS {i1} {i2} -> {i3}')

            self.memory[i3] = 1 if i1 < i2 else 0

            self.inst_ptr += 4
            return 0
        elif op == 8:
            i1 = self.get_param(op_code, 1, self.memory[self.inst_ptr+1])
            i2 = self.get_param(op_code, 2, self.memory[self.inst_ptr+2])
            i3 = self.memory[self.inst_ptr+3]

            # print(f'  EQUAL {i1} {i2}')

            self.memory[i3] = 1 if i1 == i2 else 0

            self.inst_ptr += 4
            return 0
        elif op == 9:
            self.relative_base += self.memory[self.memory[self.inst_ptr+1]]
            # print(f'  SETREL {self.relative_base}')

            self.inst_ptr += 2
            return 0
        elif op == 99:
            # print('  END')
            self.inst_ptr += 1
            self.result = 1
            return 1
        else:
            # print('  ???')
            self.inst_ptr += 1
            self.result = -1
            return -1

    def errored(self):
        return self.result == -1
    
    def halted(self):
        return self.result != 0
    
    def set_input(self, input_value):
        self.input_code = [input_value] + self.input_code

    def run_program(self):
        self.output_code = None
        result = 0
        while not self.halted() and self.output_code is None and result != -1:
            result = self.run_op()
        
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
    
    result = []
    last_output = 0
    while all(not program.halted() for program in programs):
        for program in programs:
            program.set_input(last_output)
            last_output = program.run_program()
            if program.errored():
                print('eeee')
                break
            if not program.halted():
                result.append(last_output)

    if result != expected_solution:
        print("Test FAILED. Got a result of {}, not {}".format(result, expected_solution))
        sys.exit(-1)

    print("Test passed.".format(program_code))

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

# run_test([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99], [0], [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99])

# run_test([1102,34915192,34915192,7,4,7,99,0], [0], [1219070632396864])

# run_test([104,1125899906842624,99], [0], [1125899906842624])

# print("")
# print("-----------------")
# print("All Tests PASSED.")
# print("-----------------")
# print("")

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    program_code = [int(x) for x in f.readline().split(',')]

    programs = []
    # Create the program, and set it to test mode.
    for amp in [1]:
        programs.append(Computer(program_code[:], amp))
    
    result = []
    last_output = 0
    while all(not program.halted() for program in programs):
        for program in programs:
            program.set_input(last_output)
            last_output = program.run_program()
            if program.errored():
                print('eeee')
                break
            if not program.halted():
                result.append(last_output)

    print('Solution:', result)
