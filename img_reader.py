#!/usr/bin/env python

from __future__ import print_function

import os
import pickle

from tkinter import Tk
from tkinter.filedialog import askopenfilename

import matplotlib.pyplot as pyplot

def find_file():
    """Search for the file to open.

    Only *.pmg is supported. The file should be generated from img_saver.

    Returns:
        str: The path to the selected file.
    """
    Tk().withdraw()
    return askopenfilename(initialdir = os.getenv('HOME'),
            title = 'Select file or click cancel to exit', 
            filetypes = (('pmg files', '*.pmg'), ))

def show_figure(filename):
    """Read the figures in file and display.

    Args:
        filename (str): The path for the file containing the figures. 
    """
    assert os.path.isfile(filename), 'File {} not found.'.format(filename)

    pickle.load(open(filename, 'rb'))
    pyplot.show()

def main():
    """Select one file and display the figures it contains.
    """
    show_figure(find_file())

if __name__ == '__main__':
    while True:
        main()

