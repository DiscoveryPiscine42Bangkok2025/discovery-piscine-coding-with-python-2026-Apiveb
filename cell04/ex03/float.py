#!/usr/bin/env python3

def main():
    num = float(input("Give me a number: "))
    if num.is_integer():
        print("This number is integer.")
    else:
        print("This number is decimal.")
    
main()