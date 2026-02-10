#!/usr/bin/env python3

def main():
    i = 0
    j = 0
    while i <= 10:
        multi_table = f"Table de {i}:"
        j = 0
        while j <= 10:
            multi_table += " " + str(i*j)
            j += 1
        print(multi_table)
        i += 1

main()