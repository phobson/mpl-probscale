norm = stats.norm(5, 1.25)
fig = probplot(data, ax=ax, plottype='qq', dist=norm,
          probax='x', problabel='Theoretical Quantiles',
          datalabel='Observed values', bestfit=True,
          line_kws=dict(linestyle=':', linewidth=2),
          scatter_kws=dict(marker='^', alpha=0.5))
