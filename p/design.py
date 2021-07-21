from tkinter import *
from tkinter import ttk

def audio():
    audio_dialogue = Toplevel()
    audio_dialogue.attributes('-topmost','true')
    audio_dialogue.geometry('450x300')
    audio_dialogue.title('Text to Voice')
    audio_dialogue.resizable(0,0)

    ######### TOP BAR#############################
    top_bar = Frame(audio_dialogue,height=30,bg='gray')
    top_bar.pack(side=TOP,fill=X)
    
    ######### Bottom bar #########################
    bottom_bar = Frame(audio_dialogue,height=40,bg='gray')
    bottom_bar.pack(side=BOTTOM,fill=X)

    ######### Left Bar############################
    left_bar = Frame(audio_dialogue)
    left_bar.pack(side=LEFT)

    separator  = Frame(left_bar, bg='gray',height=1)
    separator1 = Frame(left_bar, bg='gray',height=1)
    separator2 = Frame(left_bar, bg='gray',height=1)
    separator3 = Frame(left_bar, bg='gray',height=1)
    
    #speed
    speed_frame = Frame(left_bar,relief='flat',  bg='white')
    speed_frame.pack()
    separator.pack(fill=X)

    speed_text=Label(speed_frame,text="Speed",background='white')
    speed_text.pack(fill=BOTH, anchor="center")

    #volume
    volume_frame = Frame(left_bar,relief='flat', height=57.5, width=98, bg='white')
    volume_frame.pack()
    separator1.pack(fill=X)

    #gender
    gender_frame = Frame(left_bar,relief='flat', height=57.5, width=98, bg='white')
    gender_frame.pack()
    separator2.pack(fill=X)

    #save file
    save_frame = Frame(left_bar,relief='flat', height=57.5, width=98, bg='white')
    save_frame.pack()
    separator3.pack(fill=X)

    ######### Content ###########################
    content_box = Frame(audio_dialogue,height=230,width=350,bg='green')
    content_box.pack()

    

    audio_dialogue.mainloop()

if __name__ == '__main__':
    audio()