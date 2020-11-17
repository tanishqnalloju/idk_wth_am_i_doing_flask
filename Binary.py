def binary_sort(sorted_list, length, key):
    start = 0
    end = length - 1
    while start <= end:
        mid = int((start + end) / 2)
        if key == sorted_list[mid]:
            print("Entered number", key, "is present at position", mid)
            return -1
        elif key < sorted_list[mid]:
            end = mid - 1
        elif key > sorted_list[mid]:
            start = mid + 1
    print("Element not found!")
    return -1


lst = []

size = int(input("Enter size of list: "))

for n in range(size):
    numbers = int(input("Enter any number: "))
    lst.append(numbers)

lst.sort()
print('The list will be sorted, the sorted list is:', lst)

x = int(input("Enter the number to search: "))

binary_sort(lst, size, x)


