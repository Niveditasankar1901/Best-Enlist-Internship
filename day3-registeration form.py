#importing library
from tkinter import *
from tkinter import ttk

window = Tk()
#Declaring Window Title
window.title("Registration form")
#Declaring Window size
window.geometry('500x400')
#Declaring Window Color
window.configure(background = "#00cccc");
#below four fields are declared
Label(window ,text = "First Name", width="15", height="1",fg="black",background="#00cccc").grid(row = 0,column = 2)
Entry(window,width="15").grid(row = 0,column = 3)

Label(window ,text = "Last Name",width="15", height="1",fg="black",background="#00cccc").grid(row = 1,column = 2)
Entry(window,width="15").grid(row = 1,column = 3)

Label(window ,text = "Email Id",width="15", height="1",fg="black",background="#00cccc").grid(row = 2,column = 2)
Entry(window,width="15").grid(row = 2,column = 3)

Label(window ,text = "Contact Number",width="15", height="1",fg="black",background="#00cccc").grid(row = 3,column = 2)
Entry(window,width="15").grid(row = 3,column = 3)

Label(window ,text = "Course",width="15", height="1",fg="black",background="#00cccc").grid(row = 4,column = 2)
Radiobutton(window, text="B.E", value=1,width="13",height="1",fg="black",background="#00cccc",border="6").grid(row=4,column=3)
Radiobutton(window, text="BTech", value=2,width="13",height="1",fg="black",background="#00cccc",border="6").grid(row=5,column=3)
Radiobutton(window, text="Arts and Science", value=3,width="13",height="1",fg="black",background="#00cccc",border="6").grid(row=6,column=3)
Radiobutton(window, text="Others", value=4,width="13",height="1",fg="black",background="#00cccc",border="6").grid(row=7,column=3)

Label(window ,text = "Department",width="15", height="1",fg="black",background="#00cccc").grid(row = 8,column = 2)
Entry(window,width="15").grid(row = 9,column = 3)
drop=StringVar()
drop.set("Choose the department")
OptionMenu(window,drop,"ECE","EEE","CSC","MECH").grid(row = 8,column = 3)

CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()
Label(window ,text = "Interested Domain",width="15", height="1",fg="black",background="#00cccc").grid(row = 9,column = 2)
Checkbutton(window, text="Artificial Intellegence",  variable = CheckVar1, onvalue = 1, offvalue = 0, height=1, width = 15).grid(row = 9,column = 3)
Checkbutton(window, text="Internet of Things",  variable = CheckVar2, onvalue = 1, offvalue = 0, height=1, width = 15).grid(row = 10,column = 3)
Checkbutton(window, text="Machine Learning",  variable = CheckVar3, onvalue = 1, offvalue = 0, height=1, width = 15).grid(row = 11,column = 3)
Checkbutton(window, text="Data Science",  variable = CheckVar4, onvalue = 1, offvalue = 0, height=1, width = 15).grid(row = 12,column = 3)


#fubction declaration
def clicked():
    res = "Thanks for registerring" + txt.get()
    lbl.configure(text= res)
tn = ttk.Button(window ,text="Submit",width="15").grid(row = 20,column = 3)
window.mainloop()
