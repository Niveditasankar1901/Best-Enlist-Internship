#Day 21

#1. Write a program using zip() function and list() function, create a merged list of tuples from the two lists given.
a=["Portgas D","Monkey D","Edward","Boa"]
b=["Ace","Luffy","Newgate","Hancock"]
print(list(zip(a,b)))
#Output:-
#[('Portgas D', 'Ace'), ('Monkey D', 'Luffy'), ('Edward', 'Newgate'), ('Boa', 'Hancock')]

#2. First create a range from 1 to 8. Then using zip, merge the given list and the range together to create a new list of tuples.
r=range(1,9)
n=("a","b","c","d","e","f","g","h")
print(tuple(zip(n,r)))
#Output:-
#(('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6), ('g', 7), ('h', 8))

#3. Using sorted() function, sort the list in ascending order.
k=["Luffy","Nami","Zoro","Ussop","Sanji","Chopper","Robin"]
print(sorted(k))
#Output:-
#['Chopper', 'Luffy', 'Nami', 'Robin', 'Sanji', 'Ussop', 'Zoro']

#4. Write a program using filter function, filter the even numbers so that only odd numbers are passed to the new list.
def even(x):
    if(x%2==0):
        return x

x=[1,2,3,4,5,6,7,8,9,10]
f=filter(even,x)
print('The filtered numbers are:') 
for s in f: 
    print(s) 
#Output:-
#The filtered numbers are:
#2
#4
#6
#8
#10
