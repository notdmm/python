def selection_sort(array):
    size = len(array)

    for i in range(0, size - 1):
        min_index = i
        print(f"Minimum index: {min_index}")
        print(f"Iteration (outer loop): {i}")
        print(f"Before swap: {array}")

        for j in range(i + 1, size):
            print(f"        Iteration (inner loop): {j}")
            if array[min_index] > array[j]:
                print(f"        Changing minimum index to {j}...")
                min_index = j

        if min_index != i:
            print(f"Swapping {array[i]} and {array[min_index]}...")
            array[i], array[min_index] = array[min_index], array[i]
        print(f"Partial result: {array}\n")

array = [2, 8, 5, 3, 9, 4, 1]

selection_sort(array)

print(f"Final result: {array}")
