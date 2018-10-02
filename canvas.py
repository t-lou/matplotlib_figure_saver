from __future__ import print_function

import sys
import os

import matplotlib.pyplot as pyplot
import matplotlib.backends.backend_tkagg as tk_backend

if sys.version_info >= (3, 0):
    import tkinter
    from tkinter import ttk
else:
    import Tkinter as tkinter
    import ttk

import FigureManager
import interaction


def add_panel(gui):
    """Add control panel to GUI (not only execute Python code).

    Args:
        gui: Where the panel should be (should be element of tkinter).
    """
    button_script = tkinter.Button(
        gui, text='Command', command=interaction.start_text_box)
    button_script.pack(side=tkinter.TOP)


def add_canvas(figure, container):
    """Add the figure and toolbar to GUI.

    Args:
        figure (matplotlib.Figure): The figure object to visualize.
        container: The GUI part where the figure is shown.
    """
    canvas = tk_backend.FigureCanvasTkAgg(figure, master=container)
    canvas.draw()
    canvas.get_tk_widget().pack(
        side=tkinter.TOP, fill=tkinter.BOTH, expand=True)

    # NavigationToolbar2TkAgg is deprecated since matplotlib 2.2,
    # NavigationToolbar2Tk should be used and is only available in new version.
    toolbar = tk_backend.NavigationToolbar2Tk(canvas, container) \
            if hasattr(tk_backend, 'NavigationToolbar2Tk') \
            else tk_backend.NavigationToolbar2TkAgg(canvas, container)
    toolbar.update()
    canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)

    pyplot.close(figure.number)


def show_figure_from_file(filename):
    """Read the figures in file and display.

    Args:
        filename (str): The path where the pmg file is.
    """
    assert os.path.isfile(filename) and os.path.splitext(filename)[1] == '.pmg'
    data = FigureManager.FigureManager.load_pmg(filename)
    if data:
        show_figure(data, title=os.path.splitext(os.path.basename(filename))[0])


def show_figure_from_manager(figure_manager):
    """Display the figures from a FigureManager.

    Args:
        figure_manager (FigureManager): The FigureManager with figures.
    """
    show_figure(figure_manager.get_figures())


def show_figure(data, title=None):
    """Display the figures.

    Args:
        data (Figure or list[Figure]): The data from pmg file or FigureManager.
        title (str): The tile for the window.
    """
    gui = tkinter.Tk()
    if title is None:
        title = 'Pytena'
    gui.title(title)

    if isinstance(data, (list, tuple)):
        notebook = ttk.Notebook(gui)
        notebook.grid(row=1)

        for index, figure in enumerate(data, 1):
            page = ttk.Frame(notebook)
            notebook.add(page, text='figure{}'.format(index))
            add_panel(page)
            add_canvas(figure, page)

        notebook.pack(expand=True, fill=tkinter.BOTH)
    else:
        add_panel(gui)
        add_canvas(data, gui)
