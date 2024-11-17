import sys
import time 
import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import colorchooser
from configparser import ConfigParser
from tkinter import font


class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Editortest")

        # Initialize configuration
        self.parser = ConfigParser()
        self.parser.read("saves.ini")

        # Initialize recent files
        self.recent_files = [self.parser.get("recents", f"r{i}") for i in range(5)]

        # Initialize GUI components
        self.init_gui()

    def init_gui(self):
        self.text = tk.Text(self.root)
        self.text.grid()
        self.load_configuration()

        # Used for creation of function used as command
        self.current_file_path = None

        # Menu bar
        self.menubar = tk.Menu(self.root)

        # File menu
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Open", command=self.openas)
        self.filemenu.add_command(label="SaveAs", command=self.saveas)
        self.filemenu.add_command(label="Save", command=self.save)

        self.recent_menu = tk.Menu(self.filemenu, tearoff=0)
        for recent_file in self.recent_files:
            self.recent_menu.add_command(label=recent_file, command=lambda rf=recent_file: self.openfile(rf))

        self.filemenu.add_cascade(label="Recent", menu=self.recent_menu)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.root.quit)

        # View menu
        self.viewmenu = tk.Menu(self.menubar, tearoff=0)
        self.fontmenu = tk.Menu(self.viewmenu, tearoff=0)
        self.sizemenu = tk.Menu(self.viewmenu, tearoff=0)

        self.viewmenu.add_cascade(label="FontType", menu=self.fontmenu)
        self.viewmenu.add_command(label="Font Color", command=self.change_font_color)
        self.viewmenu.add_cascade(label="Font Size", menu=self.sizemenu)
        self.viewmenu.add_separator()
        self.viewmenu.add_command(label="Background Colour", command=self.change_color)

        font_families = font.families()
        for font_family in font_families:
            self.fontmenu.add_command(label=font_family, command=lambda f=font_family: self.change_font(f))

        sizes = [8, 10, 12, 14, 16, 18, 20]
        for size in sizes:
            self.sizemenu.add_command(label=str(size), command=lambda s=size: self.change_font_size(s))

        # Add options to the menubar
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.menubar.add_cascade(label="View", menu=self.viewmenu)

        self.root.config(menu=self.menubar)

    def load_configuration(self):
        saved_text_color = self.parser.get("colors", "text_color")
        saved_background_color = self.parser.get("colors", "background_color")
        saved_font_type = self.parser.get("fonts", "font_type")
        saved_font_size = int(self.parser.get("fonts", "font_size"))

        self.text.config(bg=saved_background_color, fg=saved_text_color, font=(saved_font_type, saved_font_size))
        font_details = font.Font(family=saved_font_type, size=saved_font_size)
        self.text.config(font=font_details)

    def openas(self):
        current_file_path = filedialog.askopenfilename()
        self.current_file_path = current_file_path
        if current_file_path:
            with open(current_file_path, 'r') as file:
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, file.read())
        file_name = os.path.basename(current_file_path)
        self.root.title(f"Editortest -- {file_name}")

        self.update_recent(self.current_file_path)

    def saveas(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        file_name = os.path.basename(file_path)
        self.root.title(f"Editortest -- {file_name}")
        self.current_file_path = file_path

        self.show_popup()

        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text.get(1.0, tk.END))
        self.add_to_recent(self.current_file_path)

    def save(self):
        if self.current_file_path:
            with open(self.current_file_path, 'w+') as file:
                file.seek(0)
                file.write(self.text.get(1.0, tk.END))
            file_name = os.path.basename(self.current_file_path)
            self.root.title(f"Editortest -- {file_name}")
        else:
            self.saveas()
        self.add_to_recent(self.current_file_path)
        self.show_popup()

    def change_color(self):
        background_color_code = colorchooser.askcolor()[1]
        if background_color_code:
            self.text.config(bg=background_color_code)
            self.parser.set("colors", "background_color", background_color_code)
            with open("saves.ini", "w") as cfile:
                self.parser.write(cfile)

    def change_font_color(self):
        text_color_code = colorchooser.askcolor()[1]
        if text_color_code:
            self.text.config(fg=text_color_code)
            self.parser.set("colors", "text_color", text_color_code)
            with open("saves.ini", "w") as cfile:
                self.parser.write(cfile)

    def change_font_size(self, font_size):
        saved_font_type = self.parser.get("fonts", "font_type")
        self.text.config(font=(saved_font_type, font_size))
        self.parser["fonts"] = {"font_type": saved_font_type, "font_size": str(font_size)}
        with open("saves.ini", "w") as cfile:
            self.parser.write(cfile)

    def change_font(self, font_type):
        saved_font_size = int(self.parser.get("fonts", "font_size"))
        font_details = font.Font(family=font_type, size=saved_font_size)
        self.text.config(font=font_details)
        self.parser["fonts"] = {"font_type": font_type, "font_size": str(saved_font_size)}
        with open("saves.ini", "w") as cfile:
            self.parser.write(cfile)

    def add_to_recent(self, file_path):
        if file_path not in self.recent_files:
            self.recent_files.insert(0, file_path)
            self.recent_files = self.recent_files[:5]

    def update_recent(self, new_file):
        for i in range(4, 0, -1):
            self.parser.set("recents", f"r{i}", self.parser.get("recents", f"r{i-1}"))
        self.parser.set("recents", "r0", new_file)
        with open("saves.ini", "w") as cfile:
           
