#!/usr/bin/env python3
import sys
'''
?> ./string_are_arrays.py | cat -e
none$
?> ./string_are_arrays.py "The character Z is not found in this string" | cat -e
none$
?> ./string_are_arrays.py "The character z is found in this string" | cat -e
z$
?> ./string_are_arrays.py "Zaz visits the zoo with Zazie" | cat -e
zzz$
'''

def main():
    if len(sys.argv) != 2:
        print("none")
    else:
        word = (sys.argv)[1]
        output = []
        for i in word:
            if i == "z":
                output.append(i)
            else:
                pass
        if output == []:
            print("none")
        else:
            print("".join(output))

main()