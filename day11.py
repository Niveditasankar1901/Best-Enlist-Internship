# Day 11

# 1.Create a python module with list and import the module in another .py file and change the value in list
# Create a python file that contain list and save as lis_module
# Create another python file and import lis_module
from lis_module import *
k[0]=8
print (k)

#Output:-
#[1, 2, 3, 4]
#[8, 2, 3, 4]

# 2.Install pandas package
# pip install pandas
import pandas as pd
d = pd.DataFrame({'X':[7,8,9,0,6], 'Y':[4,9,8,3,7],'Z':[1,4,3,2,8]});
print(d)

#Output:-
#   X  Y  Z
#0  7  4  1
#1  8  9  4
#2  9  8  3
#3  0  3  2
#4  6  7  8

# 3.Import a module that picks random number and write a program to fetch a random number from 1 to  100 on every run
import random
print(random.randint(0,100))

#Output:- 41

# 4.Import sys package and find the python path
import sys
for p in sys.path:
    print(p)
    
#Output:-
#C:\Users\User\Desktop\New folder
#C:\Users\User\AppData\Local\Programs\Python\Python37\Lib\idlelib
#C:\Users\User\AppData\Local\Programs\Python\Python37\python37.zip
#C:\Users\User\AppData\Local\Programs\Python\Python37\DLLs
#C:\Users\User\AppData\Local\Programs\Python\Python37\lib
#C:\Users\User\AppData\Local\Programs\Python\Python37
#C:\Users\User\AppData\Roaming\Python\Python37\site-packages
#C:\Users\User\AppData\Local\Programs\Python\Python37\lib\site-packages
#C:\Users\User\AppData\Local\Programs\Python\Python37\lib\site-packages\win32
#C:\Users\User\AppData\Local\Programs\Python\Python37\lib\site-packages\win32\lib
#C:\Users\User\AppData\Local\Programs\Python\Python37\lib\site-packages\Pythonwin
 
# 5.Try to install a package and uninstall a package using pip
# pip install os
# pip uninstall os
