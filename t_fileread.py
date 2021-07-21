import os
############################################## File handling  ##############################################
#only reading file  ###returs the value
def file_read(index):                 
    file_path = os.path.isfile("system/style.pw")
    def read():
        global value
        with open("system/style.pw",'r') as f:
            text_list = f.readlines()
            value = text_list[index].strip()
        return value 
    if file_path:
        return read()
    else:
        with  open('system/style.pw','w') as f:
            a = ["Arial\n","12\n","#ffffff\n","#000000\n"]
            for i in a:
                f.write(i)
        return read()
    
<<<<<<< HEAD
##reading and writing file
=======
#reading and writing file
>>>>>>> 1c036d88e5d97db77a312e9a7d2c1adb185782ab
def file_change(text,index):
    file_path = os.path.isfile("system/style.pw")

    def change():
        a = []
        with open('system/style.pw','r') as f:
            a = f.readlines()
            a[index] = text + "\n"
        with open('system/style.pw','w') as g:
            for i in a:
                g.write(i)

    if file_path:
        change()
    else:
        with  open('system/style.pw','w') as f:
            a = ["Arial\n","12\n","#ffffff\n","#000000\n"]
            for i in a:
                f.write(i)
        change() 
############################################## End File handling  ##########################################