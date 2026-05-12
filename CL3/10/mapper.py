import sys

# Skip header
next(sys.stdin)

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    try:
        date, max_temp, min_temp = line.split(',')
        max_temp = float(max_temp)
        min_temp = float(min_temp)
        avg_temp = (min_temp + max_temp)/2     
        print(f"{date}\t{avg_temp}")
    except:
        continue
