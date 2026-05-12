data = {}

f = open("mapper_output.txt")

for line in f:

    date, temp = line.strip().split("\t")

    year = date.split("-")[0]

    temp = float(temp)

    if year not in data:
        data[year] = []

    data[year].append(temp)

avg = {y: sum(t)/len(t) for y,t in data.items()}

hot = max(avg, key=avg.get)
cool = min(avg, key=avg.get)

print("Hottest Year:", hot, "with Avg Temp:", avg[hot])

print("Coolest Year:", cool, "with Avg Temp:", avg[cool])