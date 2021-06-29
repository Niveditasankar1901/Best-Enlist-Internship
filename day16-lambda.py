# Day 16

# 1- Create a lambda function that multiplies argument x with argument y
x=int(input("Enter the value\t"))
y=int(input("Enter the value\t"))
z=lambda a,b : a*b
print(z(x,y))
#Output:- 
#Enter the value 10
#Enter the value 2
#20

# Write a Python program to create Fibonacci series to n using Lambda
from functools import reduce
fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],range(n-2), [0, 1])
n=int(input("Enter the value\t"))
print(fib(n))
#Output:-
#Enter the value 7
#[0, 1, 1, 2, 3, 5, 8]

# Write a Python program that multiply each number of given list with a given number
lst = [] 
lst = [int(i) for i in input("Enter the list of values\t").split()]
n = int(input("Enter the value\t"))
print(list(map(lambda q:q*n,lst)))
#Output:-
#Enter the list of values   1 2 3 4 5
#Enter the value 5
#[5, 10, 15, 20, 25]

# Write a Python program to find numbers divisible by 9 from a list of numbers
r=[12,9,18,753,27,765]
print(list(map(lambda o:(o%9==0),r)))
#Output:-
#[False, True, True, False, True, True]

# Write a Python program to count the even numbers in a given list of integers
p=[1,2,3,4,5,6]
t=tuple(filter(lambda s:(s%2 == 0),p))
print(len(t))
#Output:-
#3



