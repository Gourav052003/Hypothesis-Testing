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

# t-test is used when we do not know the population standard deviation
from scipy.stats import ttest_1samp

# one sample t-test
# alternative parameter is used for <,> = popmean

ttest_1samp(a=CARDIO_BASE_df["weight"].sample(100).values, popmean=74.15)