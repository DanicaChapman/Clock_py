from tkinter import Tk, Label
import time
import sys

master = Tk()
master.title("ClocK")

def thetime():
    Time = time.strftime("%I:%M:%S %p")
    clock.config(text=Time)
    clock.after(200,thetime)

clock = Label(master, font=("Tekton Pro", 100), bg="black",fg="deep sky blue")
clock.pack()

thetime()
master.mainloop()
