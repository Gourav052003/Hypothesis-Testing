# An F-test is used to test whether two population variances are equal. The null and alternative hypotheses for the test are as follows:

# H0: σ12 = σ22 (the population variances are equal)
# H1: σ12 ≠ σ22 (the population variances are not equal)

x = [18, 19, 22, 25, 27, 28, 41, 45, 51, 55]
y = [14, 15, 15, 17, 18, 22, 25, 25, 27, 34]

import numpy as np
import scipy
#define F-test function
def f_test(x, y):
    x = np.array(x)
    y = np.array(y)
    f = np.var(x, ddof=1)/np.var(y, ddof=1) #calculate F test statistic  #ddof N-ddof or N-1
    dfn = x.size-1 #define degrees of freedom numerator 
    dfd = y.size-1 #define degrees of freedom denominator 
    p = 1-scipy.stats.f.cdf(f, dfn, dfd) #find p-value of F test statistic 
    return f, p

#perform F-test

# The F test statistic is 4.38712 and the corresponding p-value is 0.019127. Since this p-value is less than .05, we would reject the null hypothesis. 
# This means we have sufficient evidence to say that the two population variances are not equal.
print(f_test(x, y))
# example
#  Does a new treatment or process reduce the variability of some current treatment or process?