from tkinter import *
root=Tk()
label1=Label(root,text="Name")
label2=Label(root,text="Password",show="*")
enter1=Entry(root);
enter2=Entry(root);
label1.grid(row=0)
label2.grid(row=1);
enter1.grid(row=0,column=1)
enter2.grid(row=1,column=1)
root.mainloop()
