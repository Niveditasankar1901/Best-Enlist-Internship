#Day 23

#Mini project:

#Create a Tkinter project with the below functionalities:


#3. Create two browse button and place the .pdf file for the buttons and create a merge pdf option -  Watermark Merger App

import tkinter as tk
from tkinter.filedialog import askopenfilename
from PyPDF2 import PdfFileMerger, PdfFileReader
from pathlib import Path

filelist = []


merger = PdfFileMerger()

def open_file(files):
    filepath = askopenfilename(
        filetypes=[("PDF Files","*.pdf"), ("All Files", "*.*")]
    )
    if not(filepath and Path(filepath).exists()):
        return
    files.append(filepath)
    
    
    lbl_items["text"] = '\n'.join(str(f) for f in files)
    if len(files) >= 2 and btn_merge['state'] == "disabled":
        btn_merge["state"] = "normal"

def merge_pdfs(files):
    for f in files:
        merger.append(PdfFileReader(open(f, "rb")))
    
    output_filename = ent_output_name.get()

    if not output_filename:
        output_filename = "Untitled.pdf"
    elif ".pdf" not in output_filename:
        output_filename += ".pdf"
    merger.write(output_filename)


window = tk.Tk()
window.title("PDF Merger App")
window.geometry("500x500")

window.resizable(0,0)


fr_bg1 = tk.Frame(window, bd=3)
lbl_open = tk.Label(fr_bg1, text="Select the PDF files")
lbl_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

btn_open = tk.Button(fr_bg1, text="Open file",bg='blue', fg='white',font=('times new roman', 12, 'bold') ,
                command=lambda: open_file(filelist))
btn_open.grid(row=1, column=0, sticky="ew", padx=5)
lbl_items = tk.Label(fr_bg1, text="")
lbl_items.grid(row=2, column=0, pady=5)
fr_bg1.pack()


fr_bg2 = tk.Frame(window, bd=3)
lbl_to_merge = tk.Label(fr_bg2, text="Save as")
lbl_to_merge.grid(row=0, column=0, sticky="ew", padx="5", pady="5")

ent_output_name = tk.Entry(master=fr_bg2, width=7)
ent_output_name.grid(row=1, column=0, sticky="ew")

btn_merge = tk.Button(fr_bg2,bg='light blue',font=('times new roman', 12, 'bold') ,text="Merge",state="disabled",
                command=lambda: merge_pdfs(filelist))
btn_merge.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
fr_bg2.pack()


btn_exit = tk.Button(window, text="Exit", command=window.destroy, bd=2, bg='blue', fg='white',font=('times new roman', 12, 'bold') ,)
btn_exit.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.FALSE)

if __name__ == "__main__":
    window.mainloop()
