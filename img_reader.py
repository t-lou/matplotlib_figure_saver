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
    import Tkinter
    from Tkinter import Tk
    import ttk
    from tkFileDialog import askopenfilename

import matplotlib.pyplot as pyplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

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

def add_canvas(figure, container):
    """Add the figure and toolbar to GUI.

    Args:
        figure (matplotlib.Figure): The figure object to visualize.
        container: The GUI part where the figure is shown.
    """
    canvas = FigureCanvasTkAgg(figure, master=container)
    canvas.draw()
    canvas.get_tk_widget().pack(side=Tkinter.BOTTOM, fill=Tkinter.BOTH, expand=True)

    toolbar = NavigationToolbar2TkAgg(canvas, container)
    toolbar.update()
    canvas._tkcanvas.pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=True)

    pyplot.close(figure.number)

def show_figure(filename):
    """Read the figures in file and display.

    Args:
        filename (str): The path for the file containing the figures.
    """
    data = load_figure(filename)

    gui = Tk()
    gui.title(os.path.splitext(os.path.basename(filename))[0])

    if isinstance(data, (list, tuple)):
        notebook = ttk.Notebook(gui)
        notebook.grid(row=1)

        for index, figure in enumerate(data, 1):
            page = ttk.Frame(notebook)
            notebook.add(page, text='figure{}'.format(index))
            add_canvas(figure, page)
    else:
        add_canvas(data, gui)

    gui.mainloop()

    pyplot.close('all')

def main():
    """Select one file and display the figures it contains.
    """
    show_figure(find_file())

if __name__ == '__main__':
    while True:
        main()

