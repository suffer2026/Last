
import sys

for line in sys.stdin:
    line = line.strip()
    for ch in line:
        if ch.strip() != "":   
            print(f"{ch}\t1")
