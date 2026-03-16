#1. Start with low = 0 and high = n-1
#2. Find middle element
#3. If key == middle → found
#4. If key < middle → search left
#5. If key > middle → search right
class BinarySearch:
    def search(self, arr, key):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == key:
                return mid
            elif arr[mid] < key:
                low = mid + 1
            else:
                high = mid - 1

        return -1


arr = [2,4,6,8,10,12]

b = BinarySearch()

result = b.search(arr, 8)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")