def bubble_sort(array):
    print("Inside bubble_sort")
    
    swapped = True

    while swapped:
        print(f"Before swap: {array}")
        
        swapped = False

        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True  
                print(f"    Swapping {array[i]} and {array[i + 1]}...")
                print(f"    Result: {array}\n")

nums = [3, 1, 4, 2, -1, 100, 70, 45, 12, 16]

print(f"Before: {nums}\n")

bubble_sort(nums)

print(f"\nAfter: {nums}")
