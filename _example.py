from __future__ import print_function

import numpy
import matplotlib.pyplot as pyplot

import img_reader
from FigureManager import FigureManager

# plot the two figures
x = numpy.linspace(0.0, 2.0 * numpy.pi)

pyplot.plot(x, numpy.cos(x))
pyplot.title('cos')

pyplot.figure(100)
pyplot.plot(x, numpy.sinc(x))
pyplot.title('sinc')

# save to files
FigureManager.save_figure('first', 1)
FigureManager.save_figure('second.wth', 100)
FigureManager.save_all_figures('both')

# clear the canvas
pyplot.close(1)
pyplot.close(100)

# read the files
print('Please open first.pmg.')
img_reader.main()
print('Please open both.pmg.')
img_reader.main()
print('Please open second.pmg.')
img_reader.main()
