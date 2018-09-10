#!/usr/bin/env python

from __future__ import print_function

import os
import sys
import gzip
import pickle

if sys.version_info >= (3, 0):
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename
else:
    from Tkinter import Tk
    from tkFileDialog import askopenfilename

import matplotlib.pyplot as pyplot

# The directory path where the last figure is.
g_last_path = os.getenv('HOME')

def find_file():
    """Search for the file to open.

    Only *.pmg is supported. The file should be generated from img_saver.

    This function will initialize g_root if it is not ready, it also saves
    the drectory path where the last image is read.

    Returns:
        str: The path to the selected file.
    """
    global g_last_path

    gui_search = Tk()
    gui_search.withdraw()

    filename = askopenfilename(
            initialdir = g_last_path,
            title = 'Select file or click cancel to exit',
            filetypes = (('pmg files', '*.pmg'), ))

    g_last_path = os.path.dirname(filename)

    gui_search.destroy()

    return filename

def load_figure(filename):
    """Read the figures in file and return.

    This function is helpful for reusing the plotted data.
    For one figure, the following functions are helpful for reading the data.
        pyplot.gca().lines[i].get_xdata()
        pyplot.gca().lines[i].get_ydata()
    (https://stackoverflow.com/questions/20130768/retrieve-xy-data-from-matplotlib-figure)

    Args:
        filename (str): The path for the file containing the figures.

    Return:
        *: All data available in file.
    """
    assert os.path.isfile(filename), 'File {} not found.'.format(filename)

    with gzip.GzipFile(filename, 'rb') as infile:
        return pickle.load(infile)

def show_figure(filename):
    """Read the figures in file and display.

    Args:
        filename (str): The path for the file containing the figures.
    """
    load_figure(filename)

    pyplot.show()
    pyplot.close('all')

def main():
    """Select one file and display the figures it contains.
    """
    show_figure(find_file())

if __name__ == '__main__':
    while True:
        main()

