#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 15 of the Advent of Code for 2022.
"""
import sys


def build_grid(sensor_deetz):
    sensors = set()
    beacons = set()

    min_x = 1000000
    min_y = 1000000
    max_x = 0
    max_y = 0

    max_distance = 0

    for sensor in sensor_deetz:
        data = sensor.split(' ')

        s_x = int(data[2].split('=')[1].replace(',', ''))
        s_y = int(data[3].split('=')[1].replace(':', ''))

        b_x = int(data[8].split('=')[1].replace(',', ''))
        b_y = int(data[9].split('=')[1].replace(':', ''))
        beacons.add((b_x, b_y))

        # Manhatten distance from the beacon to the sensor.
        distance = abs(s_x - b_x) + abs(s_y - b_y)
        sensors.add((s_x, s_y, distance))

        min_x = min(min_x, s_x)
        min_x = min(min_x, b_x)
        max_x = max(max_x, s_x)
        max_x = max(max_x, b_x)

        min_y = min(min_y, s_y)
        min_y = min(min_y, b_y)
        max_y = max(max_y, s_y)
        max_y = max(max_y, b_y)

        max_distance = max(max_distance, distance)

    # Sensor must be one position past the current max distance.
    max_distance += 1

    return sensors, beacons, min_x - max_distance, max_x + max_distance, min_y - max_distance, max_y + max_distance


def in_range(x, y, sensors):
    # Check to see if the co-ordinate is in range of any of the sensors...
    for (sx, sy, d) in sensors:
        # Manhatten distance from the co-ordinate to the sensor.
        distance = abs(x - sx) + abs(y - sy)
        if distance <= d:
            return False

    return True


def calculate_solution(details, max_distance):
    sensors, beacons, min_x, max_x, min_y, max_y = build_grid(details)

    result = 0
    found = False
    # Check the distance from each of the sensors.
    for (sensor_x, sensor_y, distance) in sensors:
        if found:
            # Stop if we think we've found the solution.
            break

        # check all points that are d+1 away from the sensor position.
        for dist_x in range(distance + 2):
            if found:
                # Stop if we think we've found the solution.
                break

            dist_y = (distance + 1) - dist_x

            for signx, signy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                x = sensor_x + (dist_x * signx)
                y = sensor_y + (dist_y * signy)

                if not (0 <= x <= max_distance and 0 <= y <= max_distance):
                    # Ignore anything outside of the specified bounds.
                    continue

                if in_range(x, y, sensors) and (not found):
                    # Should be the right solution.
                    result = x * 4000000 + y
                    found = True
                    break

    return result


def run_test(test_input, max_distance, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input.split('\n'), max_distance)

    if result != expected_solution:
        print(
            f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_list = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

result = run_test(test_list, 20, 56000011)

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input.txt', 'r') as f:
    input_data = [line.strip() for line in f]
    answer = calculate_solution(input_data, 4000000)

    print(f'Solution is {answer}')
