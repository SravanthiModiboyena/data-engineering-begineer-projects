#!/usr/bin/env python3
import sys
from collections import defaultdict

# Dictionary to store word counts
word_count = defaultdict(int)

# Read input from mapper (STDIN)
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t')
    word_count[word] += int(count)

# Print final counts
for word, count in word_count.items():
    print(f"{word}\t{count}")

