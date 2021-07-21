import os
<<<<<<< HEAD
############################################## File handling  ###############################################
=======
############################################## File handling  ##############################################
>>>>>>> 1c036d88e5d97db77a312e9a7d2c1adb185782ab
#only reading file  ###returs the value
def file_read(index):                 
    file_path = os.path.isfile("system/speech.pw")
    def read():
        global value
        with open("system/speech.pw",'r') as f:
            text_list = f.readlines()
            value = text_list[index].strip()
        return value 
    if file_path:
        return read()
    else:
        with  open('system/speech.pw','w') as f:
            a = ["5\n","8\n","0\n"]
            for i in a:
                f.write(i)
        return read()
    
#reading and writing file
def file_change(text,index):
    file_path = os.path.isfile("system/speech.pw")

    def change():
        a = []
        with open('system/speech.pw','r') as f:
            a = f.readlines()
            a[index] = text + "\n"
        with open('system/speech.pw','w') as g:
            for i in a:
                g.write(i)

    if file_path:
        change()
    else:
        with  open('system/speech.pw','w') as f:
            a = ["5\n","8\n","0\n"]
            for i in a:
                f.write(i)
        change() 
############################################## End File handling  ##########################################

if __name__ == '__main__':
    file_change('8',1)