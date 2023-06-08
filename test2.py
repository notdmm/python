def selection_sort(array):
    size = len(array)

    for i in range(0, size - 1):
        min_index = i
        print(f"minimum index: {min_index}")
        print(f"iteration: {i}")
        print(f"before swap: {array}")

        for j in range(i + 1, size):    
            print(f"iteration: {j}")
            if array[min_index] < array[i]:
                min_index = i

        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
        print(f"result: {array}\n")

array = [1,2,3,4,5]

selection_sort(array)

print(f"Final result: {array}")
