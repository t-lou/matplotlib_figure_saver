from __future__ import print_function

import sys
import os

if sys.version_info >= (3, 0):
    import tkinter
    from tkinter.filedialog import askopenfilename
    from imp import reload
else:
    import Tkinter as tkinter
    from tkFileDialog import askopenfilename

import testfield
import testfield_source

# The directory path where the last figure is.
g_last_path = os.getenv('HOME')


def find_file(filetypes):
    """Find file with given types and return the filename.
    
    If one file is selected, the logged last path will be changed to the
    directory where the file lies.
    
    Args:
        filetypes (list(list(str, str))): Texts and patterns to restrict the
            file types.
        
    Return:
        str: The path for selected file.
    """
    global g_last_path

    gui_search = tkinter.Tk()
    gui_search.withdraw()

    filename = askopenfilename(initialdir=g_last_path, filetypes=filetypes)

    gui_search.destroy()

    if filename:
        g_last_path = os.path.dirname(filename)

    return filename


def load_python_script():
    """Find Python script and execute.
    """
    filename = find_file((('Python files', '*.py'),))

    if filename:
        with open(filename, 'r') as infile:
            testfield_source.content = infile.read()
            reload(testfield)


def find_pmg():
    """Search for the pmg image to open.

    Only *.pmg is supported. The file should be generated from img_saver.

    This function will initialize g_root if it is not ready, it also saves
    the drectory path where the last image is read.

    Returns:
        str: The path to the selected file.
    """
    return find_file((('pmg files', '*.pmg'),))


def start_text_box():
    """Open a text box for execute Python code (not yet influence the plots).
    """

    def do(string):
        """
        Alias for exec (which brings SyntaxError).
        """
        testfield_source.content = string
        reload(testfield)

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

    tkinter.Button(
        text_box,
        text='Execute',
        command=(lambda: do(txt.get('1.0', tkinter.END).strip()))).pack(
            side=tkinter.BOTTOM, expand=tkinter.YES, fill=tkinter.BOTH)


def show_help_box():
    label_box = tkinter.Tk()

    text = '''Helpful commands:
        
    add_all_figures():
        Add all matplotlib.pyplot.figure-s.
    add_figure(int/Figure):
        Add one matplotlib.pyplot.figure with either object or index.
    save_all_figures(str, [Figure]):
        Save all figures to path (first string).
        If the figures are not assigned, all figures in background will be saved.
        Default filename is 'figures'.
    update_figures():
        Show all added figures..
        '''
    tkinter.Label(
        label_box,
        text=text,
        width=80,
        height=40,
        anchor=tkinter.NW,
        justify=tkinter.LEFT).pack(
            side=tkinter.LEFT, fill=tkinter.Y, expand=tkinter.YES)

    label_box.mainloop()
