N = int(input("How many students? "))

data = []

print("Enter name, marks:")
for i in range(N):
	data.append(input())
	
with open("input.txt", "w") as f:
	f.write("\n".join(data))
	

