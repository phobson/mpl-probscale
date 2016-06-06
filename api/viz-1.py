import numpy; numpy.random.seed(0)
from matplotlib import pyplot
from scipy import stats
from probscale.viz import probplot
data = numpy.random.normal(loc=5, scale=1.25, size=37)
fig = probplot(data, plottype='prob', probax='y',
         problabel='Non-exceedance probability',
         datalabel='Observed values', bestfit=True,
         line_kws=dict(linestyle='--', linewidth=2),
         scatter_kws=dict(marker='o', alpha=0.5))
