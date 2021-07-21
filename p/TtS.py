from tkinter import *
from tkinter import ttk
import pyttsx3

root = Tk()
root.geometry("800x500")

def talk():
    engine = pyttsx3.init()
    engine.setProperty('rate',150)
    engine.setProperty('volume',1.0)    
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.say(my_entry.get())
    engine.runAndWait()
    my_entry.delete(0,END)


my_entry = Entry(root)
my_entry.pack(pady=20)

my_button = Button(root,text="play", command=talk)
my_button.pack(pady=20)

vertical = Scale(root,from_=0, to=200)
vertical.pack()

horizontal = Scale(root,from_=0, to=200,orient=HORIZONTAL,tickinterval=50,length=500,
activebackground='gray',cursor='target',label='red',showvalue=10,sliderlength=10,
troughcolor='gray',width=30)
horizontal.set(50)
######################################################################################

def slide(x):
    text_slider.config(text=int(horizontal1.get()))


horizontal1 = ttk.Scale(root,from_=0,to=200,orient=HORIZONTAL,value=100,command=slide)
horizontal1.pack()

text_slider = Label(root,text='')
text_slider.pack(pady=20)

horizontal.pack()
####################################################################################


root.mainloop()

#activebackground -> color of that slider cursor
#bg whole color bd ->3d view inside border
#cursor -> arrow circle clock cross dotbox exchange fleur heart fg
#highlightbackground -> bordercolor whole rectangle
#label topleft text
#repeatdelay defalult 300,sliderlength,throughcolor, width->height of slider