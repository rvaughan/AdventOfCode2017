#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 20 of the Advent of Code for 2023.
"""
import sys


class Circuit():
    def __init__(self) -> None:
        self.low_pulses = 0
        self.high_pulses = 0

    def pulses(self):
        return self.low_pulses, self.high_pulses


class Broadcaster(Circuit):
    def __init__(self, name, triggers) -> None:
        Circuit.__init__(self)
        self.name = name
        self.targets = triggers.split(', ')

    def add_orinator(self, name):
        pass

    def connect(self, circuits):
        for target in self.targets:
            t = circuits[target]
            t.add_orinator(self.name)

    def trigger(self, pulse, circuits, _originator):
        next_t = []

        for target in self.targets:
            print(_originator, self.name, pulse, target)

            if pulse == 0:
                self.low_pulses += 1
            else:
                self.high_pulses += 1
            
            # print(self.low_pulses, self.high_pulses, target, pulse, circuits[target].targets)

            next_t.append((target, pulse, self.name))

        return next_t


class FlipFlop(Circuit):
    def __init__(self, name, triggers) -> None:
        Circuit.__init__(self)
        self.name = name
        self.targets = triggers.split(', ')
        self.mode = 0

    def add_orinator(self, name):
        pass

    def connect(self, circuits):
        for target in self.targets:
            t = circuits[target]
            t.add_orinator(self.name)

    def trigger(self, pulse, circuits, _originator):
        next_t = []

        if pulse == 0:
            self.mode = 0 if self.mode == 1 else 1

            for target in self.targets:
                print(_originator, self.name, self.mode, target)

                if self.mode == 0:
                    self.low_pulses += 1
                else:
                    self.high_pulses += 1
                
                # print(self.low_pulses, self.high_pulses, target, pulse, circuits[target].targets)

                next_t.append((target, self.mode, self.name))

        return next_t


class Conjunction(Circuit):
    def __init__(self, name, triggers) -> None:
        Circuit.__init__(self)
        self.name = name
        self.targets = triggers.split(', ')
        self.originators = {}

    def add_orinator(self, name):
        self.originators[name] = 0

    def connect(self, circuits):
        for target in self.targets:
            t = circuits[target]
            t.add_orinator(self.name)

    def trigger(self, pulse, circuits, _originator):
        next_t = []

        self.originators[_originator] = pulse

        triggered = True
        for originator in self.originators:
            if self.originators[originator] != pulse:
                triggered = False
                break
        
        if triggered:
            pulse = 0 if pulse == 1 else 1

            for target in self.targets:
                print(_originator, self.name, pulse, target)

                if pulse == 0:
                    self.low_pulses += 1
                else:
                    self.high_pulses += 1
                
                # print(self.low_pulses, self.high_pulses, target, pulse, circuits[target].targets)

                next_t.append((target, pulse, self.name))

        return next_t


class Button(Circuit):
    def __init__(self, name, triggers) -> None:
        Circuit.__init__(self)
        self.name = name
        self.targets = triggers.split(', ')

    def add_orinator(self, name):
        pass

    def connect(self, circuits):
        for target in self.targets:
            t = circuits[target]
            t.add_orinator(self.name)

    def trigger(self, pulse, circuits, _originator):
        next_t = []

        for target in self.targets:
            print(_originator, self.name, pulse, target)

            self.low_pulses += 1

            next_t.append((target, pulse, self.name))

        return next_t


class Dummy(Circuit):
    def __init__(self, name, triggers) -> None:
        Circuit.__init__(self)
        self.name = name
        self.targets = triggers.split(', ')

    def add_orinator(self, name):
        pass

    def connect(self, circuits):
        pass

    def trigger(self, pulse, circuits, _originator):
        return []


def calculate_solution(items, iterations=1):
    circuits = {}

    for row in items:
        parts = row.split(' -> ')

        if parts[0].startswith('b'):
            bcast = Broadcaster(parts[0], parts[1])
            circuits[parts[0]] = bcast
        elif parts[0].startswith('%'):
            ff = FlipFlop(parts[0][1:], parts[1])
            circuits[parts[0][1:]] = ff
        elif parts[0].startswith('&'):
            con = Conjunction(parts[0][1:], parts[1])
            circuits[parts[0][1:]] = con
        else:
            d = Dummy(parts[0][1:], parts[1])
            circuits[parts[0][1:]] = d

    circuits['button'] = Button('button', 'broadcaster')

    circuits['output'] = Dummy('output', '')

    for circuit in circuits:
        circuits[circuit].connect(circuits)

    for _ in range(iterations):
        triggers = [('button', 0, None)]

        while any(triggers):
            trigger, pulse, originator = triggers.pop(0)
            # print(trigger, pulse)
            if trigger in circuits:
                t = circuits[trigger]
                next_t = t.trigger(pulse, circuits, originator)
                for nt in next_t:
                    triggers.append(nt)

    low_pulses = 0
    high_pulses = 0

    for circuit in circuits:
        low, high = circuits[circuit].pulses()
        low_pulses += low
        high_pulses += high

    # print(low_pulses, high_pulses)

    return low_pulses * high_pulses


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input.split('\n'))

    print()
    if result != expected_solution:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

# test_list = """broadcaster -> a, b, c
# %a -> b
# %b -> c
# %c -> inv
# &inv -> a"""
# result = run_test(test_list, 32000000)

test_list = """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""
result = run_test(test_list, 11687500)

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input.txt', 'r') as f:
    input_data = [line.strip() for line in f]
    answer = calculate_solution(input_data)

    print(f'Solution is {answer}')
