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

# ztest is used for comparing the means of one sample with specified population mean value is known as one sample test,
# where comparing two samples means differenece or correlation with each other is called two sample test 
from statsmodels.stats.weightstats import ztest

# one sample ztest
# If the p-value <0.05 than null hypothesis of having sample mean equal to 74.15 is rejected
print(ztest(x1 = CARDIO_BASE_df["weight"].sample(100).values,value = 74.15))
