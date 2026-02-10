#!/usr/bin/env python3
import sys
'''
 ./aff_first_param.py | cat -e
 ./aff_first_param.py "Code Ninja" "Numerique" "42" | cat -e
'''

def main():
    if len(sys.argv) <= 1:
        print("none")
    else:
        print(sys.argv[1])
    
main()
