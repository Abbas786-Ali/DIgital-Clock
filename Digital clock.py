from tkinter import *
from tkinter.ttk import *
from time import strftime 
root=Tk()
root.title('python Digital clock')
def time():
    string=strftime('%H:%M:%S %p\n %D')
    label.configure(text=string)
    label.after(1000,time)
label=Label(root,font=('calibri',50,'bold'),background='green',foreground='black')
label.pack(anchor='center')

time()
mainloop()