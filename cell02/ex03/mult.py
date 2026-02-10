#!/usr/bin/env python3

def main():
    first_num = int(input("Enter the first number:\n"))
    second_num = int(input("Enter the second number:\n"))
    sumation = first_num * second_num
    if sumation > 0:
        print("The result is positive.")
    elif sumation < 0:
        print("The result is negative.")
    elif sumation == 0:
        print("The result is both positive and negative.")
    else:
        pass

main()