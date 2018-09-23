#!/usr/bin/env python

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

import img_reader
import FigureManager

g_figure_manager = FigureManager.FigureManager()

# The size of the button (width, height) for buttons in root gui.
SIZE_BUTTON = (18, 4)


def load_python_script():
    """Find Python script and execute.
    """
    gui_search = tkinter.Tk()
    gui_search.withdraw()

    filename = askopenfilename(
        initialdir=img_reader.g_last_path,
        filetypes=(('python files', '*.py'), ))

    gui_search.destroy()

    if filename:
        img_reader.g_last_path = os.path.dirname(filename)
        with open(filename, 'r') as infile:
            exec (infile.read())


def main():
    """The main entry of the program.
    """
    root = tkinter.Tk()
    root.title('Hello World!')

    tkinter.Button(
        root,
        text='Script',
        height=SIZE_BUTTON[1],
        width=SIZE_BUTTON[0],
        command=load_python_script).pack(side=tkinter.TOP)

    tkinter.Button(
        root,
        text='Image',
        height=SIZE_BUTTON[1],
        width=SIZE_BUTTON[0],
        command=img_reader.main).pack(side=tkinter.TOP)

    tkinter.Button(
        root,
        text='Command',
        height=SIZE_BUTTON[1],
        width=SIZE_BUTTON[0],
        command=img_reader.start_text_box).pack(side=tkinter.TOP)

    root.mainloop()


if __name__ == '__main__':
    main()
