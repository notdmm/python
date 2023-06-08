def insertion_sort(array):
    print("Inside insertion_sort")
    size = len(array)

    for i in range(1, size):
        temp = array[i]
        print(f"    Saving {array[i]} in temp variable...")
        j = i - 1
        print(f"    Value of j (Before): {j}")
        print(f"    Before insertion: {array}")

        while j >= 0 and temp < array[j]:
            array[j + 1] = array[j]
            print(f"        Moving {array[j + 1]} to index {j}...")
            print(f"        Result: {array}")
            j = j - 1
            print(f"        Value of j (after): {j}")

        print(f"        Inserting {temp} to index {j + 1}...")
        array[j + 1] = temp
        print(f"        Partial result: {array}\n")

array = [2, 8, 5, 3, 9, 4]

insertion_sort(array)

print(f"Final result: {array}")
