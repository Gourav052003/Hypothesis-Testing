# A one-way ANOVA (“analysis of variance”) is used to determine whether or not there is a statistically significant difference between the 
# means of three or more independent groups.

# A researcher recruits 30 students to participate in a study. The students are randomly assigned to use one of three studying techniques for the next three weeks to prepare for an exam. At the end of the three weeks, all of the students take the same test. 
# Use the following steps to perform a one-way ANOVA to determine if the average scores are the same across all three groups.

#enter exam scores for each group
group1 = [85, 86, 88, 75, 78, 94, 98, 79, 71, 80]
group2 = [91, 92, 93, 85, 87, 84, 82, 88, 95, 96]
group3 = [79, 78, 88, 94, 92, 85, 83, 85, 82, 81]

from scipy.stats import f_oneway

#perform one-way ANOVA
print(f_oneway(group1, group2, group3))

# The F test statistic is 2.3575 and the corresponding p-value is 0.1138. Since the p-value is not less than .05, we fail to reject the null hypothesis.
# This means we do not have sufficient evidence to say that there is a difference in exam scores among the three studying techniques.




