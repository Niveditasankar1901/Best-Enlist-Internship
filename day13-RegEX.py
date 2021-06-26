#Write a Python program for all the cases which can check a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)
import re
def character(string):
    c = re.compile(r'[^a-zA-Z0-9.]')
    string = c.search(string)
    return not bool(string)

print(character("NiveditaS")) 
print(character("&%@=#!}>."))
#Output:-
#True
#False

#Write a Python program that matches a word containing 'ab'
import re
def match(word):
    pattern = 'ab'
    if re.search(pattern, word):
        return ("Match found")
    else:
        return ("Match not found")
print(match("abdul kalam"))
print(match("science"))
#Output:-
#Match found
#Match not found

#Write a Python program to check for a number at the end of a word/sentence.
import re
def match(word):
    pattern = re.compile(r'[0-9$]')
    if re.search(pattern, word):
        return ("Match found")
    else:
        return ("Match not found")
print(match("Nivedita Sankar1901"))
print(match("Nivedita"))
#Output:-
#Match found
#Match not found

#Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string
import re
str = '12,3,65,876543,hello,world'
x = re.findall('[0-9]+', str)
N=3
def fil(n):
	if(len(n)<=N):
		return True
	else:
		return False
		
f = list(filter(fil, x))
print('Numbers are',f)
#Output:- Numbers are ['12', '3', '65']

#Write a Python program to match a string that contains only uppercase letters
import re
def match(word):
    pattern = '^[A-Z]*$'
    if re.fullmatch(pattern, word):
        return ("Match found")
    else:
        return ("Match not found")
print(match("NARUTO"))
print(match("luffy"))
#Output:- 
#Match found
#Match not found

