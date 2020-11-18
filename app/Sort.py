def bubbleSort(unsorted_numbers):

    alist = data_process(unsorted_numbers)

    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                change = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = change


def mergeSort(unsorted_numbers):
    #print("Splitting ",alist)
    alist = data_process(unsorted_numbers)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    #print("Merging ",alist)




def data_process(numbers:str):

    #converting text to list 
    num_list = list(map(int, numbers.strip().split(",")))
    return num_list