import tkinter as tk 
from tkinter import ttk 




def main(main_application,text_editor,main_menu):


    edit = tk.Menu(main_menu, tearoff=False)
    main_menu.add_cascade(label='Edit', menu=edit)

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

    
    main_application.bind("<Control-f>", find_func)