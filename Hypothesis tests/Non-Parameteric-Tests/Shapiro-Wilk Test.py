# Shapiro-Wilk Test on Normally Distributed Data

from numpy.random import seed
from numpy.random import randn
from scipy.stats import shapiro

#set seed (e.g. make this example reproducible)
seed(0)

#generate dataset of 100 random values that follow a standard normal distribution
data = randn(100)

#perform Shapiro-Wilk test
print(shapiro(data))

# From the output we can see that the test statistic is 0.9927 and the corresponding p-value is 0.8689.

# Since the p-value is not less than .05, we fail to reject the null hypothesis.
#  We do not have sufficient evidence to say that the sample data does not come from a normal distribution.

from numpy.random import poisson
#set seed (e.g. make this example reproducible)
seed(0)

#generate dataset of 100 values that follow a Poisson distribution with mean=5
data = poisson(5, 100)

print(shapiro(data))

# From the output we can see that the test statistic is 0.9582 and the corresponding p-value is 0.00299.

# Since the p-value is less than .05, we reject the null hypothesis.
#  We have sufficient evidence to say that the sample data does not come from a normal distribution.
