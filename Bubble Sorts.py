##import random
##def bubbleSort(alist):
##    for passnum in range(len(alist)-1,0,-1):
##        for i in range(passnum):
##            if alist[i]>alist[i+1]:
##                temp = alist[i]
##                alist[i] = alist[i+1]
##                alist[i+1] = temp
##
##alist = []
##for j in range(0,20):
##    x = random.randint(1,101)
##    alist.append(x)
##print ("Unsorted:",alist)
##bubbleSort(alist)
##print("Sorted:", alist)

import random
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                change = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = change

alist = []
for j in range(0,20):
    x = random.randint(1,101)
    alist.append(x)
print ("Unsorted", alist)
bubbleSort(alist)
print ( "Sorted", alist)
