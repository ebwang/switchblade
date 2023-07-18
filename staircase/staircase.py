#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#
# This will print in below format
#    #
#   ##
#  ###

def staircase(num_stairs):
    n = num_stairs - 2
    for stairs in range(1, num_stairs):
        print(' ' * n, '#' * stairs)
        n -= 1
    print('#' * num_stairs)
    
    
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)