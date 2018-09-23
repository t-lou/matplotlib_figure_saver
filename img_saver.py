from __future__ import print_function

import os
import gzip
import pickle

import matplotlib.pyplot as pyplot
import matplotlib._pylab_helpers as pylab_helpers


def complete_extension(filename):
    """Add or replace the extension to .pmg.

    Args:
        filename (str): The path for one file.

    Returns:
        str: The filename corresponding to the given path, but with .pmg as
            extension.
    """
    extension = '.pmg'
    return os.path.splitext(filename)[0] + extension


def save_all_figures(filename):
    """Save all figures available to file.

    Args:
        filename (str): The filename for the ouput file.
    """
    # https://stackoverflow.com/questions/3783217/get-the-list-of-figures-in-matplotlib
    with gzip.GzipFile(complete_extension(filename), 'wb') as outfile:
        pickle.dump(
            tuple(manager.canvas.figure
                  for manager in pylab_helpers.Gcf.get_all_fig_managers()),
            outfile,
            protocol=2)


def save_figure(filename, figure_id):
    """Save specific figure to file.

    Args:
        filename (str): The filename for the ouput file.
    """
    with gzip.GzipFile(complete_extension(filename), 'wb') as outfile:
        pickle.dump(pyplot.figure(figure_id), outfile, protocol=2)
