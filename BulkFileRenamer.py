#! /usr/bin/env python
#  -*- coding: utf-8 -*-


import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
import threading
import webbrowser


class App:
    def __init__(self, root):
       
        _bgcolor = '#d9d9d9'  
        _fgcolor = '#000000'  
        _compcolor = '#d9d9d9'
        _ana1color = '#d9d9d9' 
        _ana2color = '#ececec'
        self.style = ttk.Style()

        root.geometry("820x600+329+146")
        root.resizable(0,  0)
        root.title("iTech®")
        root.configure(background="#d9d9d9")
        root.configure(highlightbackground="#d9d9d9")
        root.configure(highlightcolor="black")
        self.path = StringVar()
        self.extension = StringVar()
        self.newFilesNames = StringVar()

        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.TNotebook1 = ttk.Notebook(root)
        self.TNotebook1.place(relx=0.049, rely=0.133, relheight=0.763
                , relwidth=0.902)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t1_1_1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1_1_1, padding=3)
        self.TNotebook1.tab(0, text="Preferences", compound="left", underline="-1"
                ,)
        self.TNotebook1_t1_1_1.configure(relief="sunken")
        self.TNotebook1_t1_1_1.configure(background="#d9d9d9")
        self.TNotebook1_t1_1_1.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t1_1_1.configure(highlightcolor="black")
        self.TNotebook1_t2_1_1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2_1_1, padding=3)
        self.TNotebook1.tab(1, text="Help",compound="left",underline="-1",)
        self.TNotebook1_t2_1_1.configure(relief="sunken")
        self.TNotebook1_t2_1_1.configure(background="#d9d9d9")
        self.TNotebook1_t2_1_1.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t2_1_1.configure(highlightcolor="black")
        self.TNotebook1_t3_1_1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t3_1_1, padding=3)
        self.TNotebook1.tab(2, text="About",compound="none",underline="-1",)
        self.TNotebook1_t3_1_1.configure(relief="sunken")
        self.TNotebook1_t3_1_1.configure(background="#d9d9d9")
        self.TNotebook1_t3_1_1.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t3_1_1.configure(highlightcolor="black")

        self.path_entry = ttk.Entry(self.TNotebook1_t1_1_1)
        self.path_entry.place(relx=0.326, rely=0.095, relheight=0.073
                , relwidth=0.62)
        self.path_entry.configure(font="-family {Tahoma} -size 9")
        self.path_entry.configure(justify='center')
        self.path_entry.configure(takefocus="")
        self.path_entry.configure(cursor="ibeam")
        self.path_entry.configure(textvariable=self.path)

        self.extension_entry = ttk.Entry(self.TNotebook1_t1_1_1)
        self.extension_entry.place(relx=0.326, rely=0.261, relheight=0.073
                , relwidth=0.62)
        self.extension_entry.configure(font="-family {Tahoma} -size 9")
        self.extension_entry.configure(justify='center')
        self.extension_entry.configure(takefocus="")
        self.extension_entry.configure(cursor="ibeam")
        self.extension_entry.configure(textvariable=self.extension)

        self.new_files_names = ttk.Entry(self.TNotebook1_t1_1_1)
        self.new_files_names.place(relx=0.326, rely=0.427, relheight=0.073
                , relwidth=0.62)
        self.new_files_names.configure(font="-family {Tahoma} -size 9")
        self.new_files_names.configure(justify='center')
        self.new_files_names.configure(takefocus="")
        self.new_files_names.configure(cursor="ibeam")
        self.new_files_names.configure(textvariable=self.newFilesNames)

        self.result_output = tk.Label(self.TNotebook1_t1_1_1)
        self.result_output.place(relx=0.326, rely=0.758, height=67, width=457)
        self.result_output.configure(activebackground="#f9f9f9")
        self.result_output.configure(activeforeground="black")
        self.result_output.configure(background="#d9d9d9")
        self.result_output.configure(disabledforeground="#a3a3a3")
        self.result_output.configure(font="-family {Segoe UI Semibold} -size 10 -weight bold")
        self.result_output.configure(foreground="#000000")
        self.result_output.configure(highlightbackground="#d9d9d9")
        self.result_output.configure(highlightcolor="black")

        self.rename_button = tk.Button(self.TNotebook1_t1_1_1)
        self.rename_button.place(relx=0.326, rely=0.569, height=42, width=456)
        self.rename_button.configure(activebackground="#ececec")
        self.rename_button.configure(activeforeground="#000000")
        self.rename_button.configure(background="#d9d9d9")
        self.rename_button.configure(disabledforeground="#a3a3a3")
        self.rename_button.configure(foreground="#000000")
        self.rename_button.configure(highlightbackground="#d9d9d9")
        self.rename_button.configure(highlightcolor="black")
        self.rename_button.configure(pady="0")
        self.rename_button.configure(command=self._resetbutton())

        self.Label2 = tk.Label(self.TNotebook1_t1_1_1)
        self.Label2.place(relx=0.027, rely=0.095, height=33, width=56)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor='sw')
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(justify='left')
        self.Label2.configure(text='''Path''')

        self.Label2_1 = tk.Label(self.TNotebook1_t1_1_1)
        self.Label2_1.place(relx=0.027, rely=0.261, height=33, width=86)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(anchor='sw')
        self.Label2_1.configure(background="#d9d9d9")
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(foreground="#000000")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(justify='left')
        self.Label2_1.configure(text='''Extension''')

        self.Label2_2 = tk.Label(self.TNotebook1_t1_1_1)
        self.Label2_2.place(relx=0.027, rely=0.427, height=33, width=146)
        self.Label2_2.configure(activebackground="#f9f9f9")
        self.Label2_2.configure(activeforeground="black")
        self.Label2_2.configure(anchor='sw')
        self.Label2_2.configure(background="#d9d9d9")
        self.Label2_2.configure(disabledforeground="#a3a3a3")
        self.Label2_2.configure(foreground="#000000")
        self.Label2_2.configure(highlightbackground="#d9d9d9")
        self.Label2_2.configure(highlightcolor="black")
        self.Label2_2.configure(text='''New Files Names''')

        self.help_text = ScrolledText(self.TNotebook1_t2_1_1)
        self.help_text.place(relx=0.014, rely=0.118, relheight=0.836
                , relwidth=0.957)
        self.help_text.configure(background="white")
        self.help_text.configure(font="TkTextFont")
        self.help_text.configure(foreground="black")
        self.help_text.configure(highlightbackground="#d9d9d9")
        self.help_text.configure(highlightcolor="black")
        self.help_text.configure(insertbackground="black")
        self.help_text.configure(insertborderwidth="3")
        self.help_text.configure(selectbackground="blue")
        self.help_text.configure(selectforeground="white")
        self.help_text.configure(wrap="none")
        self.help_text.insert(tk.END, '''
        
        Bulk Files Renamer helps you renaming thousands files in few seconds!

        Thanks to Python Threading technique!

        • What should I input in Path?

        You should input the folder directory, where your files are located.

        Example:  C:/Users/user/Desktop/Folder/

        Hint: In windows, you should replace all Backslash with Forward Slash
        and add another Forward Slash after the folder name like the following.

        Wrong path input:       C:\\Users\\user\\Desktop\\folder

        Correct path input:   C:/Users/user/Desktop/folder/


        • What should I input in extension?

        You should input the extension of the files your are willing to rename.

        Input example: txt, pdf, doc, exe ect..


        • What should I input in New Files names?

        You should input the name which will be used for all files with the same extension.

        Exemple: Let's suppose you have multiple xlsx files which are related to a single project
        of a Hotel financial report, simply input Hotel or the hotel's name.
        
        ''')
        self.help_text.configure(state='disabled')


        self.linkedin = tk.Button(self.TNotebook1_t3_1_1)
        self.linkedin.place(relx=0.261, rely=0.498, height=42, width=378)
        self.linkedin.configure(activebackground="#ececec")
        self.linkedin.configure(activeforeground="#000000")
        self.linkedin.configure(background="#d9d9d9")
        self.linkedin.configure(disabledforeground="#a3a3a3")
        self.linkedin.configure(foreground="#000000")
        self.linkedin.configure(highlightbackground="#d9d9d9")
        self.linkedin.configure(highlightcolor="black")
        self.linkedin.configure(pady="0")
        self.linkedin.configure(text='''LinkedIn''')
        self.linkedin.configure(command=lambda:self.linked_in())

        self.github = tk.Button(self.TNotebook1_t3_1_1)
        self.github.place(relx=0.261, rely=0.659, height=42, width=378)
        self.github.configure(activebackground="#ececec")
        self.github.configure(activeforeground="#000000")
        self.github.configure(background="#d9d9d9")
        self.github.configure(disabledforeground="#a3a3a3")
        self.github.configure(foreground="#000000")
        self.github.configure(highlightbackground="#d9d9d9")
        self.github.configure(highlightcolor="black")
        self.github.configure(pady="0")
        self.github.configure(text='''Github''')
        self.github.configure(command=lambda:self.git_hub())

        self.website = tk.Button(self.TNotebook1_t3_1_1)
        self.website.place(relx=0.261, rely=0.801, height=42, width=378)
        self.website.configure(activebackground="#ececec")
        self.website.configure(activeforeground="#000000")
        self.website.configure(background="#d9d9d9")
        self.website.configure(disabledforeground="#a3a3a3")
        self.website.configure(foreground="#000000")
        self.website.configure(highlightbackground="#d9d9d9")
        self.website.configure(highlightcolor="black")
        self.website.configure(pady="0")
        self.website.configure(text='''Website''')
        self.website.configure(command=lambda:self.portfolio())

        self.about_text = tk.Label(self.TNotebook1_t3_1_1)
        self.about_text.place(relx=0.149, rely=0.142, height=111, width=567)
        self.about_text.configure(activebackground="#f9f9f9")
        self.about_text.configure(activeforeground="black")
        self.about_text.configure(background="#d9d9d9")
        self.about_text.configure(disabledforeground="#a3a3a3")
        self.about_text.configure(font="verdana")
        self.about_text.configure(foreground="#000000")
        self.about_text.configure(highlightbackground="#d9d9d9")
        self.about_text.configure(highlightcolor="black")
        self.about_text.configure(text="By iTech® 2021")

        self.title = tk.Label(root)
        self.title.place(relx=0.098, rely=0.017, height=51, width=667)
        self.title.configure(activebackground="#f9f9f9")
        self.title.configure(activeforeground="black")
        self.title.configure(background="#d9d9d9")
        self.title.configure(disabledforeground="#a3a3a3")
        self.title.configure(font="-family {Eras Demi ITC} -size 14")
        self.title.configure(foreground="#000000")
        self.title.configure(highlightbackground="#d9d9d9")
        self.title.configure(highlightcolor="black")
        self.title.configure(text='''Bulk Files Renamer''')

    def rename_files(self):

        try:

            my_path = self.path.get()
            filenames = os.listdir(my_path)
            my_extension = "." + self.extension.get()
            new_files_names = self.newFilesNames.get()
                
            for file in range(len(filenames)):            

                if filenames[file].endswith(my_extension):
                    
                    new_names = my_path + new_files_names + str(file) + my_extension
                    src = my_path + filenames[file]         
                    os.rename(src, new_names)
                            
            self.result_output.configure(text="done!")
            
        except OSError:
            self.result_output.configure(text="Looks like there is wrong input! Please check and try again!")

        except Exception:
            self.result_output.configure(text="Unexpected error occured! Please try again!")

    def linked_in(self):
        url='https://linkedin.com/in/cyber-services'
        webbrowser.open_new_tab(url)

    def git_hub(self):
        url='https://github.com/IT-Support-L2'
        webbrowser.open_new_tab(url)

    def portfolio(self):
        url='https://hamdi-bouaskar.herokuapp.com'
        webbrowser.open_new_tab(url)

    def _resetbutton(self):
            self.running = False
            self.rename_button.config(text="Start", command=self.startthread)

    def startthread(self):
        self.running = True
        newthread = threading.Thread(target=self.StartTask)
        newthread.start()
        self.rename_button.configure(text="Stop", command=self._resetbutton)

    def StartTask(self):
        if self.running:
            self.rename_files()
               


class AutoScroll(object):
    def __init__(self, master):
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledText(AutoScroll, tk.Text):
    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0] 
    child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
    child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
   

def _unbound_to_mousewheel(event, widget):
    
    widget.unbind_all('<MouseWheel>')
    widget.unbind_all('<Shift-MouseWheel>')
    

def _on_mousewheel(event, widget):
    
    widget.yview_scroll(-1*int(event.delta/120),'units')
   

def _on_shiftmouse(event, widget):
    
    widget.xview_scroll(-1*int(event.delta/120), 'units')

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()





