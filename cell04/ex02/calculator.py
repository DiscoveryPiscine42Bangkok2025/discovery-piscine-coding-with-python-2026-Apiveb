#!/usr/bin/env python3

def main():
    first = int(input("Give me your first number: "))
    second = int(input("Give me your second number: "))
    print("Thank You!")
    print(f"{first} + {second} = {first+second}")
    print(f"{first} - {second} = {first-second}")

    if second == 0:
        print(f"{first} / {second} = Undefined.")
    else:
        print(f"{first} / {second} = {(first/second):g}")

    print(f"{first} * {second} = {first*second}")

main()