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

# two sample ztest
# If the p-value <0.05 than null hypothesis of having samples mean difference equal to 0 is rejected
# Here the standard deviation of the samples is assumed to be the same, usevar : 'pooled' by default
# You can change the hypotheis using "alternative" paramneter

# this two sample z test also can be used for independent paired samples for comparing difference in means
ztest(x1 = CARDIO_BASE_df["weight"].sample(100).values,x2 = CARDIO_BASE_df["weight"].sample(100).values,value = 0)