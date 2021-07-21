from tkinter import *

root = Tk()
root.title('Audio')
root.geometry('400x400')

my_list = Listbox(root)
my_list.pack(pady=15)

#add items in list box
my_list.insert(END,"Speed")
my_list.insert(END,"volume")
my_list.insert(END,"Gender")
my_list.insert(END,"Save")
root.mainloop()

