import sys

died_data = {}        # {sex: [total_age, count]}
survived_data = {}    # {class: count}

for line in sys.stdin:
    parts = line.strip().split("\t")

    if parts[0] == "DIED":
        sex = parts[1]
        age = float(parts[2])
        cnt = int(parts[3])

        if sex not in died_data:
            died_data[sex] = [0, 0]

        died_data[sex][0] += age
        died_data[sex][1] += cnt

    elif parts[0] == "SURVIVED":
        pclass = parts[1]
        cnt = int(parts[2])

        if pclass not in survived_data:
            survived_data[pclass] = 0

        survived_data[pclass] += cnt


# 🔹 Final Output

# Average age of dead
for sex in died_data:
    total_age, count = died_data[sex]
    avg = total_age / count
    print(f"DIED_{sex}\tAverage Age: {avg:.2f}")

# Survivors per class
for pclass in survived_data:
    print(f"SURVIVED_CLASS_{pclass}\tSurvivors: {survived_data[pclass]}")
