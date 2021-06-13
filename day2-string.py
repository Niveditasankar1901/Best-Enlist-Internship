#Day 2 : String Practice

#How to print a value?
print("30 days 30 hour challenge")
#Output :- 30 days 30 hour challenge

print('30 days 30 hour challenge')
#Output :- 30 days 30 hour challenge

#Assigning String to Variable:
Hours = "thirty"
print(Hours)
#Output :- thirty

#Indexing using String:
Days = "Thirty days"
print(Days[3])
#Output :- r

#How to print the particular character from certain text?
Challenge = "I will win"
print(Challenge[7:10])
#Output :- win

#Print the length of Character:
Challenge = "I will win"
print(len(Challenge))
#Output :- 10

#Convert String into lower character;
Challenge = "I will win"
print(Challenge.lower())
#Output :- i will win

#String Concatenation – Joining two strings
a = "30 Days"
b = "30 hours"
c = a + b
print(c)
#Output :- 30 Days30 hours

#Adding space during concatenation
a = "30 Days"
b = "30 hours"
c = a + " " + b
print(c)
#Output :- 30 Days 30 hours

#casefold() - Usage
text = "Thirty days and Thirty hours"
a = text.casefold()
print(a)
#Output :- thirty days and thirty hours

#capitalize()
text = "Thirty days and Thirty hours"
b = text.capitalize()
print(b)
#Output :- Thirty days and thirty hours

#find()
text = "Thirty days and Thirty hours"
c = text.find("days")
print(c)
#Output :- 7

#isalpha()
text = "Thirty days and Thirty hours"
d = text.isalpha()
print(d)
#Output :- False

#isalnum()
text = "Thirty days and Thirty hours"
e = text.isalnum()
print(e)
#Output :- False
