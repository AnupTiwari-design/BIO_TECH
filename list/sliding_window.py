arr = [2, 1, 5, 1, 3, 2]
k = 3

# Step 1: First window sum
window_sum = 0
for i in range(k):
    window_sum += arr[i]

max_sum = window_sum

# Step 2: Slide the window
for i in range(k, len(arr)):
    window_sum += arr[i]        # add next element
    window_sum -= arr[i - k]   # remove previous element
    
    if window_sum > max_sum:
        max_sum = window_sum

print("Maximum sum:", max_sum)