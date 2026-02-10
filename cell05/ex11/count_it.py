#!/usr/bin/env python3
import sys
import re
'''
./count_it.py | cat -e
none$

./count_it.py "Game" "of" "Thrones" | cat -e
parameters: 3$
Game: 4$
of: 2$
Thrones: 7$
'''

def main():
    if len(sys.argv) <= 1:
        print("none")
    else:
        print(f"parameters: {len(sys.argv) - 1}")
        for i in range(1, len(sys.argv)):
            print(f"{sys.argv[i]}: {len(sys.argv[i])}")
main()
