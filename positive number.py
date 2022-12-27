list1=[12, -7, 5, 64, -14]
list2=[12, 14, -95, 3]
print(list1)
for i in list1:
    if i<0:
        list1.remove(i)
print(list1)
print(list2)
for j in list2:
    if j<0:
        list2.remove(j)
        print(list2)
