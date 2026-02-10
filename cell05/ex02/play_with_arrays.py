#!/usr/bin/env python3

def main():
    origin = [2, 8, 9, 48, 8, 22, -12, 2]
    new_arr = []
    for i in origin:
        if i > 5:
            new_arr.append(i+2)
    print(origin)
    print(new_arr)

main()
