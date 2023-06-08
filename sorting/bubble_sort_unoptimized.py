def bubble_sort(array):
    print("Inside bubble_sort")

    for i in range(len(array)):
        # Printing stuffs
        print(f"Before swap {i}: {array}")

        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                print(f"    Swapping {array[j]} and {array[j + 1]}...")
                print(f"    Result: {array}\n")
        
nums = [3, 1, 4, 2, -1, 100, 70, 45, 12, 16]

print(f"Before: {nums}\n")

bubble_sort(nums)

print(f"\nAfter: {nums}")
