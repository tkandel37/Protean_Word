from tkinter import *
from tkinter import ttk
from tkinter import font

def audio():
    audio_dialogue = Toplevel()
    audio_dialogue.geometry('450x300')
    audio_dialogue.title('Text to Voice')
    audio_dialogue.resizable(0,0)

    sidebar = Frame(audio_dialogue, width=200, bg='white', relief='flat')
    sidebar.pack(expand=False, fill=Y, side='left', anchor='nw')

    separator  = Frame(sidebar, bg='gray',height=1)
    separator1 = Frame(sidebar, bg='gray',height=1)
    separator2 = Frame(sidebar, bg='gray',height=1)
    separator3 = Frame(sidebar, bg='gray',height=1)
    

    speed_button = Button(sidebar,relief='flat', bg='brown', text=' Speed ',font=('Arial',20))
    speed_button.pack(ipadx=5,ipady=5)
    separator.pack(fill='x')

    volume_button = Button(sidebar,relief='flat', bg='brown', text=' Volume',font=('Arial',20))
    volume_button.pack(ipadx=5,ipady=5)
    separator1.pack(fill='x')

    gender_button = Button(sidebar,relief='flat', bg='brown', text=' Gender',font=('Arial',20))
    gender_button.pack(ipadx=5,ipady=5)
    separator2.pack(fill='x')

    save_button = Button(sidebar,relief='flat', bg='brown', text='  Save  ',font=('Arial',20))
    save_button.pack(ipadx=5,ipady=5)
    separator3.pack(fill='x')


    audio_dialogue.mainloop()

if __name__ == '__main__':
    audio()