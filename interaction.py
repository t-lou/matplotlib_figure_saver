from __future__ import print_function

import sys
import os

if sys.version_info >= (3, 0):
    import tkinter
    from tkinter import ttk
    from tkinter.filedialog import askopenfilename
else:
    import Tkinter as tkinter
    import ttk
    from tkFileDialog import askopenfilename

import FigureManager

# The directory path where the last figure is.
g_last_path = os.getenv('HOME')


def load_python_script():
    """Find Python script and execute.
    """
    global g_last_path

    gui_search = tkinter.Tk()
    gui_search.withdraw()

    filename = askopenfilename(
        initialdir=g_last_path, filetypes=(('python files', '*.py'),))

    gui_search.destroy()

    if filename:
        g_last_path = os.path.dirname(filename)
        with open(filename, 'r') as infile:
            add_all_figures = FigureManager.g_figure_manager.add_all_figures
            add_figure = FigureManager.g_figure_manager.add_figure
            save_all_figures = FigureManager.FigureManager.save_all_figures
            exec(infile.read())


def find_file():
    """Search for the file to open.

    Only *.pmg is supported. The file should be generated from img_saver.

    This function will initialize g_root if it is not ready, it also saves
    the drectory path where the last image is read.

    Returns:
        str: The path to the selected file.
    """
    global g_last_path

    gui_search = tkinter.Tk()
    gui_search.withdraw()

    filename = askopenfilename(
        initialdir=g_last_path,
        title='Select file or click cancel to exit',
        filetypes=(('pmg files', '*.pmg'),))

    gui_search.destroy()

    if filename:
        g_last_path = os.path.dirname(filename)

    return filename


def start_text_box():
    """Open a text box for execute Python code (not yet influence the plots).
    """

    def do(string):
        """
        Alias for exec (which brings SyntaxError).
        """
        add_all_figures = FigureManager.g_figure_manager.add_all_figures
        add_figure = FigureManager.g_figure_manager.add_figure
        save_all_figures = FigureManager.FigureManager.save_all_figures
        exec(string)

    text_box = tkinter.Tk()
    text_box.title('Command')

    tkinter.Label(
        text_box, text='Add Python script here').pack(
            side=tkinter.TOP, fill=tkinter.BOTH, expand=tkinter.YES)

    txt = tkinter.Text(text_box, width=120, height=40)
    txt.focus()
    txt.pack(side=tkinter.LEFT, fill=tkinter.X, expand=tkinter.YES)

    scrollbar = tkinter.Scrollbar(text_box)
    scrollbar.pack(side=tkinter.LEFT, fill=tkinter.Y, expand=tkinter.YES)
    scrollbar.config(command=txt.yview)
    txt.config(yscrollcommand=scrollbar.set)

    txt.insert(tkinter.END, 'import matplotlib.pyplot as plt\n')
    txt.insert(tkinter.END, 'import numpy as np\n')
    txt.insert(tkinter.END, '# call g_figure_manager.add_all_figures() ')
    txt.insert(tkinter.END, 'to save all figures\n\n')

    tkinter.Button(
        text_box,
        text='Execute',
        command=(lambda: do(txt.get('1.0', tkinter.END).strip()))).pack(
            side=tkinter.BOTTOM, expand=tkinter.YES, fill=tkinter.BOTH)
