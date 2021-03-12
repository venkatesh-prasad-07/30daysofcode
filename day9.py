#!/bin/python3
#recursion
import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    if n == 0:
        fact = 1
        return fact
    
    else:
        fact = 1
        while n > 1:
            fact =  n *  fact 
            n = n-1
    return fact

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
