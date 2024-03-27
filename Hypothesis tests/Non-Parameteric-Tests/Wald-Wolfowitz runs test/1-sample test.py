#runs test (Wald-Wolfowitz runs test)

# Runs test is a statistical test that is used to determine whether or not a dataset comes from a random process.


from statsmodels.sandbox.stats.runs import runstest_1samp 

#create dataset
data = [12, 16, 16, 15, 14, 18, 19, 21, 13, 13]

#Perform Runs test
# for sample n1<20 and n2<20
# G is calucation and test using G table

# for greater than 20 ztest is used

print(runstest_1samp(data, correction=False))
# The z-test statistic turns out to be -0.67082 and the corresponding p-value is 0.50233. Since this p-value is not less than α = .05, we fail to reject the null hypothesis. We have sufficient evidence to say that the data was produced in a random manner.

data = ['H','H','T','H','T','T','T','H','T']
data = [0,0,1,0,1,1,1,0,1]

# for numeric meadian or mean is used as cutoff
 
print(runstest_1samp(data, correction=False))
