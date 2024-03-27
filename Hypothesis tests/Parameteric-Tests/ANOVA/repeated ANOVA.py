#Repeated ANNOVA

"""
A repeated measures ANOVA is used to determine whether or not there is a statistically significant difference 
between the means of three or more groups in which the same subjects show up in each group

"""

"""
Researchers want to know if four different drugs lead to different reaction times. 
To test this, they measure the reaction time of five patients on the four different drugs.

Since each patient is measured on each of the four drugs, we will use a repeated measures ANOVA to determine if the mean reaction time differs between drugs.

"""

import numpy as np
import pandas as pd

#create data
df = pd.DataFrame({'patient': np.repeat([1, 2, 3, 4, 5], 4),
                   'drug': np.tile([1, 2, 3, 4], 5),
                   'response': [30, 28, 16, 34,
                                14, 18, 10, 22,
                                24, 20, 18, 30,
                                38, 34, 20, 44, 
                                26, 28, 14, 30]})

#view first ten rows of data 
print(df.head())

from statsmodels.stats.anova import AnovaRM

#perform the repeated measures ANOVA
print(AnovaRM(data=df, depvar='response', subject='patient', within=['drug']).fit())

#Since this p-value is less than 0.05, we reject the null hypothesis and conclude that there is a statistically 
# significant difference in mean response times between the four drugs.
# Results showed that the type of drug used lead to statistically significant differences in response time (F(3, 12) = 24.75887, p < 0.001).

