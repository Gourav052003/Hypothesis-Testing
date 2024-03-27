from statsmodels.sandbox.stats.runs import runstest_2samp

d1 = [1,2,3,4,5]
d2 = [1000,10000,3000.5,60000.75]

#should be floating point data atleast in one list d2

print(runstest_2samp(d1,d2))

# we reject the null hypothesis of having both data came from same distribution