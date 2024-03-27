# A three-way ANOVA is used to determine whether or not there is a statistically significant difference between the means of three or more independent groups 
# that have been split on three factors.

"""
Suppose a researcher wants to determine if two training programs lead to different mean improvements in jumping height among college basketball players.

The researcher suspects that gender and division (Division I or II) may also affect jumping height so he collects data for these factors as well.

His goal is to perform a three-way ANOVA to determine how training program, gender, and division affect jumping height.

"""

import numpy as np
import pandas as pd

#create DataFrame
df = pd.DataFrame({'program': np.repeat([1, 2], 20),
                   'gender': np.tile(np.repeat(['M', 'F'], 10), 2),
                   'division': np.tile(np.repeat([1, 2], 5), 4),
                   'height': [7, 7, 8, 8, 7, 6, 6, 5, 6, 5,
                              5, 5, 4, 5, 4, 3, 3, 4, 3, 3,
                              6, 6, 5, 4, 5, 4, 5, 4, 4, 3,
                              2, 2, 1, 4, 4, 2, 1, 1, 2, 1]})

#view first ten rows of DataFrame 
print(df[:10])

import statsmodels.api as sm
from statsmodels.formula.api import ols

#perform three-way ANOVA
model = ols("""height ~ C(program) + C(gender) + C(division) +
               C(program):C(gender) + C(program):C(division) + C(gender):C(division) +
               C(program):C(gender):C(division)""", data=df).fit()

print(sm.stats.anova_lm(model, typ=2))

"""
In conclusion, we would state that training program, gender, and division are all significant predictors of the jumping height increase among players.

We would also state that there are no significant interaction effects between these three factors.

"""