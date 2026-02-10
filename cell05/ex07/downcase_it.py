#!/usr/bin/env python3
import sys
'''
?> ./downcase_it.py | cat -e
none$
?> ./downcase_it.py "LUCIOLE" | cat -e
luciole$
?> ./downcase_it.py 'This exercise is quite easy!' | cat -e
this exercise is quite easy!$
'''


def main():
    if len(sys.argv) != 2:
        print("none")   
    else:
        print(sys.argv[1].lower())
main()
