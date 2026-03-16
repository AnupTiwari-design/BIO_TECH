list = []

size = int(input("Enter the size = "))
print("Enter list elements:")
for i in range(size):
    list.append(int(input()))

pos = int(input("Enter position to insert (1 to {size+1}): "))
element = int(input("Enter element to insert: "))

# Add extra space at end
list.append(0)

# Shift elements to the right
for i in range(len(list)-1, pos-1, -1):
    list[i] = list[i-1]

# Insert element
list[pos-1] = element

print("List after insertion:")
for x in list:
    print(x, end=" ")