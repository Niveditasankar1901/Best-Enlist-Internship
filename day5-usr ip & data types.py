# DAY 5
# 1)Write a program to create a list of n integer values

# Add an item in to the list 
l=[]
l.append(8)
print(l)
#Output :- [8]

l2=[3,7,9,5,4,1,7,6]
l.extend(l2)
print(l)
#Output :- [8, 3, 7, 9, 5, 4, 1, 7, 6]

l.insert(3,0)
print(l)
#Output :- [8, 3, 7, 0, 9, 5, 4, 1, 7, 6]

# Delete an item in to the list 
del l[3]
print(l)
#Output :- [8, 3, 7, 9, 5, 4, 1, 7, 6]

del l[4:6]
print(l)
#Output :- [8, 3, 7, 9, 1, 7, 6]

l.pop(0)
print(l)
#Output :- [3, 7, 9, 1, 7, 6]

l.remove(9)
print(l)
#Output :- [3, 7, 1, 7, 6]

# Store the largest number from the list to a variable
x=max(l)
print(x)
#Output :- 7

# Store the smallest number from the list to a variable
y=min(l)
print(y)
#Output :- 1

#2) Create a tuple and print the reverse of the created tuple
t=(6,7,9,5,4,2,1)
x=t[::-1]
print(x)
#Output :- (1, 2, 4, 5, 9, 7, 6) 

#3) Create a tuple and convert tuple into list
e=(234,'dfg',543,'ytrr')
print(list(e))
#Output :- [234, 'dfg', 543, 'ytrr']

