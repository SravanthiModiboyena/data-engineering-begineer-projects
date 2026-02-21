#!/usr/bin/env python3
import sys

# Mapper reads each line from input (STDIN)
for line in sys.stdin:
    # Remove leading/trailing whitespace
    line = line.strip()
    # Split line into words
    words = line.split()
    # Output each word with a count of 1
    for word in words:
        print(f"{word}\t1")

