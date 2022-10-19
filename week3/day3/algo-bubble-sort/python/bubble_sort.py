sequence = [4, 3, 5, 0, 1]
swaps = 0

# Your Code Here

def bubble_sort(arr):
    count = 0

    while arr != sorted(arr):
        for i in range(len(arr) - 1):
            previous = arr[i]
            current = arr[i + 1]
            # print(previous)
            # print(current)
            if previous > current:
                arr[i] = current
                arr[i + 1] = previous
                count += 1
            else:
                count += 1
    return (arr, count)

print(bubble_sort([0,3,1,5,4]))
print(bubble_sort([0,1,4,3,5]))
print(bubble_sort([5,3,0,1,4]))
print(bubble_sort([5,4,3,0,1]))
print(bubble_sort([5,1,4,3,0]))

# print(f"Final result: {result}")
# print(f"Swaps: {swaps}")
