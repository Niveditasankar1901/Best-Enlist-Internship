# Day 22

#1. Read a jpeg image and print the image file

import cv2
img = cv2.imread('naruto.jpg')
cv2.imshow('image', img)
cv2.waitKey(0)		
cv2.destroyAllWindows()

#2. Merge two pdf files using python script
import PyPDF2 

pdf1File = open('day2.pdf', 'rb')
pdf2File = open('day4.pdf', 'rb')

pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)

pdfWriter = PyPDF2.PdfFileWriter()
 
for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
 
for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
 

pdfOutputFile = open('MergedFiles.pdf', 'wb')
pdfWriter.write(pdfOutputFile)

pdfOutputFile.close()
pdf1File.close()
pdf2File.close()

#3. Scrape a website and store the data into DB.

import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.storylink')
subtext = soup.select('.subtext')
links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):
  return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
  hn = []
  for idx, item in enumerate(links):
    title = item.getText()
    href = item.get('href', None)
    vote = subtext[idx].select('.score')
    if len(vote):
      points = int(vote[0].getText().replace(' points', ''))
      if points > 99:
        hn.append({'title': title, 'link': href, 'votes': points})
  return sort_stories_by_votes(hn)
 
pprint.pprint(create_custom_hn(mega_links, mega_subtext))

#4. Write queries to filter the data in db
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Yourpassword",
  database = "best-enlist"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customer WHERE name='John' ")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  
#Output
#('John', 'Highway 21')
