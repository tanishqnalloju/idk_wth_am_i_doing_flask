def binary_search(unsorted_list, key):

    sorted_list, key = data_process(unsorted_list, key)
    length = len(sorted_list)
    start = 0
    end = length - 1
    while start <= end:
        mid = int((start + end) / 2)
        if key == sorted_list[mid]:
            #print("Entered number", key, "is present at position", mid)
            return True
        elif key < sorted_list[mid]:
            end = mid - 1
        elif key > sorted_list[mid]:
            start = mid + 1
    #print("Element not found!")
    return False

def linear_search(unsorted_list, key):

    unsorted_list, key = data_process(unsorted_list, key)
    for ele in unsorted_list:
        if ele == key:
            return True
        
    return False
        

def data_process(numbers:str, key:str):
    #converting text to list 
    num_list = list(map(int, numbers.strip().split(",")))
    return num_list, int(key)
