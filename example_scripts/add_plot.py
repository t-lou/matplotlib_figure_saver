import matplotlib.pyplot as pyplot

add_pmg('both.pmg')

pyplot.figure()
pyplot.plot([1] * 50)

remove_all_figures()
add_all_figures()
update_figures()

print('Constant line with y=1 is added after both.pmg')
