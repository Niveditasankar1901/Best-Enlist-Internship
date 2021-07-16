#Day 26

# Enumerate a python list and try to print the counter with the list value
l = ["Luffy","Zoro","Sanji","Nami","Choper","Robin","Franky","Brook"] 
obj = enumerate(l) 
print (list(enumerate(l,1)))

# Output:-
# [(1, 'Luffy'), (2, 'Zoro'), (3, 'Sanji'), (4, 'Nami'), (5, 'Choper'), (6, 'Robin'), (7, 'Franky'), (8, 'Brook')]
  

# Enumerate a python tuple and try to print the counter with the tuple value
m = ("Naruto","Sauske","Sakura","Kakashi") 
obj = enumerate(m) 
print (tuple(enumerate(m,1)))

# Output:-
# ((1, 'Naruto'), (2, 'Sauske'), (3, 'Sakura'), (4, 'Kakashi'))
