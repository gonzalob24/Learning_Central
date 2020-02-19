import tkinter as tk
from tkinter import ttk # create GUI Window
from tkinter import messagebox # yes no questions
from tkinter import simpledialog # single value data entry
from tkinter import filedialog # file chooser, selecting a file
import os
from tkinter import colorchooser # select a color


# creates the application window
#window = tk.Tk()
#rgb_color, web_color = colorchooser.askcolor(parent=window, initialcolor=(255, 0, 0))

# Creates the user interface
#my_label = ttk.Label(window, text = "Whats up!")
#my_label.grid(row=1, column=1)


def message():
    messagebox.showinfo("Information","Informative message")
    messagebox.showerror("Error", "Error message")
    messagebox.showwarning("Warning","Warning ")


def yes_no():
    answer = messagebox.askokcancel("Question","Do you want to open this file?")
    answer = messagebox.askretrycancel("Question", "Do you want to try that again?")
    answer = messagebox.askyesno("Question","Do you like Python?")
    answer = messagebox.askyesnocancel("Question", "Continue playing?")


def value_entry():
    application_window = tk.Tk()

    answer = simpledialog.askstring("Input", "What is your first name?",
                                    parent=application_window)
    if answer is not None:
        print("Your first name is ", answer)
    else:
        print("You don't have a first name?")

    answer = simpledialog.askinteger("Input", "What is your age?",
                                     parent=application_window,
                                     minvalue=0, maxvalue=100)
    if answer is not None:
        print("Your age is ", answer)
    else:
        print("You don't have an age?")

    answer = simpledialog.askfloat("Input", "What is your salary?",
                                   parent=application_window,
                                   minvalue=0.0, maxvalue=100000.0)
    if answer is not None:
        print("Your salary is ", answer)
    else:
        print("You don't have a salary?")

def file_chooser():
    application_window = tk.Tk()

    # Build a list of tuples for each file type the file dialog should display
    my_filetypes = [('all files', '.*'), ('text files', '.txt')]

    # Ask the user to select a folder.
    answer = filedialog.askdirectory(parent=application_window,
                                     initialdir=os.getcwd(),
                                     title="Please select a folder:")

    # Ask the user to select a single file name.
    answer = filedialog.askopenfilename(parent=application_window,
                                        initialdir=os.getcwd(),
                                        title="Please select a file:",
                                        filetypes=my_filetypes)

    # Ask the user to select a one or more file names.
    answer = filedialog.askopenfilenames(parent=application_window,
                                         initialdir=os.getcwd(),
                                         title="Please select one or more files:",
                                         filetypes=my_filetypes)

    # Ask the user to select a single file name for saving.
    answer = filedialog.asksaveasfilename(parent=application_window,
                                          initialdir=os.getcwd(),
                                          title="Please select a file name for saving:",
                                          filetypes=my_filetypes)
def my_function():
  print("my_function was called.")

#my_button = tk.Button(application_window, text="Example", command=my_function)

# or

#my_button = tk.Button(application_window, text="Example")
#my_button['command'] = my_function

def hello_world():
    # Create the application window
    window = tk.Tk()

    # Create the user interface
    my_label = ttk.Label(window, text="Hello World")
    my_label.grid(row=1, column=1)

    quit_button = ttk.Button(window, text="Quit")
    quit_button.grid(row=2, column=1)
    quit_button['command'] = window.destroy

    # Start the GUI event loop
    window.mainloop()

hello_world()

#file_chooser()
#value_entry()
# Start the GUI event loop
#window.mainloop()
