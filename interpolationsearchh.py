def interpolation_search(array, low, high, target):
    i = 1
    
    while target >= array[low] and target <= array[high] and low < high:
        probe =int(low + ((high - low ) * (target - array[low]) // (array[high] - array[low])))

        print(f"Comparison {i}:")
        print(f"low: {low}, array[{low}]: {array[low]}")
        print(f"high: {high}, array[{high}]: {array[high - 1]}")
        print()

        if array[probe] == target:
            return probe
        elif array[probe] > target:
            high = probe - 1
        else:
            low = probe + 1
    return -1

array = [1.5,1.75,2.00,2.25,2.50,2.75,3.00,4.00,5.00]
high = len(array) - 1
low = 0
target = 4.00
result = interpolation_search(array, low, high, target)

if result != -1:
    print(f"Index: {result}")
else:
    print("Element not found")