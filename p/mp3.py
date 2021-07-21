import pyttsx3
from tkinter import *
from tkinter import filedialog

root = Tk()


def say():
    

    engine = pyttsx3.init()
    a = 'I love Nepal'
    engine.say(a)
    # url = filedialog.askdirectory(parent=root,initialdir="/",title='Save audio in',)
    # k = '/apple.mp3'
    # ok = url + k
    # print(ok)
    filename = filedialog.asksaveasfilename(defaultextension='.mp3', filetypes=(
        ('Mp3 file', '*.mp3'),
        ('Mp4 file', '*.mp4'),
        ('M4a file', '*.m4a'),
        ('AAC file', '*.aac'),
        ('WAV file', '*.wav'),
        ('FLAC file', '*.flac'),
        ('3GPP file', '*.3gp'),
        ('WMA file', '*.wma'),))

    engine.save_to_file(a,filename)
    engine.runAndWait()
    #print(url)

a = Button(root,command=say, text='Say')
a.pack()


root.mainloop()

# mp3 mp4 wav aac m4a flac wma 