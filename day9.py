#Day 9
# Write a program to loop through a list of numbers and add +2 to every value to elements in list
p=[1,2,3,4,5]
for i in p:
    i=i+2
    print (i)
#Output:-
#3
#4
#5
#6
#7
    
# Write a program to get the below pattern
n = 5
for i in range(n, 0, -1):
    num = i
    for j in range(i,0,-1):
        print(j, end=" ")
    print(" ")
#Output:-
#5 4 3 2 1  
#4 3 2 1  
#3 2 1  
#2 1  
#1
    
# Python Program to Print the Fibonacci sequence
a=1
b=1
n=5
print(a)
print(b)
for i in range(0,n):
    c=a+b
    print(c)
    a=b
    b=c
    c=a
    n=n+1
#Output:-
#1
#1
#2
#3
#5
#8
#13
    
# Explain Armstrong number and write a code with a function
# An armstrong number is a number which equal to the sum of the cubes of its individual digits(for 3 digit).
# For example,
#153 = (1)^3 + (5)^3 + (3)^3
#153 = 1 + 125 + 27 = 153
#153 is an armstrong number

def armstrong(n):
    sum=0
    temp=n
    while(temp!=0):
        a=temp%10
        sum=sum+a**3
        temp=temp//10
    if(n==sum):
        print(n,"is a armstrong number")
    else:
        print(n,"is not a armstrong number")
            
n=int(input("Enter the value\t"))
armstrong(n)
#Output:-
#Enter the value 153
#153 is a armstrong number

# Write a program to print the multiplication table of 9
n=12
for i in range(1,n+1):
    x=i*9
    print(i,"*9 =",x)
#Output:-
#1 *9 = 9
#2 *9 = 18
#3 *9 = 27
#4 *9 = 36
#5 *9 = 45
#6 *9 = 54
#7 *9 = 63
#8 *9 = 72
#9 *9 = 81
#10 *9 = 90
#11 *9 = 99
#12 *9 = 108

# Check if a program is negative or positive
a=int(input("Enter the value\t"))
if(a>0):
    print(a,"is a positive number")
elif(a<0):
    print(a,"is a negative number")
else:
    print("Zero")
#Output:-
#Enter the value -8
#-8 is a negative number
    
# Write a program to convert the number of days to ages
q=int(input("Enter the number of days\t"))
print("Age=",q/365)
#Output:-
#Enter the number of days700
#Age= 1.917808219178082

# Solve Trigonometry problem using math function write a program to solve using math function
import math
f=input("Enter the function\t")
n=int(input("Enter the value\t"))
if(f=="sin"):
    print(math.sin(n))
elif(f=="cos"):
    print(math.cos(n))
elif(f=="tan"):
    print(math.tan(n))
elif(f=="cosine"):
    print(math.cosine(n))
elif(f=="sec"):
    print(math.sec(n))
elif(f=="cot"):
    print(math.cot(n))
else:
    print("Please enter valid function")
#Output:-
#Enter the function cos
#Enter the value 0
#1.0
    
# Create a calculator only on a code level by using if condition (Basic arithmetic calculation)
a, b = map(int, input("Enter a two value: ").split())
f=input("add-addition\nsub-subtraction \nmul-multiplication \ndiv-division \nmod-modulo \nEnter the function ")
if(f=="add"):
    print(a+b)
elif(f=="sub"):
    print(a-b)
elif(f=="mul"):
    print(a*b)
elif(f=="div"):
    print(a/b)
elif(f=="mod"):
    print(a%b)
else:
    print("Please enter valid function")
#Output:-    
#Enter a two value: 2 7
#add-addition
#sub-subtraction 
#mul-multiplication 
#div-division 
#mod-modulo 
#Enter the function add
#9    
