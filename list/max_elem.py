arr=[1,4,2,6,3,7,5]
max=arr[0]
for i in range(1,len(arr)):
    if arr[i]>max:
        max=arr[i]
print("max elem in list",max)