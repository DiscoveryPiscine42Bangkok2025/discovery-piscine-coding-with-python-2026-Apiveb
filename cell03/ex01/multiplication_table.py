#!/usr/bin/env python3

def main():
    multi_num = int(input("Enter a number\n"))
    for i in range(0, 10):
        print(f"{i} x {multi_num} = {i*multi_num}")

main()