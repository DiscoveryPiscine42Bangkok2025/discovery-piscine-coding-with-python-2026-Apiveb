#!/usr/bin/env python3

def main():
    input_number = int(input())
    if input_number > 0:
        print("This number is positive.")
    elif input_number < 0:
        print("This number is negative.")
    elif input_number == 0:
        print("This number is both positive and negative.")
    else :
        pass

main()