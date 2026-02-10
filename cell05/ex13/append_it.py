#!/usr/bin/env python3
import sys

'''
./append_it.py | cat -e
none$

./append_it.py "parallel" "egoism" "human" | cat -e
parallelism$
humanism
'''

def main():
    if len(sys.argv) <= 1:
        print("none")
    else:
        for i in range(1, len(sys.argv)):
            if sys.argv[i][-3:] != "ism":
                print(sys.argv[i]+"ism")
            else:
                pass
main()
