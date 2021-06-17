#DAY-6
#1) Write a Python script to merge two Python dictionaries

x={"One piece":"Monkey D Luffy", "Naruto":"Kakashi Hatake","Jujutsu kaisen":"Gojo Satoru"}
y={"Kaguya sama":"Miyuki Shirogane","One punch man":"Saitama"}
z=x.copy()
z.update(y)
print(z)
#Output :- {'One piece': 'Monkey D Luffy', 'Naruto': 'Kakashi Hatake', 'Jujutsu kaisen': 'Gojo Satoru', 'Kaguya sama': 'Miyuki Shirogane', 'One punch man': 'Saitama'}

#2) Write a Python program to remove a key from a dictionary

del z["Kaguya sama"]
print(z)
#Output :- {'One piece': 'Monkey D Luffy', 'Naruto': 'Kakashi Hatake', 'Jujutsu kaisen': 'Gojo Satoru', 'One punch man': 'Saitama'}

#3) Write a Python program to map two lists into a dictionary

key=["Luffy","Nami","Zoro","Ussop","Sanji","Chopper","Robin"]
value=["Captain","Navigator","Swordmen","Snipper","Cook","Doctor","Archaeologist"]
d=dict(zip(key,value))
print(d)
#Output :- {'Luffy': 'Captain', 'Nami': 'Navigator', 'Zoro': 'Swordmen', 'Ussop': 'Snipper', 'Sanji': 'Cook', 'Chopper': 'Doctor', 'Robin': 'Archaeologist'}

#4) Write a Python program to find the length of a set

set={14,42,13,32,89,98}
print(len(set))
#Output :- 6

#5) Write a Python program to remove the intersection of a 2nd set from the 1st set

s1={1,2,3,4,5}
s2={4,5,6,7,8}
for i in s1&s2:
    s1.remove(i)
print("s1",s1)
print("s2",s2)
#Output :- s1 {1, 2, 3}
          #s2 {4, 5, 6, 7, 8}
