#!/usr/bin/env python3
import sys
import re
'''
./scan_it.py | cat -e
none$
./scan_it.py "the" | cat -e
none$
./scan_it.py "the" "the quick brown fox jumps over the lazy dog" | cat -e
2$
?>
'''

def main():
    if len(sys.argv) <= 2:
        print("none")
    else:
        finding = sys.argv[1]
        word = sys.argv[2]

        all = re.findall(finding, word)

        if len(all) == 0:
            print("none")
        else:
            print(len(all))

main()
