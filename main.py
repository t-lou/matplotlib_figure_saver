#!/usr/bin/env python

from __future__ import print_function

import sys

if sys.version_info >= (3, 0):
    import tkinter
    from tkinter import ttk
    from tkinter.filedialog import askopenfilename
else:
    import Tkinter as tkinter
    import ttk
    from tkFileDialog import askopenfilename

import interaction
import img_reader

# The size of the button (width, height) for buttons in root gui.
SIZE_BUTTON = (18, 4)


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
        command=interaction.load_python_script).pack(side=tkinter.TOP)

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
        command=interaction.start_text_box).pack(side=tkinter.TOP)

    root.mainloop()


if __name__ == '__main__':
    main()
