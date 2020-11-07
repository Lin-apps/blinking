import os
import time
from tkinter import*

root=Tk()

sc=2

def fune():
	sc=0

Button(root, text="STOP", command=fune).pack()


def fun():

	while sc>1:
		f= open("file.txt","x")
		for i in range(10):
			f.write("Skrivnost Skrivnosti")
		f.close() 
		time.sleep(0.5)
		os.remove("file.txt")
		time.sleep(0.5)

fun()

root.mainloop()