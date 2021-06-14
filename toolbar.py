import tkinter as tk 
from tkinter import ttk 
from tkinter import font, colorchooser

def main(tool_bar,text_editor):
    
    ## font box 
    font_tuple = font.families()
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
    bold_btn = ttk.Button(tool_bar,image=bold_icon)
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

        # font family and font size functionality 
    

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