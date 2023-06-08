def binary_search(array, high, low, target):
    i = 1
    
    while low <= high:
        mid = low + (high - low) // 2

        print(f"Comparison {i}:")
        print(f"low: {low}, array[{low}]: {array[low]}")
        print(f"high: {high}, array[{high}]: {array[high - 1]}")
        print()

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
        
        i = i + 1

    return -1

array = [1.5,1.75,2.00,2.25,2.50,2.75,3.00,4.00,5.00]
high = len(array) - 1
low = 0
target = 2.00

result = binary_search(array, high, low, target)

if result != -1:
    print(f"Index: {result}")
else:
    print("Element not found")