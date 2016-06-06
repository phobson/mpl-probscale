fig = probplot(data, plottype='qq', probax='x',
         problabel='Theoretical Quantiles',
         datalabel='Observed values', bestfit=True,
         line_kws=dict(linestyle='-', linewidth=2),
         scatter_kws=dict(marker='s', alpha=0.5))
