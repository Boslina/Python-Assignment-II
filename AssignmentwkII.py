#empty list
my_list = []
print(my_list)

#Append my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

#insert 15 at the second position
my_list.insert(2, 15)
print(my_list)

#extend my_list with another_list

Another_list = [50, 60, 70]
my_list.extend(Another_list)
print(my_list)

#remove the last element from my_list
del my_list[-1]
print(my_list)

#sort my_list in ascending order
my_list.sort()
print(my_list)

#Find and print the index of the value 30 in my_list.
position = my_list.index(30)
print(position)