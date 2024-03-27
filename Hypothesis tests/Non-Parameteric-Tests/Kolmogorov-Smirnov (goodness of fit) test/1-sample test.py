#  one-sample Kolmogorov-Smirnov test for goodness of fit.
# This test compares the underlying distribution F(x) of a sample against a given continuous distribution G(x).

import numpy as np
from  scipy import stats
import seaborn as sns

rng = np.random.default_rng(20)
x = stats.norm.rvs(size=100, random_state=rng) # Prepare normal distributed data
print(stats.ks_1samp(x, stats.chi2(2).cdf)) #two degrees of freedom    