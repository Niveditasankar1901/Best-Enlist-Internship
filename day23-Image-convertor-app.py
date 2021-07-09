#Day 23

#Mini project:

#Create a Tkinter project with the below functionalities:

#1. Create a browse option with a specific folder which has all the JPEG Files & create a Convert button to convert the image from JPEG to PNG – Basic Image converter App

from tkinter import *
from tkinter import filedialog as fd
import os
from PIL import Image
from tkinter import messagebox

root = Tk()

root.title("Image_Converter_App")


def jpg_to_png():
	global im1

	
	import_filename = fd.askopenfilename()
	if import_filename.endswith(".jpg"):

		im1 = Image.open(import_filename)
		export_filename = fd.asksaveasfilename(defaultextension=".png")
		im1.save(export_filename)
		messagebox.showinfo("success ", "your image converted to png")
		
	else:
		Label_2 = Label(root, text="Error!", width=20,
						fg="red", font=("bold", 15))
		Label_2.place(x=80, y=280)
		messagebox.showerror("Fail!!", "Something Went Wrong...")


def png_to_jpg():
	global im1
	import_filename = fd.askopenfilename()

	if import_filename.endswith(".png"):
		im1 = Image.open(import_filename)
		export_filename = fd.asksaveasfilename(defaultextension=".jpg")
		im1.save(export_filename)

		messagebox.showinfo("success ", "your Image converted to jpg ")
	else:
		Label_2 = Label(root, text="Error", width=20,
						fg="red", font=("bold", 15))
		Label_2.place(x=80, y=280)

		messagebox.showerror("Failed", "Something Went Wrong")


button1 = Button(root, text="JPG to PNG", width=20, height=2, bg="#430366",
				fg="white", font=("Times new roman", 14, "bold"), command=jpg_to_png)

button1.place(x=120, y=120)

button2 = Button(root, text="PNG to JPG", width=20, height=2, bg="#430366",
				fg="white", font=("Times new roman", 14, "bold"), command=png_to_jpg)

button2.place(x=120, y=220)
root.geometry("500x500+400+200")
root.mainloop()
