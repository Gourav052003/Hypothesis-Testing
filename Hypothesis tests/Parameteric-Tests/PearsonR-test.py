

import pandas as pd
import math
import warnings
warnings.filterwarnings('ignore')

CARDIO_BASE_df = pd.read_csv('Data\\cardio_base.csv',delimiter=',')
print(CARDIO_BASE_df.head())

CARDIO_BASE_df["age"] = CARDIO_BASE_df["age"].apply(lambda x:math.floor(x/365))
print(CARDIO_BASE_df.head())

import seaborn as sns

# checking for normally distributed data beacuse parametric test give accurate results with normally distributes data 
# although parameteric test can also be done for non - normal distributed data
sns.distplot(CARDIO_BASE_df["weight"])

from scipy.stats import pearsonr

# alternative{‘two-sided’, ‘greater’, ‘less’}, optional
# Defines the alternative hypothesis. Default is ‘two-sided’. The following options are available:

# ‘two-sided’: the correlation is nonzero

# ‘less’: the correlation is negative (less than zero)

# ‘greater’: the correlation is positive (greater than zero)

print(pearsonr(x=CARDIO_BASE_df["weight"].sample(100).values,y = CARDIO_BASE_df["weight"].sample(100).values))