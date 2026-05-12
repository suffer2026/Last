import sys


num_cols_N = 2
num_rows_M = 2

for line in sys.stdin:
    line = line.strip()
    matrix, i, j, value = line.split(",")
    
    i = int(i)
    j = int(j)
    value = float(value)

    if matrix == "M":
        for k in range(num_cols_N):
            print(f"{i},{k}\tM,{j},{value}")
    
    elif matrix == "N":
        for i_val in range(num_rows_M):
            print(f"{i_val},{j}\tN,{i},{value}")
