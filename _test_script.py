from __future__ import print_function

import numpy
import matplotlib.pyplot as pyplot

x = numpy.linspace(0.0, 2.0 * numpy.pi)

pyplot.plot(x, numpy.cos(x))
pyplot.title('cos')

pyplot.figure(100)
pyplot.plot(x, numpy.sinc(x))
pyplot.title('sinc')

g_figure_manager.add_all_figures()

pyplot.figure(2)
pyplot.plot(x, numpy.log(x + 1e-9))
pyplot.title('log')

g_figure_manager.add_figure(2)

# pyplot.show()
pyplot.close('all')
