arr = [1, 2, 2, 3, 1, 2, 4]

freq = {}

for x in arr:
    freq[x] = freq.get(x, 0) + 1

print(freq)