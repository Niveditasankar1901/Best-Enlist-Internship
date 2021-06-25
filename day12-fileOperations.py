#Day-12
#Create a file 30 days 30 hour operations
#Write data in it I have completed 10 days successfully.
#Append the data your name in to it.
#Close the file.

#create a text file as "file1.txt" 
file1 = open("file1.txt","r") 
print ("Output of Reading the file")
print ( file1.readlines() )
print

#Output of Read the file
#['30 days 30 hour operations']

#write mode
file1 = open("file1.txt","w") 
file1.write("I have completed 10 days successfully ") 
 

file1 = open("file1.txt","r") 
print ("Output of Readlines after writing")
print ( file1.readlines() )
print

#Output of Readlines after writing
#['I have completed 10 days successfully ']

#append mode 
file1 = open("file1.txt","a")
file1.write("Nivedita ") 


file1 = open("file1.txt","r") 
print ("Output of Readlines after appending")
print (file1.readlines()) 
print

file1.close()

#Output of Readlines after appending
#['I have completed 10 days successfully Nivedita ']
