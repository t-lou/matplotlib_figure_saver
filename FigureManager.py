from __future__ import print_function

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
        """
        self._figures += pylab_helpers.Gcf.get_all_fig_managers()

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

    def get_figure(self, index):
        """Get the figure with index.

        Args:
            index (int): The index of the wanted figure.

        Return:
            matplotlib.pyplot.Figure: The expected figure object.
        """
        assert index < len(self._figures), \
            'Asked figure {} but only {} images are available.'.format(
                    index,
                    len(self._figures))
        return self._figures[index]
