#!/usr/bin/env python3
import sys
'''
./parameters.py
./parameters.py "initiation"
./parameters.py "this" "is" "crazy" "there's" "everywhere!"
'''

def main():
    print(f"Number of Parameters: {len(sys.argv)-1}.")
    
main()
