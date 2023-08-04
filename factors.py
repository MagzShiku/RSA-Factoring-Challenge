#!/usr/bin/python3

import sys

def factorize(n):
    """
    Given an integer n, find two factors p and q such that n=p*q.
    """
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            return i, int(n/i)
    return None

if __name__ == '__main__':
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            for line in f:
                num = int(line.strip())
                factors = factorize(num)
                print(f"{num}={factors[0]}*{factors[1]}")
    else:
        print("Usage: factors <file>")

