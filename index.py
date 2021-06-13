import tkinter as tk 
from tkinter import ttk 
from tkinter import font, colorchooser, filedialog, messagebox
import os 

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

main_menu = tk.Menu()
#file icons

file = tk.Menu(main_menu, tearoff=False)



#####edit 
#edit icons 


edit = tk.Menu(main_menu, tearoff=False)


######## view icons 

view = tk.Menu(main_menu, tearoff=False)


######## color theme 


# cascade 
main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
#main_menu.add_cascade(label='Color Theme', menu=color_theme)


############################################## toolbar  ###################################################

tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill=tk.X)

## font box 
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width=30, textvariable=font_family, state='readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0, column=3, padx=5)


## size box 
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar, width=14, textvariable = size_var, state='readonly')
font_size['values'] = tuple(range(8,81))
font_size.current(4)
font_size.grid(row=0, column=4, padx=5)

## bold button 
bold_icon = tk.PhotoImage(file='icons/bold.png')
bold_btn = ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row=0, column=0, padx=5)

## italic button 
italic_icon = tk.PhotoImage(file='icons/italic.png')
italic_btn = ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0, column=1, padx=5)

## underline button 
underline_icon = tk.PhotoImage(file='icons/underline.png')
underline_btn = ttk.Button(tool_bar, image = underline_icon)
underline_btn.grid(row = 0, column=2, padx=5)

## font color button 
font_color_icon = tk.PhotoImage(file='icons/font_color.png')
font_color_btn = ttk.Button(tool_bar, image=font_color_icon)
font_color_btn.grid(row=0, column=8,padx=5)

## align left 
align_left_icon = tk.PhotoImage(file='icons/align_left.png')
align_left_btn = ttk.Button(tool_bar, image=align_left_icon)
align_left_btn.grid(row=0, column=5, padx=5)

## align center 
align_center_icon = tk.PhotoImage(file='icons/align_center.png')
align_center_btn = ttk.Button(tool_bar, image=align_center_icon)
align_center_btn.grid(row=0, column=6, padx=5)

## align right 
align_right_icon = tk.PhotoImage(file='icons/align_right.png')
align_right_btn = ttk.Button(tool_bar, image=align_right_icon)
align_right_btn.grid(row=0, column=7, padx=5)

# -------------------------------------&&&&&&&& End toolbar  &&&&&&&&&&& ----------------------------------

############################################## text editor ###################################################
text_editor = tk.Text(main_application,selectforeground="yellow",selectbackground="red",undo=True)
text_editor.config(wrap='word', relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# font family and font size functionality 
current_font_family = 'Arial'
current_font_size = 12

def change_font(event=None):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))

def change_fontsize(event=None):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family, current_font_size))


font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_fontsize)

######## buttons functionality

# italic functionlaity
def change_italic():

    text_editor.tag_remove("bold","sel.first","sel.last") #bug fixed while clicking simultaneously
    text_editor.tag_remove("underline","sel.first","sel.last") #bug fixed while clicking simultaneously

    #create font
    bold_font = font.Font(text_editor,text_editor.cget("font"))
    bold_font.configure(slant="italic")

    # creat tag
    text_editor.tag_configure("italic",font=bold_font)

    #if statement to set tag
    current_tags = text_editor.tag_names("sel.first")
    if "italic" in current_tags:
        text_editor.tag_remove("italic","sel.first","sel.last")
    else:
        text_editor.tag_add("italic","sel.first","sel.last")
    
italic_btn.configure(command=change_italic)

# underline functionality 
def change_underline():

    text_editor.tag_remove("bold","sel.first","sel.last") #bug fixed while clicking simultaneously
    text_editor.tag_remove("italic","sel.first","sel.last") #bug fixed while clicking simultaneously
    
    #create font
    underline_font = font.Font(text_editor,text_editor.cget("font"))
    underline_font.configure(underline=1)

    # creat tag
    text_editor.tag_configure("underline",font=underline_font)

    #if statement to set tag
    current_tags = text_editor.tag_names("sel.first")
    if "underline" in current_tags:
        text_editor.tag_remove("underline","sel.first","sel.last")
    else:
        text_editor.tag_add("underline","sel.first","sel.last")
    
underline_btn.configure(command=change_underline)

# bold button functionality
def change_bold():

    text_editor.tag_remove("underline","sel.first","sel.last") #bug fixed while clicking simultaneously
    text_editor.tag_remove("italic","sel.first","sel.last") #bug fixed while clicking simultaneously

    #create font
    bold_font = font.Font(text_editor,text_editor.cget("font"))
    bold_font.configure(weight="bold")

    # creat tag
    text_editor.tag_configure("bold",font=bold_font)

    #if statement to set tag
    current_tags = text_editor.tag_names("sel.first")
    if "bold" in current_tags:
        text_editor.tag_remove("bold","sel.first","sel.last")
    else:
        text_editor.tag_add("bold","sel.first","sel.last")
    
bold_btn.configure(command=change_bold)

## font color functionality 
def change_font_color():
    color_var = colorchooser.askcolor()[1]
    
    if color_var:
        #create font
        color_font = font.Font(text_editor,text_editor.cget("font"))
        # creat tag
        text_editor.tag_configure("color",font=color_font,foreground=color_var)

        #if statement to set tag
        current_tags = text_editor.tag_names("sel.first")
        if "color" in current_tags:
            text_editor.tag_remove("color","sel.first","sel.last")
        else:
            text_editor.tag_add("color","sel.first","sel.last")

font_color_btn.configure(command=change_font_color)

### align functionality 

def align_left():
    text_content = text_editor.get('sel.first','sel.last')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete('sel.first','sel.last')
    text_editor.insert(tk.INSERT, text_content, 'left')
align_left_btn.configure(command=align_left)

## center 
def align_center():
    text_content = text_editor.get('sel.first','sel.last')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete('sel.first','sel.last')
    text_editor.insert(tk.INSERT, text_content, 'center')

align_center_btn.configure(command=align_center)

## right 
def align_right():
    text_content = text_editor.get('sel.first','sel.last')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete('sel.first','sel.last')
    text_editor.insert(tk.INSERT, text_content, 'right')

align_right_btn.configure(command=align_right)



text_editor.configure(font=('Arial', 12))
# -------------------------------------&&&&&&&& End text editor &&&&&&&&&&& ----------------------------------


##############################################  status bar ###################################################

#its defined and displayed above for  bug fix..

text_changed = False                                #bug fixed  while exit

def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True                         #bug fixed  while exit
        words = len(text_editor.get(1.0, 'end').split())
        characters = len(text_editor.get(1.0, 'end-1c'))
        status_bar.config(text=f'Characters : {characters} Words : {words}')
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>', changed)


# -------------------------------------&&&&&&&& End  status bar &&&&&&&&&&& ----------------------------------


############################################## main menu functinality ###################################################

## variable 
url = ''

## new functionality
def new_file(event=None):
    global url 
    url = ''
    text_editor.delete(1.0, tk.END)

## file commands 
file.add_command(label='New', compound=tk.LEFT, accelerator='Ctrl+N', command=new_file)

## open functionality

def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return 
    except:
        return 
    main_application.title(os.path.basename(url))
    text_changed = False                             #bug fixed while exit

file.add_command(label='Open', compound=tk.LEFT, accelerator='Ctrl+O', command=open_file)

## save file 

def save_file(event=None):
    global url 
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            save_as()
    except:
        return 
    main_application.title(os.path.basename(url))

file.add_command(label='Save', compound=tk.LEFT, accelerator='Ctrl+S', command = save_file)


## save as functionality 
def save_as(event=None):
    global url 
    try:
        content = text_editor.get(1.0, tk.END)
        url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
        url.write(content)
        url.close()
    except:
        return 
    main_application.title(os.path.basename(url))

file.add_command(label='Save As', compound=tk.LEFT, accelerator='Ctrl+Shift+S', command=save_as)

## exit functionality 

def exit_func(event=None):
    global text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file ?')
            if mbox is True:
                save_file()
                main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return 
file.add_command(label='Exit', compound=tk.LEFT, accelerator='Ctrl+Q', command=exit_func)


#########################################################find functionality##############################################################

def find_func(event=None):

    def find():
        word = find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break 
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')
    
    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0,0)

    ## frame 
    find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
    find_frame.pack(pady=20)

    ## labels
    text_find_label = ttk.Label(find_frame, text='Find : ')
    text_replace_label = ttk.Label(find_frame, text= 'Replace')

    ## entry 
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    ## button 
    find_button = ttk.Button(find_frame, text='Find', command=find)
    replace_button = ttk.Button(find_frame, text= 'Replace', command=replace)

    ## label grid 
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    ## entry grid 
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    ## button grid 
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_dialogue.mainloop()

## edit commands 
edit.add_command(label='Copy', compound=tk.LEFT, accelerator='Ctrl+C', command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label='Paste', compound=tk.LEFT, accelerator='Ctrl+V', command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label='Cut',  compound=tk.LEFT, accelerator='Ctrl+X', command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label='Clear All',  compound=tk.LEFT, accelerator='Ctrl+Alt+X', command= lambda:text_editor.delete(1.0, tk.END))
edit.add_command(label='Find',  compound=tk.LEFT, accelerator='Ctrl+F', command = find_func)

## view check button 
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
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


view.add_checkbutton(label='Tool Bar',onvalue=True, offvalue=0,variable = show_toolbar, compound=tk.LEFT, command=hide_toolbar)
view.add_checkbutton(label='Status Bar',onvalue=1, offvalue=False,variable = show_statusbar, compound=tk.LEFT, command=hide_statusbar)

## color theme 




# -------------------------------------&&&&&&&& End main menu  functinality&&&&&&&&&&& ----------------------------------

main_application.config(menu=main_menu)

#### bind shortcut keys 
main_application.bind("<Control-n>", new_file)
main_application.bind("<Control-o>", open_file)
main_application.bind("<Control-s>", save_file)
main_application.bind("<Control-Shift-s>", save_as)
main_application.bind("<Control-q>", exit_func)
main_application.bind("<Control-f>", find_func)

main_application.mainloop()