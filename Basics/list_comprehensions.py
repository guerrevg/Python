myList = [1, 2, 9, 5, 3, 5]
squared_list = []
for item in myList:
    squared_list.append(item*item)
print(squared_list)


squaredList = [i*i for i in myList]     #Using List_Comprehensions
print(squared_list)