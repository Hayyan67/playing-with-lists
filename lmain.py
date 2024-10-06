l1=[23,87,98,34,67,89,12,8,45,78,23,56,23]
sum=0
for c in l1:
    sum=sum+c
print('The sum of element of the list is: ',sum)
print('The maximum element of the list is: ',max(11))
print('The count of 23 is: ',l1.count(23))
print('The minimum element of the list is: ',min(l1))
l1.append(77)
print('updated list: ',l1)
l1.insert(3,36)
print('updated list: ',l1)
l1.remove(34)
print('updated list: ',l1)