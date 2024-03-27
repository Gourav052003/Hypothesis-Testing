# chi2 test of independence

# Suppose we want to know whether or not gender is associated with political party preference. 
# We take a simple random sample of 500 voters and survey them on their political party preference. The following table shows the results of the survey:

data = [[120, 90, 40],
        [110, 95, 45]]

import scipy.stats as stats

#perform the Chi-Square Test of Independence
print(stats.chi2_contingency(data))
# with expected vales

