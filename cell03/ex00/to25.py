#!/usr/bin/env python3

def main():
    loop_num = int(input("Enter a number less than 25\n"))
    if loop_num > 25:
        print("Error")
    else:
        while loop_num <= 25:
            print(f"Inside the loop, my variable is {loop_num}")
            loop_num += 1

main()