#!/usr/bin/env python

import sys


NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)


def find_start(maze):
    for idx in xrange(len(maze[0])):
        if maze[0][idx] == "|":
            return 0, idx

    return -1, -1


def process_maze(maze):
    path = ""
    cur_x, cur_y = find_start(maze)
    direction = SOUTH

    while True:
        if maze[cur_x][cur_y] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            path += maze[cur_x][cur_y]
        elif maze[cur_x][cur_y] in '+':
            if direction != EAST and maze[cur_x][cur_y-1] != " ":
                direction = WEST
            elif direction != WEST and maze[cur_x][cur_y+1] != " ":
                direction = EAST
            elif direction != NORTH and maze[cur_x+1][cur_y] != " ":
                direction = SOUTH
            elif direction != SOUTH and maze[cur_x-1][cur_y] != " ":
                direction = NORTH
            else:
                break
        elif maze[cur_x][cur_y] == ' ':
            break

        cur_x += direction[0]
        cur_y += direction[1]

    return path


# Tests go here


with open("test_input.txt", "r") as f:
    maze = []
    lines = f.readlines()
    for line in lines:
        maze.append(" " + line.strip("\n") + " ")
    maze.append([" "] * len(maze[0]))

    path = process_maze(maze)

    if path != "ABCDEF":
        print 'Wrong path. {0}'.format(path)
        sys.exit(-1)

print "All Tests passed."


# All tests complete


with open("input.txt", "r") as f:
    maze = []
    lines = f.readlines()
    for line in lines:
        maze.append(" " + line.strip("\n") + " ")
    maze.append([" "] * len(maze[0]))

    path = process_maze(maze)

    print path
