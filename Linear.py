lst = []

num = int(input("Enter the number of items in the list: "))

for i in range(num):
    numbers =int(input("Enter any number: "))
    lst.append(numbers)

found = False

x = int(input("Enter a number to be searched: "))

for j in range(len(lst)):
    if x == lst[i]:
        found = True
        print(x,'was found at position',i)
        break
    
    if found is found:
        print(x,'is not in the list')
        break
    

