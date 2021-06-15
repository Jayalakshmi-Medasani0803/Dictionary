import tkinter
from PyDictionary import PyDictionary
from tkinter import messagebox as m
dict=PyDictionary()
gui=tkinter.Tk()
gui.title("Dictionary")
gui.geometry("200x200")
l1=tkinter.Label(gui,text="Welcome to Calender")
l1.grid(row=1,column=4)
l2=tkinter.Label(gui,text="Enter word")
l2.grid(row=2,column=2)
e1=tkinter.Entry(gui,width=10)
e1.grid(row=2,column=4)
def clicked():
    word=e1.get()
    meaning=dict.meaning(word)
    synonym=dict.synonym(word)
    antonym=dict.antonym(word)
    m.showinfo(title="Meaning",message=f'Meaning is {meaning} \n Synonym is {synonym} \n Antonym is {antonym}')
b1=tkinter.Button(gui,text="Get Meaning",fg="blue",bg="skyblue",command=clicked)
b1.grid(row=3,column=4)


gui.mainloop()