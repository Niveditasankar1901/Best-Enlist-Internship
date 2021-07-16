#Day 25

#1. Write a Python program to convert a string to datetime

from datetime import datetime
x = datetime.strptime('Jan 19 2001 11:20PM', '%b %d %Y %I:%M%p')
print(x)
# Output :-
# 2001-01-19 23:20:00

#2. Write a Python program to subtract five days (last working day) from current date

from datetime import date, timedelta
d = date.today() - timedelta(5)
print('Current Date :',date.today())
print('5 days before :',d)
# Output :-
# Current Date : 2021-07-16
# 5 days before : 2021-07-11



#3. Write a Python program to convert the date to datetime using a function 

from datetime import date
from datetime import datetime
t = date.today()
print(datetime.combine(t, datetime.min.time()))
# Output :-
# 2021-07-16 00:00:00


#4. Write a Python program to print next 7 days (week) starting from today

from datetime import date, timedelta
a = date.today() + timedelta(7)
print('Current Date :',date.today())
print('7 days after :',a)
# Output :-
# Current Date : 2021-07-16
# 7 days after : 2021-07-23
