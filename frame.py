from tkinter import *
from tkinter.ttk import * 
root=Tk()
s = Style()
s.configure('My.TFrame', background='red')
topframe=Frame(root,style="My.TFrame");
topframe.place(height=70, width=400, x=83, y=109)
topframe.config()



bottamframe=Frame(root)
bottamframe.pack(side=BOTTOM);
button1=Button(topframe,text="click me1");
button2=Button(topframe,text="click me2");
button3=Button(topframe,text="click me3");
button4=Button(bottamframe,text="click me4");
button1.pack(side="left")
button2.pack(side="right")
button3.pack(side="right")
button4.pack(side=BOTTOM)


root.mainloop();
