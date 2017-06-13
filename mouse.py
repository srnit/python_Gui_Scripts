from tkinter import *
root=Tk()
def leftclick(event):
    print ("left");
def middle(event):
    print ("middle")
def right(event):
    print("right");
fram=Frame(root,width=300, height=100);
fram.bind("<Button-1>",leftclick)
fram.bind("<Button-2>",middle)
fram.bind("<Button-3>",right)
fram.pack();

root.mainloop()
