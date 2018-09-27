#!/usr/bin/env python

from __future__ import print_function

import sys

if sys.version_info >= (3, 0):
    import tkinter
else:
    import Tkinter as tkinter

import interaction
import canvas
import FigureManager

# The size of the button (width, height) for buttons in root gui.
SIZE_BUTTON = (18, 4)


def find_show_image():
    """Search, open and show an pmg image.
    """
    filename = interaction.find_pmg()
    if filename:
        FigureManager.g_figure_manager.add_pmg(filename)
        canvas.show_figure_from_manager(FigureManager.g_figure_manager)


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
        command=find_show_image).pack(side=tkinter.TOP)

    tkinter.Button(
        root,
        text='Command',
        height=SIZE_BUTTON[1],
        width=SIZE_BUTTON[0],
        command=interaction.start_text_box).pack(side=tkinter.TOP)

    root.mainloop()


if __name__ == '__main__':
    main()
