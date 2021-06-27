# 1- List down all the error types and check all the errors using a python program for all errors

#AssertionError	Raised when the assert statement fails.
#AttributeError	Raised on the attribute assignment or reference fails.
#ImportError	Raised when the imported module is not found.
#IndexError	Raised when the index of a sequence is out of range.
#KeyError	Raised when a key is not found in a dictionary.
#KeyboardInterrupt	Raised when the user hits the interrupt key (Ctrl+c or delete).
#MemoryError	Raised when an operation runs out of memory.
#NameError	Raised when a variable is not found in the local or global scope.
#OverflowError	Raised when the result of an arithmetic operation is too large to be represented
#RuntimeError	Raised when an error does not fall under any other category.
#StopIteration	Raised by the next() function to indicate that there is no further item to be returned by the iterator.
#SyntaxError	Raised by the parser when a syntax error is encountered.
#IndentationError	Raised when there is an incorrect indentation.
#TabError	Raised when the indentation consists of inconsistent tabs and spaces.
#TypeError	Raised when a function or operation is applied to an object of an incorrect type value.
#ZeroDivisionError	Raised when the second operand of a division or module operation is zero.

try:
    print("Start")
    print(1 / 0)
    print("division")	    
except:
    print("Error occured")
finally:
    print("Stop")
#Output:-
#Start
#Error occured
#Stop

# 2- Design a simple calculator app with try and except for all use cases

a=int(input("Enter the value\t"))
b=int(input("Enter the value\t"))
f=input("Enter the function\t")
try:
    if(f=="add"):
        print(a+b)
    elif(f=="sub"):
        print(a-b)
    elif(f=="mul"):
        print(a*b)
    elif(f=="div"):
        print(a/b)
except ZeroDivisionError:
    print("Cannot divide a number by 0")  
else:
    print("Please check the function")

#Output:-
#Enter the value 10
#Enter the value 0
#Enter the function div
#Cannot divide a number by 0

#Enter the value 10
#Enter the value 2
#Enter the function mul
#20

# 3- print one message if the try block raises a NameError and another for other errors

e=10
try:
    print(t)
except NameError:
    print("Variable is not defined")
except:
    print("Check your code")

#Output:-
#Variable is not defined
    
# 4- When try-except scenario is not required

# If you want to test the outcome of program, try-except scenario is not required.
# Try-except make the code a lot harder to comprehend

# 5- Try getting an input inside the try catch block
try:
    x=int(input("Enter the value\t"))
    print(x)
except:
    print("Don't enter the character")
#Output:-
#Enter the value nivedita
#Don't enter the character

#Enter the value 12
#12
