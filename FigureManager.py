from __future__ import print_function

import os
import sys
import gzip
import pickle

import matplotlib.pyplot as pyplot
import matplotlib._pylab_helpers as pylab_helpers

import interaction


class FigureManager(object):
    """The manager to store and matplotlib figures.
    """

    def __init__(self):
        """Initialize the figure list.
        """
        self._figures = []

    def add_all_figures(self):
        """Add all pyplot.figure available.
        """
        self._figures += [
            manager.canvas.figure
            for manager in pylab_helpers.Gcf.get_all_fig_managers()
        ]

    def add_figure(self, target):
        """Add specified figure.

        Args:
            target (int or matplotlib.pyplot.Figure): Figure index of figure.
        """
        if isinstance(target, int):
            self._figures.append(pyplot.figure(target))
        elif isinstance(target, pyplot.Figure):
            self._figures.append(target)
        else:
            print('Parameter for add_figure must be int or pyplot.Figure.')

    def add_pmg(self, filename):
        """Load the figure(s) from one pmg file.

        Args:
            filename (str): The filename to read.
        """
        data = interaction.load_pmg(filename)
        if isinstance(data, pyplot.Figure):
            data = [data]
        self._figures += data

    def get_figures(self):
        """Return all figures.

        Return:
            List of figures.
        """
        return self._figures

    def get_figure(self, index):
        """Get the figure with index.

        Args:
            index (int): The index of the wanted figure.

        Return:
            matplotlib.pyplot.Figure: The expected figure object.
        """
        assert -len(self._figures) <= index < len(self._figures), \
            'Asked figure {} but only {} images are available.'.format(
                    index,
                    len(self._figures))
        return self._figures[index]

    def remove_figure(self, index):
        """Delete figure with index.

        Args:
            index (int): Index of figure to delete.
        """
        assert -len(self._figures) <= index < len(self._figures), \
            'Asked figure {} but only {} images are available.'.format(
                    index,
                    len(self._figures))
        del self._figures[index]

    def save_pmg(self, filename='images'):
        """Save all figures in pmg file with given name.

        Args:
            filename (str): The filename to save.
        """
        FigureManager.save_all_figures(self._figures, filename)

    @staticmethod
    def load_pmg(filename):
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
            if sys.version_info >= (3, 0):
                return pickle.load(infile, encoding='latin1')
            else:
                return pickle.load(infile)

    @staticmethod
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

    @staticmethod
    def save_all_figures(filename='figures', figures=None):
        """Save all figures available to file.
        Args:
            filename (str): The filename for the ouput file.
        """
        if figures is None:
            fm = FigureManager()
            fm.add_all_figures()
            figures = fm.get_figures()

        # https://stackoverflow.com/questions/3783217/get-the-list-of-figures-in-matplotlib
        with gzip.GzipFile(FigureManager.complete_extension(filename),
                           'wb') as outfile:
            pickle.dump(
                tuple(manager.canvas.figure
                      for manager in pylab_helpers.Gcf.get_all_fig_managers()),
                outfile,
                protocol=2)

    @staticmethod
    def save_figure(filename, figure_id):
        """Save specific figure to file.
        Args:
            filename (str): The filename for the ouput file.
        """
        with gzip.GzipFile(FigureManager.complete_extension(filename),
                           'wb') as outfile:
            pickle.dump(pyplot.figure(figure_id), outfile, protocol=2)


# Default instance for the main application.
g_figure_manager = FigureManager()
