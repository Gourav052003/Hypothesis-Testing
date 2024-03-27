# the differences in height between cross- and self-fertilized corn plants is given as follows
d = [6, 8, 14, 16, 23, 24, 28, 29, 41, -48, 49, 56, 60, -67, 75]
# Cross-fertilized plants appear to be higher. To test the null hypothesis that there is no height difference, we can apply the two-sided test

# Wilcoxon matched pair test is a non-parametric hypothesis test that compares the median of two paired groups and tells if they are identically distributed or not. 
from scipy.stats import wilcoxon
res = wilcoxon(d)
print(res.statistic, res.pvalue)
# Hence, we would reject the null hypothesis at a confidence level of 5%, concluding that there is a difference in height between the groups. 

# Define your data
# one sample test
data = [22, 33, 45, 55, 12, 33, 56, 78, 34, 23]

# Define the median you want to compare with
median_to_compare = 100000

# Center the data around the alternative median
centered_data = [x - median_to_compare for x in data]

# Perform Wilcoxon signed-rank test
statistic, p_value = wilcoxon(centered_data, alternative='greater')

# Print the results
print("Wilcoxon signed-rank statistic:", statistic)
print("p-value:", p_value)
