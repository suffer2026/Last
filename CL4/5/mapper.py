import sys
import csv

reader = csv.reader(sys.stdin)

# Skip header
header = next(reader)

for row in reader:
    try:
        survived = row[1]
        pclass = row[2]
        sex = row[4]
        age = row[5]

        # Handle missing age
        if age == "":
            continue

        age = float(age)

        # Case 1: People who died -> calculate avg age
        if survived == "0":
            print(f"DIED\t{sex}\t{age}\t1")

        # Case 2: Survivors per class
        elif survived == "1":
            print(f"SURVIVED\t{pclass}\t1")

    except:
        continue
