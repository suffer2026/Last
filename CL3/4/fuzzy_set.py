def get_fuzzy_set(name):
    s = {}
    n = int(input(f"How many elements in Fuzzy Set {name}? "))
    for _ in range(n):
        e = input("Element name: ")
        m = float(input(f"Membership of {e} (0-1): "))
        s[e] = m
    return s

def fuzzy_union(A, B):
    keys = set(A) | set(B)
    return {k: max(A.get(k, 0), B.get(k, 0)) for k in keys}

def fuzzy_intersection(A, B):
    keys = set(A) | set(B)
    return {k: min(A.get(k, 0), B.get(k, 0)) for k in keys}

def fuzzy_complement(A):
    return {k: round(1 - v, 2) for k, v in A.items()}

def fuzzy_difference(A, B):
    keys = set(A) | set(B)
    return {k: round(min(A.get(k, 0), 1 - B.get(k, 0)), 2) for k in keys}

def cartesian_product(A, B):
    return {(x, y): round(min(A[x], B[y]), 2) for x in A for y in B}

def max_min_composition(R, S, A_keys, B_keys):
    return {
        (x, z): round(max(min(R[(x, y)], S[(y, z)]) for y in B_keys), 2)
        for x in A_keys for z in A_keys
    }

def print_relation(name, rel, rows, cols):
    print(f"\n{name}:")
    print("     " + " ".join(f"{c:>6}" for c in cols))
    for r in rows:
        print(f"{r:>5}", end="")
        for c in cols:
            print(f"{rel[(r, c)]:>6}", end=" ")
        print()

print("FUZZY SET OPERATIONS")
A = get_fuzzy_set("A")
print("\n")
B = get_fuzzy_set("B")

print("\nA =", A)
print("B =", B)
print("Union =", fuzzy_union(A, B))
print("Intersection =", fuzzy_intersection(A, B))
print("Complement of A =", fuzzy_complement(A))
print("Difference (A-B) =", fuzzy_difference(A, B))

R = cartesian_product(A, B)
S = cartesian_product(B, A)
T = max_min_composition(R, S, list(A.keys()), list(B.keys()))

print_relation("\nRelation R = A x B", R, list(A.keys()), list(B.keys()))
print_relation("Relation S = B x A", S, list(B.keys()), list(A.keys()))
print_relation("Composition T = R o S", T, list(A.keys()), list(A.keys()))
