import sys
from collections import defaultdict

current_key = None
values_M = []
values_N = []

def compute_result(key, values_M, values_N):
    result = 0
    dict_M = {j: val for j, val in values_M}
    dict_N = {j: val for j, val in values_N}
    
    for j in dict_M:
        if j in dict_N:
            result += dict_M[j] * dict_N[j]
    
    print(f"{key}\t{result}")

for line in sys.stdin:
    line = line.strip()
    key, value = line.split("\t")
    
    matrix, j, val = value.split(",")
    j = int(j)
    val = float(val)

    if key != current_key and current_key is not None:
        compute_result(current_key, values_M, values_N)
        values_M = []
        values_N = []

    current_key = key

    if matrix == "M":
        values_M.append((j, val))
    else:
        values_N.append((j, val))

if current_key:
    compute_result(current_key, values_M, values_N)
