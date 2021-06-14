import tkinter as tk 
from tkinter import filedialog, messagebox
import os




def main(main_application,text_editor,main_menu,text_change):

    file = tk.Menu(main_menu, tearoff=False)
    main_menu.add_cascade(label='File', menu=file)


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
        global url, text_changed
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
        try:
            global url
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

    main_application.bind("<Control-n>", new_file)
    main_application.bind("<Control-o>", open_file)
    main_application.bind("<Control-s>", save_file)
    main_application.bind("<Control-Shift-s>", save_as)
    main_application.bind("<Control-q>", exit_func)