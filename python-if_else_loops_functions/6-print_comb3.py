#!/usr/bin/python3

for x in range(0, 9):
    for y in range(x + 1, 10):
        print("{:02d}".format(x * 10 + y), end=", ")
