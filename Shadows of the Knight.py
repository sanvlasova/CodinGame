https://www.codingame.com/ide/puzzle/shadows-of-the-knight-episode-1

import sys
import math

w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x, y = [int(i) for i in input().split()]
first_x = 0
last_x = w
first_y = 0
last_y = h

# game loop
while True:
    # the direction of the bombs from batman's current location:
    # U, UR, R, DR, D, DL, L or UL
    direction = input()
    if 'U' in direction:
        last_y = y - 1
    elif 'D' in direction:
        first_y = y + 1
    if 'L' in direction:
        last_x = x - 1
    elif 'R' in direction:
        first_x = x + 1
    x = (first_x + last_x) // 2
    y = (first_y + last_y) // 2
    print("{} {}".format(x, y)) 
