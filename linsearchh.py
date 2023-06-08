def linear_search(array, size, target):
    for index in range(0, size):
        if array[index] == target:
            return index
    
    return -1

array = [3, 2, 4, 5, 6, 6, 7, 8, 9, 9, 0, 9]
size = len(array)
target = 6

result = linear_search(array, size, target)

if result != -1:
    print(f"Index: {result}")
else:
    print("Element not found")