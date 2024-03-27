# In the 1- sample wilcoxon test example, the differences in height between paired plants are provided to wilcoxon directly.
# Alternatively, wilcoxon accepts two samples of equal length, calculates the differences between paired elements, then performs the test. 
# Consider the samples x and y:


# two sampled paired test
from scipy.stats import wilcoxon
import numpy as np
x = np.array([0.5, 0.825, 0.375, 0.5])
y = np.array([0.525, 0.775, 0.325, 0.55])
res = wilcoxon(x, y, alternative='greater')
print(res)