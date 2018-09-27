from __future__ import print_function

import FigureManager
import canvas
import testfield_source

# Some abbreviations.
add_all_figures = FigureManager.g_figure_manager.add_all_figures
add_figure = FigureManager.g_figure_manager.add_figure
save_all_figures = FigureManager.FigureManager.save_all_figures


def update_figures():
    canvas.show_figure_from_manager(FigureManager.g_figure_manager)


# Execute the string (from script or command line).
if testfield_source.content is not None:
    exec(testfield_source.content)
