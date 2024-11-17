import sys
import time
import os
import tkinter as tk
from tkinter import  *
from tkinter import filedialog
from tkinter import colorchooser
from configparser import ConfigParser
from tkinter import font
 



#Reads the config file and loads the default value of values
parser = ConfigParser()

parser.read("saves.ini")
saved_text_color = parser.get("colors","text_color")
saved_background_color = parser.get("colors","background_color")
saved_font_type = parser.get("fonts","font_type")
saved_font_size = parser.get("fonts", "font_size")
recent_file0 = parser.get("recents","r0")
recent_file1 = parser.get("recents","r1")
recent_file2 = parser.get("recents","r2")
recent_file3 = parser.get("recents","r3")
recent_file4 = parser.get("recents","r4")

root = tk.Tk("Text editor")
text = tk.Text(root)

text.grid()
text.config(bg =saved_background_color,fg = saved_text_color ,font = (saved_font_type, saved_font_size))
font_details = font.Font(family = saved_font_type,size = saved_font_size)

#Used for creation of function used as command
c_file_path = None
def openas():

	current_file_path = filedialog.askopenfilename()
	global c_file_path
	c_file_path= current_file_path
	if(current_file_path):
		with open(current_file_path,'r') as file:

			text.delete(1.0,tk.END)
			text.insert(tk.END,file.read())
	file_name = os.path.basename(current_file_path)
	root.title(f"Editortest --{file_name}")


	update_recent(c_file_path)







def show_popup():
	global c_file_path
	file_name = os.path.basename(c_file_path)


	popup = tk.Toplevel(root)
	popup.title("File Saved")

	label = tk.Label(popup, text=f"{file_name} saved")

	label.pack(padx=10, pady=10)

	popup.after(1000, popup.destroy)

def saveas():
	global c_file_path
	file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
	file_name = os.path.basename(file_path)
	root.title(f"Editortest -- {file_name}")
	c_file_path = file_path
	#Creates a popup that shows that the file has been saved

	show_popup()


	if file_path:
		with open(file_path, 'w') as file:
			file.write(text.get(1.0, tk.END))
	add_to_recent(c_file_path)


def save():
	global c_file_path
	if c_file_path:

		with open(c_file_path, 'w+') as file:

			file.seek(0)
			file.write(text.get(1.0,tk.END))


		file_name = os.path.basename(c_file_path)
		root.title(f"Editortest -- {file_name}")
	else:
		saveas()
	add_to_recent(c_file_path)


	show_popup()

def change_color():
	background_color_code = colorchooser.askcolor()[1]
	if background_color_code:
		text.config(bg = background_color_code )
		#Saving in the config file

		parser = ConfigParser()
		parser.read("saves.ini")
		parser.set("colors","background_color", background_color_code)
		#Writing into the config file

		with open("saves.ini", "w") as cfile:
			parser.write(cfile)

def change_font_color():
	text_color_code = colorchooser.askcolor()[1]
	if text_color_code:
		text.config(fg = text_color_code)



		#Saving in the config file

		parser = ConfigParser()
		parser.read("saves.ini")
		parser.set("colors","text_color", text_color_code)
		#Writing into the config file

		with open("saves.ini", "w") as cfile:
			parser.write(cfile)


def change_font_size(font_size):
	global saved_font_type

	text.config(font = (saved_font_type,font_size))

	#Saving in the config file

	parser = ConfigParser()
	parser.read("saves.ini")
	parser["fonts"]= {"font_type":saved_font_type,"font_size" :font_size}
	#Writing into the config file

	with open("saves.ini", "w") as cfile:
		parser.write(cfile)



def change_font(font_type):
	global saved_font_size
	global font_details
	font_details.configure(family = font_type,size= saved_font_size)
	text.config(font = font_details)
	#Saving font type

	config = ConfigParser()
	config.read("saves.ini")
	config['fonts'] = {'font_type': font_type, 'font_size': saved_font_size}
	with open("saves.ini", 'w') as cfile:
		config.write(cfile)


def add_to_recent(file_path):
	global recent_files
	if file_path not in recent_files:
		recent_files.insert(0,file_path)
		recent_files = recent_files[:5]



def update_recent(new_file):
	global recent_file0
	global recent_file1
	global recent_file2
	global recent_file3
	global recent_file4
	recent_file4 = recent_file3
	recent_file3 = recent_file2
	recent_file2 = recent_file1
	recent_file1 = recent_file0
	recent_file0 =  new_file
	parser = ConfigParser()
	parser.read("saves.ini")
	parser.set("recents","r1", recent_file1)
	parser.set("recents","r0",recent_file0)
	parser.set("recents","r2",recent_file2)
	parser.set("recents","r3",recent_file3)
	parser.set("recents","r4",recent_file4)
	#Writing into the config file

	with open("saves.ini", "w") as cfile:
		parser.write(cfile)
	print("File has been updated")


def openfile(file_path):

	if(file_path):
		with open(file_path,'r') as file:

			text.delete(1.0,tk.END)
			text.insert(tk.END,file.read())
	file_name = os.path.basename(file_path)
	root.title(f"Editortest --{file_name}")



root.title("Editortest")

#Used for creating the menu bar


menubar = tk.Menu(root)


#used for creating the contents of the file menu
filemenu = tk.Menu(menubar,tearoff = 0)
filemenu.add_command(label = "Open", command = openas)
filemenu.add_command(label = "SaveAs", command = saveas)
filemenu.add_command(label = "Save", command = save)
recent_menu = tk.Menu(filemenu,tearoff = 0)

recent_menu.add_command(label = recent_file0, command =lambda:openfile(recent_file0))
recent_menu.add_command(label = recent_file1, command = lambda:openfile(recent_file1))
recent_menu.add_command(label = recent_file2, command = lambda:openfile(recent_file2))
recent_menu.add_command(label = recent_file3, command = lambda:openfile(recent_file3))
recent_menu.add_command(label = recent_file4, command = lambda:openfile(recent_file4))

filemenu.add_cascade(label = "Recent", menu = recent_menu)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = root.quit)


#used for creating the contents of view menu
viewmenu = tk.Menu(menubar,tearoff = 0)
fontmenu = tk.Menu(viewmenu, tearoff = 0)


sizemenu = tk.Menu(viewmenu,tearoff= 0)
#Used for the cascading font option
viewmenu.add_cascade(label = "FontType" , menu = fontmenu)
viewmenu.add_command(label = "Font Color", command = change_font_color)
viewmenu.add_cascade(label = "Font Size" , menu = sizemenu )
viewmenu.add_separator()
viewmenu.add_command(label = "Background Colour", command = change_color)


#Used for the font menu

 # Get all available font families
font_families = font.families()
# Add each font family to the menu
for font_family in font_families:
	fontmenu.add_command(label=font_family, command=lambda f=font_family:change_font(f))



#Used for the size menu
sizemenu.add_command(label = "8", command = lambda:change_font_size(8))
sizemenu.add_command(label = "10", command = lambda:change_font_size(10))
sizemenu.add_command(label = "12", command = lambda:change_font_size(12))
sizemenu.add_command(label = "14", command = lambda:change_font_size(14))
sizemenu.add_command(label = "16", command = lambda:change_font_size(16))
sizemenu.add_command(label = "18", command = lambda:change_font_size(18))
sizemenu.add_command(label = "20", command = lambda:change_font_size(20))

#adds the following options to the menubar

menubar.add_cascade(label = "File", menu = filemenu)
menubar.add_cascade(label = "View", menu = viewmenu)
root.config(menu=menubar)

root.mainloop()

