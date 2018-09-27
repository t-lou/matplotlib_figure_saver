#!/usr/bin/env python

from __future__ import print_function

import interaction
import canvas

if __name__ == '__main__':
    while True:
        filename = interaction.find_pmg()
        if filename:
            canvas.show_figure(filename)
        else:
            break
