#!/usr/bin/env python3
import sys

'''
./parameter_matching.py
none

./parameter_matching.py "Hello"
What was the parameter? Bonjour
Nope, sorry...

./parameter_matching.py "Hello"
What was the parameter? Hello
Good job!

'''

def main():
    if len(sys.argv) != 2:
        print("none")
    else:
        check = input("What was the parameter? ")
        if check == sys.argv[1]:
            print("Good job!")
        else:
            print("Nope, sorry...")
main()
