def interpolation_search(array, low, high, target):
    i = 1

    while target >= array[low] and target <= array[high] and low < high:
        probe =int(low + ((high - low ) * (target - array[low]) // (array[high] - array[low])))

        print(f"comparison {i}:")
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

array = [99,66,96]
high = len(array) - 1
low = 1
target = 96
result = interpolation_search(array, low, high, target)

if result != -1:
    print(f"found index: {result}")
else:
    print("element not found")