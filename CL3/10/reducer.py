import sys

current_year = None
temps = []

hottest_year = None
coolest_year = None
max_temp = float('-inf')
min_temp = float('inf')

for line in sys.stdin:
    line = line.strip()
    date, temp = line.split('\t')
    temp = float(temp)
    
    year = int(date.split("-")[0])

    if current_year == year:
        temps.append(temp)
    else:
        if current_year:
            avg_temp = sum(temps) / len(temps)

            if avg_temp > max_temp:
                max_temp = avg_temp
                hottest_year = current_year

            if avg_temp < min_temp:
                min_temp = avg_temp
                coolest_year = current_year

        current_year = year
        temps = [temp]


if current_year:
    avg_temp = sum(temps) / len(temps)

    if avg_temp > max_temp:
        max_temp = avg_temp
        hottest_year = current_year

    if avg_temp < min_temp:
        min_temp = avg_temp
        coolest_year = current_year

print(f"Hottest Year: {hottest_year} with Avg Temp: {max_temp}")
print(f"Coolest Year: {coolest_year} with Avg Temp: {min_temp}")
