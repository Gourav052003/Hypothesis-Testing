# One special type of correlation is called Spearman Rank Correlation, which is used to measure the correlation between two ranked variables. 
# (e.g. rank of a student’s math exam score vs. rank of their science exam score in a class).

import pandas as pd

#create DataFrame
df = pd.DataFrame({'student': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
                   'math': [70, 78, 90, 87, 84, 86, 91, 74, 83, 85],
                   'science': [90, 94, 79, 86, 84, 83, 88, 92, 76, 75]})

from scipy.stats import spearmanr

#calculate Spearman Rank correlation and corresponding p-value
rho, p = spearmanr(df['math'], df['science'])

#print Spearman rank correlation and p-value
print(rho)

print(p)



# From the output we can see that the Spearman rank correlation is -0.41818 and the corresponding p-value is 0.22911.
# This indicates that there is a negative correlation between the science and math exam scores.
# However, since the p-value of the correlation is not less than 0.05, the correlation is not statistically significant.            