# Suppose we want to know whether a certain study program significantly impacts student performance on a particular exam. To test this, we have 15 students in a class take a pre-test. 
# Then, we have each of the students participate in the study program for two weeks. Then, the students retake a test of similar difficulty.

# To compare the difference between the mean scores on the first and second test, we use a paired samples t-test because for each student their first test score can be paired with their second test score.


pre = [88, 82, 84, 93, 75, 78, 84, 87, 95, 91, 83, 89, 77, 68, 91]
post = [91, 84, 88, 90, 79, 80, 88, 90, 90, 96, 88, 89, 81, 74, 92]

from scipy.stats import ttest_rel

#perform the paired samples t-test
print(ttest_rel(pre, post))

# The test statistic is -2.9732 and the corresponding two-sided p-value is 0.0101.

# Since the p-value (0.0101) is less than 0.05, we reject the null hypothesis. We have sufficient evidence to say that the true mean test score is different for students before and after participating in the study program.

