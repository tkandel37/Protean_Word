import tkinter as tk 
from tkinter import ttk 
import file_menu
import edit_menu
import toolbar

main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.title('Protean Word')
main_application.wm_iconbitmap('icons/icon.ico')

#status bar not displaying properly bug fixed.

def statusbar():
    global status_bar
    status_bar = ttk.Label(main_application, text = 'Status Bar')  
    status_bar.pack(side=tk.BOTTOM)

statusbar()
############################################## main menu ###################################################


#main_menu.add_cascade(label='Color Theme', menu=color_theme)

#text editor defined to fix bug
text_editor = tk.Text(main_application,selectforeground="yellow",selectbackground="red",undo=True)  #bug fixed

##############################################  status bar ###################################################

#its defined and displayed above for  bug fix..

text_changed = False                                #bug fixed  while exit
def changed(event=None):
    if text_editor.edit_modified():
        text_changed = True                         #bug fixed  while exit
        words = len(text_editor.get(1.0, 'end').split())
        characters = len(text_editor.get(1.0, 'end-1c'))
        status_bar.config(text=f'Characters : {characters} Words : {words}')
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>', changed)


# -------------------------------------&&&&&&&& End  status bar &&&&&&&&&&& ----------------------------------


############################################## toolbar  ###################################################
tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill=tk.X)
toolbar.main(tool_bar,text_editor)

# -------------------------------------&&&&&&&& End toolbar  &&&&&&&&&&& ----------------------------------

############################################## main menu functinality ###################################################
#file menu 
main_menu = tk.Menu()
file_menu.main(main_application,text_editor,main_menu,text_changed)
edit_menu.main(main_application,text_editor,main_menu)
# -------------------------------------&&&&&&&& End main menu  functinality&&&&&&&&&&& ----------------------------------



####################################################### View ##############################################

view = tk.Menu(main_menu, tearoff=False)
main_menu.add_cascade(label='View', menu=view)

show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar,tool_bar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False 
    else :
        text_editor.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        show_toolbar = True 


def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False 
    else :
        statusbar()
        show_statusbar = True 


view.add_checkbutton(label='Tool Bar',onvalue=True, offvalue=0, variable = show_toolbar, compound=tk.LEFT, command=lambda:hide_toolbar())
view.add_checkbutton(label='Status Bar',onvalue=1, offvalue=False,variable = show_statusbar, compound=tk.LEFT, command=hide_statusbar)

####################################################### END_View ##############################################


############################################## text editor ###################################################

text_editor.config(wrap='word', relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)
text_editor.configure(font=('Arial', 12))

############################end text editor###############################3



main_application.config(menu=main_menu)
main_application.mainloop()