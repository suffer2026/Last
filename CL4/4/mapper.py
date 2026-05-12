import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    name, marks = line.split(",")
    marks = int(marks)

    # Assign grade
    if marks >= 90:
        grade = 'A'
    elif marks >= 75:
        grade = 'B'
    elif marks >= 60:
        grade = 'C'
    elif marks >= 50:
        grade = 'D'
    else:
        grade = 'F'

    # Output: grade as key
    print(f"{grade}\t{name}({marks})")
