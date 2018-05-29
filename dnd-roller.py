#!/usr/bin/env python3

import re
import sys
import random

def roll(n, r, modifier=0):
    results = (random.randint(1, r) for _ in range(n))
    return sum(results) + modifier

def main():
    SEPARATOR = 'd'
    PROMPT = '> '
    while True:
        try:
            # Get input and ensure proper number of args
            inp = input(PROMPT).strip().lower().split()
            if len(inp) == 0 or len(inp) > 2:
                print('Invalid input: wrong number of args')
                continue

            # Get dice and ensure correct format of NdR
            dice = inp[0]
            match = re.match(r'\d+d\d+', dice)
            if match:
                n, r = (int(x) for x in dice.split(SEPARATOR))
            else:
                print('Invalid input: wrong dice format')
                continue


            # Get modifier and ensure correct format of +N, else modifier=0
            modifier = inp[1] if len(inp) > 1 else 0
            if modifier != 0:
                match = re.match(r'\+\d+', modifier)
                if match:
                    modifier = int(modifier.strip('+'))
                else:
                    print('Invalid input: wrong modifier format')

            # Get result and display
            result = roll(n, r, modifier=modifier)
            print(result)
        except KeyboardInterrupt:
            print('\nGoodbye!')
            sys.exit(0)




if __name__ == '__main__':
    main()
