f = open("clean_weather.csv")

next(f)

out = open("mapper_output.txt", "w")

for line in f:

    try:
        date, mx, mn = line.strip().split(",")

        avg = (float(mx) + float(mn)) / 2

        out.write(f"{date}\t{avg}\n")

    except:
        pass

out.close()