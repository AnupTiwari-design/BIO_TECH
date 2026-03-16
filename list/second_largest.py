arr = [10, 5, 20, 8, 15]
largest = second = float('-inf')
for x in arr:
    if x > largest:
        second = largest
        largest = x
    elif x > second and x != largest:
        second = x

print(second)
