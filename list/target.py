arr = [1, 2, 3, 7, 5]
target = 12
sum = 0
s = 0
for e in range(len(arr)):
    sum += arr[e]
    while sum > target and s <= e:
        sum -= arr[s]
        s += 1
    if sum == target:
        print(s + 1, e + 1)  
        break
else:
    print("No subarray found")