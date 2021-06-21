#Day 8
#Write a Python script to merge two Python dictionaries
a = {'Maths': 60, 'Physics': 80}
b = {'Chemistry': 50, 'Computer Science': 90}
z = a.copy()
z.update(b)
print(z)
#Output:- {'Maths': 60, 'Physics': 80, 'Chemistry': 50, 'Computer Science': 90}

#Write a program to sort the value from descending to ascending in list and convert it in to a set.
l=["Naruto","Zoro","Luffy","Levi","Kaguya"]
l.sort(reverse=True)
print("Descending =",l)
l.sort()
print("Ascending =",l)
print("Coverting to set = ",set(l))
#Output:-
#Descending = ['Zoro', 'Naruto', 'Luffy', 'Levi', 'Kaguya']
#Ascending = ['Kaguya', 'Levi', 'Luffy', 'Naruto', 'Zoro']
#Coverting to set =  {'Luffy', 'Levi', 'Zoro', 'Kaguya', 'Naruto'}

#Write a Python program to list number of items in a dictionary key and sort thelist with the help of a function & without the function.
d={"Dark":"Jonas Kahnwald", "Sherlock":"Sherlock Holmes","Flash":"Barry Allen","Stranger Things":"Eleven"}
print(len(d))
print("Sorting using Fuction =",sorted(d))
#Output:-
#4
#Sorting using Fuction = ['Dark', 'Flash', 'Sherlock', 'Stranger Things']

#Write a Python program to get a string from a given string (user input) and change the first occurrence of the word to a user specified input.
u=input("Enter the string ")
r=input("Enter the Character ")
print(u.replace(u[0],r))
#Output:-
#Enter the string Monkey
#Enter the Character D
#Donkey

#Write a Python program to get a string from a given string where all occurrences of its first char have been changed to capital letter.
f=input("Enter string")
print(f.title())
#Output:- 
#Enter string monkey d luffy
#Monkey D Luffy

#Write a Python program to find the repeated items of a list
k=[1,0,3,8,5,2,3,6,7,9,5]
p=[]
for i in k:
    if i not in p:
        p.append(i)
    else:
        print(i,end=' ')
#Output:- 3 5
        
#Write a Python program to check the sum of three elements and divided by a value which is given as an input by the user
x, y, z = map(int, input("Enter a three value: ").split())
d=int(input("Enter the divisor"))
print((x+y+z)/d)
#Output:-
#Enter a three value: 4 5 9
#Enter the divisor5
#3.6

#Write a Python program to find the Mean,median,mode among three given numbers
import statistics
o=[2,3,7,4,8,3,1]
print(statistics.mean(o))
print(statistics.median(o))
print(statistics.mode(o))
#Output:-
#4
#3
#3


#Write a Python program to swap cases of a given string
j = input("Enter the string")
print(j.swapcase())
#Output:-
#Enter the string bEliEvE iT
#BeLIeVe It


#Write a program to convert an integer to binary & octal decimal
c = 34
print("Binary =",bin(c))
print("Octal =",oct(c))
#Output:-
#Binary = 0b100010
#Octal = 0o42



