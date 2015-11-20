# mpl-probscale
Real probability scales for matplotlib

[![Build Status](https://travis-ci.org/phobson/mpl-probscale.svg)](https://travis-ci.org/phobson/mpl-probscale)
[![Coverage Status](https://coveralls.io/repos/phobson/mpl-probscale/badge.svg?branch=master&service=github)](https://coveralls.io/github/phobson/mpl-probscale?branch=master)

Simply importing `probscale` let's you use probability scales in your matplotlib figures:

```python
import matplotlib.pyplot as plt
import probscale

plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_ylim(1e-2, 1e2)
ax.set_yscale('log')

ax.set_xlim(0.5, 99.5)
ax.set_xscale('prob')
```

![Alt text](docs/img/example.png "Example axes")

