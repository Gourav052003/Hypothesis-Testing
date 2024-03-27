# Researchers want to know whether or not two different species of plants have the same mean height. 
# To test this, they collect asimple random sample of 20 plants from each species.

# two independent sample t test for comparing the two independent population mean are eaual, less , greater depending on 'altenative' parameter
from scipy.stats import ttest_ind
import numpy as np

# Before we perform the test, we need to decide if we’ll assume the two populations have equal variances or not. As a rule of thumb, we can assume the populations have equal variances if the ratio of the larger sample variance to the smaller sample variance is less than 4:1. 

group1 = np.array([14, 15, 15, 16, 13, 8, 14, 17, 16, 14, 19, 20, 21, 15, 15, 16, 16, 13, 14, 12])
group2 = np.array([15, 17, 14, 17, 14, 8, 12, 19, 19, 14, 17, 22, 24, 16, 13, 16, 13, 18, 15, 13])
print(np.var(group1), np.var(group2))

print(12.260000000000002/7.727500000000001)
# if less than 4 then they are having equal variances

#perform two sample t-test with equal variances
print(ttest_ind(a=group1, b=group2, equal_var=True))

# equal_var: if True, perform a standard independent 2 sample t-test that assumes equal population variances.
# If False, perform Welch’s t-test, which does not assume equal population variances. This is True by default.


