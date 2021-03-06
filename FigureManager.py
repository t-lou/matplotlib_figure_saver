from __future__ import print_function

import os
import sys
import gzip
import pickle
import io

import matplotlib.pyplot as pyplot
import matplotlib._pylab_helpers as pylab_helpers


class FigureManager(object):
    """The manager to store and matplotlib figures.
    """

    def __init__(self):
        """Initialize the figure list.
        """
        self._figures = []

    def add_all_figures(self):
        """Add all pyplot.figure available.

        This function will close all figures, otherwise the program may block.
        """
        for manager in pylab_helpers.Gcf.get_all_fig_managers():
            self.add_figure(manager.canvas.figure)

    def add_figure(self, target, index=-1):
        """Add specified figure.

        If one index is given, the figure will be closed. Otherwise the program may block.

        Args:
            target (int or matplotlib.pyplot.Figure): Figure or index of figure.
            index (int): To which index to add this figure.
        """
        if isinstance(target, int):
            self.add_figure(pyplot.figure(target))
        elif isinstance(target, pyplot.Figure):
            buffer = io.BytesIO()
            pickle.dump(target, buffer)
            buffer.seek(0)
            if index < 0:
                self._figures.append(buffer)
            else:
                self._figures.insert(index, buffer)
        else:
            print('Parameter for add_figure must be int or pyplot.Figure.')

    def reset_figure(self, target, target_index):
        """Replace a figure with the given one.

        If one index is given, the figure will be closed. Otherwise the program may block.

        Args:
            target (int or matplotlib.pyplot.Figure): Figure or index of figure.
            target_index (int): To which index to add this figure.
        """
        if isinstance(target, int):
            self.reset_figure(pyplot.figure(target), target_index)
        elif isinstance(target, pyplot.Figure):
            buffer = io.BytesIO()
            pickle.dump(target, buffer)
            buffer.seek(0)
            self._figures[target_index] = buffer
        else:
            print('Parameter for add_figure must be int or pyplot.Figure.')

    def add_pmg(self, filename):
        """Load the figure(s) from one pmg file.

        Args:
            filename (str): The filename to read.
        """
        data = FigureManager.load_pmg(filename)
        if isinstance(data, pyplot.Figure):
            data = [data]
        for figure in data:
            self.add_figure(figure)

    def get_figure(self, index, start_index=0):
        """Get the figure with index.

        Args:
            index (int): The index of the wanted figure.
            start_index (int): Starting index in matplotlib, default value is equivalent to index+1.

        Return:
            matplotlib.pyplot.Figure: The expected figure object.
        """
        assert -len(self._figures) <= index < len(self._figures), \
            'Asked figure {} but only {} images are available.'.format(
                    index,
                    len(self._figures))
        if start_index < 1:
            start_index = index + 1
        pyplot.figure(start_index)
        figure = pickle.load(self._figures[index])
        self._figures[index].seek(0)
        return figure

    def get_all_figures(self, start_index=1):
        """Return all figures of this manager.

        Args:
            start_index (int): Starting index in matplotlib.

        Return:
            list[matplotlib.pyplot.Figure]: All figures in this figure manager.
        """
        pyplot.figure(start_index)
        return [self.get_figure(index) for index, _ in enumerate(self._figures)]

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

    def remove_all_figures(self):
        """Remove all figures.
        """
        self.clean_figures()

    def clean_figures(self):
        """Remove all figures.
        """
        del self._figures
        self._figures = []

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
            figures ([Figure]): The figure objects to save.
        """
        if figures is None:
            fm = FigureManager()
            fm.add_all_figures()
            figures = fm.get_all_figures()

        # https://stackoverflow.com/questions/3783217/get-the-list-of-figures-in-matplotlib
        with gzip.GzipFile(FigureManager.complete_extension(filename),
                           'wb') as outfile:
            pickle.dump(figures, outfile, protocol=2)

    @staticmethod
    def save_figure(filename, figure_id):
        """Save specific figure to file.

        Args:
            filename (str): The filename for the ouput file.
            figure_id (int): The index of figure to save.
        """
        with gzip.GzipFile(FigureManager.complete_extension(filename),
                           'wb') as outfile:
            pickle.dump(pyplot.figure(figure_id), outfile, protocol=2)


# Default instance for the main application.
g_figure_manager = FigureManager()
