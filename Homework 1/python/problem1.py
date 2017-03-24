"""
problem1.py
Written By: Devon Bray for CS2223

prints the amount of time it takes to calculate different orders of loops in ms

To run linear test: python problem1.py 1
To run quadratic test: python problem1.py 2
To run cubic test: python problem1.py 3
"""

from timeit import timeit
import sys

n = 10000


def linear():
    for x in range(n):
        pass


def quadratic():
    for x in range(n):
        for y in range(n):
            pass


def cubic():
    for x in range(n):
        for y in range(n):
            for z in range(n):
                pass


if __name__ == "__main__":

    if len(sys.argv) > 2:
        print("Bad input, too many args")
        exit()

    user_in = sys.argv[1]

    k = None

    try:
        k = int(user_in)
    except ValueError:
        print("Bad input, bad number")
        exit()

    if k is 1:
        execution_time = (timeit(linear, number=1) * 1000000)
        print("Linear Took: " + str(execution_time) + "ms")
    elif k is 2:
        execution_time = (timeit(quadratic, number=1) * 1000000)
        print("Quadratic Took: " + str(execution_time) + "ms")
    elif k is 3:
        execution_time = (timeit(cubic, number=1) * 1000000)
        print("Cubic Took: " + str(execution_time) + "ms")
    else:
        print("bad argument")
