#Day 7 – Functions
#1.Create a function getting two integer inputs from user

def arithmetic(a,b):
    print("Addition=",a+b)
    print("Subtraction=",a-b)
    print("Division=",a/b)
    print("Multiplication=",a*b)

a=int(input("Enter the value\t"))
b=int(input("Enter the value\t"))
arithmetic(a,b)

#Output:-
#Enter the value 10
#Enter the value 2
#Addition= 12
#Subtraction= 8
#Division= 5.0
#Multiplication= 20
    
#2.Create a function covid( ) & it should accept patient name, and body temperature, by default the body temperature should be 98 degree

def covid(name,temp):
    if(temp > 98):
        print(name,"you are not safe.")
    else:
        print(name,"you are safe.")

name=input("Enter your name\t")
temperature=int(input("Enter your temperature\t"))
covid(name,temperature)

#Output:-
#Enter your name Itachi
#Enter your temperature	100
#Itachi you are not safe.

#Enter your name Rem
#Enter your temperature	32
#rem you are safe.

