import sys

for line in sys.stdin:
    line = line.strip()
    
    words = line.split()
    
    for word in words:
        word = word.strip().upper()
        print(f"{word}\t1")
