#!/usr/bin/env python3

import sys
import random

def roll(n, r, modifier=0):
    results = (random.randint(1, r) for _ in range(n))
    return sum(results) + modifier

def main():
    pass

if __name__ == '__main__':
    main()
