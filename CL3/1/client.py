import xmlrpc.client

# Connect to server
client = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Input from user
num = int(input("Enter a number: "))

# RPC call
result = client.factorial(num)

# Output result
print("Factorial is:", result)