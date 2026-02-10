#!/usr/bin/env python3
import sys
'''
?> ./aff_rev_params.py | cat -e
none$
?> ./aff_rev_params.py "coucou" | cat -e
none$
?> ./aff_rev_params.py "Python" "piscine" "hello" | cat -e
hello$
piscine$
Python$
?>
'''

def main():
    if len(sys.argv) <= 2:
        print("none")
    else:
        for i in range(len(sys.argv)-1, 0, -1):
            print(sys.argv[i])

main()