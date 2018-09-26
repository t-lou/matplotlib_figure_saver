#!/usr/bin/env python

from __future__ import print_function

from FigureManager import FigureManager
import canvas
import interaction


def main():
    """Select one file and display the figures it contains.
    """
    canvas.show_figure(interaction.find_file())


if __name__ == '__main__':
    while True:
        main()
