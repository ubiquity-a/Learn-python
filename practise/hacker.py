'''n = int(input())
a = tuple(int(x) for x in range(1,n+1))
print(a)
print(hash(a))
'''
# Get the number of elements in the tuple
num_elements = int(input())

# Get the space-separated integers and convert them to a tuple
data_str = input()
data = tuple(map(int, data_str.split()))

# Calculate the product without using a function
product = 1
for num in data:
  product *= num


# Print the product
print(product)
   