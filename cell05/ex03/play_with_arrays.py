#!/usr/bin/env python3

#./play_with_arrays.py

def main():
    origin = [2, 8, 9, 48, 8, 22, -12, 2]
    new_arr = []
    for i in origin:
        if i > 5 and i + 2 not in new_arr:
            new_arr.append(i+2)
    print(origin)
    print(new_arr)

main()
