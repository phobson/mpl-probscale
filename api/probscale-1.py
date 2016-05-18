from matplotlib import pyplot
import probscale
fig, ax = pyplot.subplots()
ax.set_xlim(left=0.2, right=99.9)
ax.set_xscale('prob')
