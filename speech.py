from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox
from typing import MutableMapping
from s_fileread import file_change,file_read
import pyttsx3



################################# playing audio ####################################
def audio_play(text):
        engine = pyttsx3.init()
        engine.setProperty('rate',int(file_read(0)))
        engine.setProperty('volume',int(file_read(1))/10)   
        voices = engine.getProperty('voices')
        engine.setProperty('voice',voices[int(file_read(2))].id)
        engine.say(text)
        engine.runAndWait()
 
#################################### saving the file ###################################
def audio_save(text):
        global audio_dialogue
        url = filedialog.asksaveasfilename(defaultextension='.mp3', filetypes=(
        ('Mp3 file', '*.mp3'),
        ('Mp4 file', '*.mp4'),
        ('M4a file', '*.m4a'),
        ('AAC file', '*.aac'),
        ('WAV file', '*.wav'),
        ('FLAC file', '*.flac'),
        ('3GPP file', '*.3gp'),
        ('WMA file', '*.wma'),))

        if url:
            save_audio = pyttsx3.init()
            save_audio.setProperty('rate',int(file_read(0)))
            save_audio.setProperty('volume',int(file_read(1)))    
            voices = save_audio.getProperty('voices')
            save_audio.setProperty('voice',voices[int(file_read(2))].id)
            save_audio.save_to_file(text,url)
            save_audio.runAndWait()

        else:
            return

        speed = str(int((int(file_read(0))-100)/10))
        volume = file_read(1)
        gender = file_read(2)

        if gender == 0:
            gender = 'Male'
        else:
            gender = 'Female'
        
        messagebox.showinfo("Audio File Saved", f"Audio saved with following settings: \n\n Speed: {speed} \n Volume: {volume} \n Gender: {gender}")
        audio_dialogue.destroy() #closing main box

#########################################################################################################
def audio_setting(text):
    global audio_dialogue
    audio_dialogue = Tk()  
    audio_dialogue.geometry('450x300')
    audio_dialogue.title('Text to Voice')
    audio_dialogue.wm_iconbitmap('icons/icon.ico')
    #audio_dialogue.overrideredirect(1)

    audio_dialogue.resizable(0,0)

    ################ Function of Leftside button ############
    global _speed
    global _volume
    global _gender
    global _save

    _speed = 'True'
    _volume = 'True'
    _gender = 'True'
    _save = 'True'

    
    def speed():
        global _speed
        global speed_bar
        speed_bar = ttk.Scale(speed_content_box, from_=0, to=20, orient=HORIZONTAL, value=int((int(file_read(0))-100)/10), length=200)
        speed_text_slider = Label(speed_content_box,text='Speed: ' + str(int((int(file_read(0))-100)/10)))

        if _speed == 'True':
            speed_content_box.pack()
            _speed = 'else'
            speed_button.config(bg='Green',state=DISABLED,disabledforeground="white")

            def speed_value(x):
                a='Speed: '
                speed_text_slider.config(text=a+str(int(speed_bar.get())))

            speed_bar.config(command=speed_value)    
            speed_bar.pack()
            speed_text_slider.pack(pady=3)


           

    def volume():
        global _volume
        global volume_bar
        volume_bar = ttk.Scale(volume_content_box, from_=0, to=10, orient=HORIZONTAL, value=int(file_read(1)), length=200)
        volume_text_slider = Label(volume_content_box,text='Volume: ' + file_read(1))

        if _volume == 'True':
            volume_content_box.pack()
            _volume = 'else'
            volume_button.config(bg='Green',state=DISABLED,disabledforeground="white")

            def volume_value(x):
                a = 'Volume: '
                volume_text_slider.config(text=a+str(int(volume_bar.get())))

            volume_bar.config(command=volume_value)    
            volume_bar.pack()
            volume_text_slider.pack(pady=3)
     
    def gender():
        global _gender
        global select_gender
        select_gender = Button(gender_content_box, relief='flat', text=' ',
                        width=15,font=('Arial',12),fg='white',activeforeground='white')

        def button_display(x):
            if x == 0:
                select_gender.config (bg='#FF1493',activebackground='#FF1493',text='Female',command=lambda:button_display(1))
                file_change('1',2)               
            else:
                select_gender.config (bg='Blue',activebackground='Blue', text='Male',command=lambda:button_display(0))
                file_change('0',2)

        if _gender == 'True':
            gender_content_box.pack()
            _gender = 'else'
            gender_button.config(bg='Green',state=DISABLED,disabledforeground="white")
            gender_number = int(file_read(2))

            if gender_number == 1:
                select_gender.config (bg='#FF1493',activebackground='#FF1493',text='Female',command=lambda:button_display(1))
            
            else:
                select_gender.config (bg='Blue',activebackground='Blue', text='Male',command=lambda:button_display(0))
            
            select_gender.pack(ipady=2,pady=5)

        
#################### END Function of Leftside button ############

#################### Apply and Reset ##################################
    
    def apply_button(event=None):
        global speed_bar,volume_bar,select_gender

        speed_value = str((int(speed_bar.get())*10) + 100)
        file_change(speed_value,0)
       
        volume_value = str(int(volume_bar.get()))
        file_change(volume_value,1)
            

    def reset_button(event=None):
        audio_dialogue.destroy()
        file_change('160',0)
        file_change('8',1)
        file_change('0',2)
        audio_setting(text)

    def hover_reset(event=None):
        reset.config(fg='white')
    def hovered_reset(event=None):
        reset.config(fg='black')   

    def hover_apply(event=None):
        apply.config(fg='white')
    def hovered_apply(event=None):
        apply.config(fg='black')   

   ################ END Save and Reset ##############################


     ######### TOP BAR ############################
    top_bar = Frame(audio_dialogue,height=31,bg='skyblue')
    top_bar.pack(side=TOP,fill=X)

    txt = Label(top_bar, text='Text to speech audio manager',bg='skyblue')
    txt.pack(side=LEFT,ipady=5,padx=10)

    apply = Label(top_bar, text='Apply', bg='skyblue')
    apply.pack(side=RIGHT,ipady=5,padx=10)

    reset = Label(top_bar, text='Reset',bg='skyblue')
    reset.pack(side=RIGHT,ipady=5)
    
    ######### Bottom bar #########################
    bottom_bar = Frame(audio_dialogue,height=41,bg='green')
    bottom_bar.pack(side=BOTTOM,fill=X)

    play = Button(bottom_bar,relief='flat', bg='green', height=2, text=' Play ',command=lambda:audio_play(text))
    play.pack(fill=X)

    ######### Left Bar ###########################
    left_bar = Frame(audio_dialogue, bg='purple')
    left_bar.pack(side=LEFT,anchor=N)

    separator  = Frame(left_bar, bg='gray',height=1)
    separator1 = Frame(left_bar, bg='gray',height=1)
    separator2 = Frame(left_bar, bg='gray',height=1)
    separator3 = Frame(left_bar, bg='gray',height=1)

    speed_button = Button(left_bar,relief='flat', bg='purple', width=8, 
    activebackground='purple', activeforeground='white',text='Speed',
    fg='white',  font=('Arial',20), command=speed)
    speed_button.pack()
    separator.pack(fill='x')

    volume_button = Button(left_bar,relief='flat', bg='purple', width=8, 
    activebackground='purple', activeforeground='white',text='Volume',
    fg='white',  font=('Arial',20), command=volume)
    volume_button.pack()
    separator1.pack(fill='x')

    gender_button = Button(left_bar,relief='flat', bg='purple', width=8, 
    activebackground='purple', activeforeground='white',text='Gender',
    fg='white',  font=('Arial',20), command=gender)
    gender_button.pack()
    separator2.pack(fill='x')

    save_button = Button(left_bar,relief='flat', bg='purple', width=8, 
    activebackground='purple', activeforeground='white',text='Save',
    fg='white',  font=('Arial',20), command=lambda:audio_save(text))
    save_button.pack()
    separator3.pack(fill='x')

    ######### Content for different ###########################
    speed_content_box = Frame(audio_dialogue,height=228,width=350)
    volume_content_box = Frame(audio_dialogue,height=228,width=350)
    gender_content_box = Frame(audio_dialogue,height=228,width=350)

    ################################# Binding ######################
    apply.bind("<Button-1>", apply_button)
    reset.bind("<Button-1>", reset_button)

    apply.bind("<Enter>", hover_apply)
    apply.bind("<Leave>", hovered_apply)

    reset.bind("<Enter>", hover_reset)
    reset.bind("<Leave>", hovered_reset)
    
    audio_dialogue.mainloop()


if __name__ == '__main__':
    audio_setting('Trilochan kandel')