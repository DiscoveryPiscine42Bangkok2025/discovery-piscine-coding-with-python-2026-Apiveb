#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) != 3:
        print("none")
    else:   
        output = []
        number = [int(i) for i in sys.argv[1:3]]
        for i in range(min(number), max(number)+1):
            output.append(int(i))
        print(output)

main()