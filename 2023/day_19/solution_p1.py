#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 19 of the Advent of Code for 2023.
"""
import sys


def calculate_solution(items):
    workflows = {}
    for idx in range(len(items)):
        item = items[idx]
        
        if item == '':
            break

        w_id, wf = item.split('{')
        workflows[w_id] = wf[:-1]

    accepted = []
    for idx in range(idx+1, len(items)):
        item = items[idx]

        p_x, p_m, p_a, p_s = item[1:-1].split(',')
        p_x = int(p_x[2:])
        p_m = int(p_m[2:])
        p_a = int(p_a[2:])
        p_s = int(p_s[2:])

        p = {
            'x': p_x,
            'm': p_m,
            'a': p_a,
            's': p_s
        }

        cur_wf = 'in'
        evaluating = True
        while evaluating:
            if cur_wf == 'R':
                evaluating = False
                continue

            if cur_wf == 'A':
                accepted.append(p)
                evaluating = False
                continue

            workflow = workflows[cur_wf]
            parts = workflow.split(',')
            for part in parts:
                if '<' in part:
                    val, next_wf = part.split(':')
                    if p[val[0]] < int(val[2:]):
                        cur_wf = next_wf
                        break
                elif '>' in part:
                    val, next_wf = part.split(':')
                    if p[val[0]] > int(val[2:]):
                        cur_wf = next_wf
                        break
                elif '==' in part:
                    val, next_wf = part.split(':')
                    if p[val[0]] == int(val[2:]):
                        cur_wf = next_wf
                        break
                else:
                    cur_wf = part

    result = 0

    for part in accepted:
        result += (part['x'] + part['m'] + part['a'] + part['s'])

    return result


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input.split('\n'))

    if result != expected_solution:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_list = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""
result = run_test(test_list, 19114)

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
