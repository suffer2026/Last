import sys

current_grade = None
students = []

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    grade, data = line.split('\t')

    if current_grade == grade:
        students.append(data)
    else:
        if current_grade:
            print(f"{current_grade}: {', '.join(students)}")
        current_grade = grade
        students = [data]

# Print last grade group
if current_grade:
    print(f"{current_grade}: {', '.join(students)}")
