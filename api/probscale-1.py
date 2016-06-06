from matplotlib import pyplot
import probscale
fig, ax = pyplot.subplots(figsize=(4, 7))
ax.set_ylim(bottom=0.5, top=99.5)
ax.set_yscale('prob')
