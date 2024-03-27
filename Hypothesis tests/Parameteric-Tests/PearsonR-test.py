from scipy.stats import pearsonr

# alternative{‘two-sided’, ‘greater’, ‘less’}, optional
# Defines the alternative hypothesis. Default is ‘two-sided’. The following options are available:

# ‘two-sided’: the correlation is nonzero

# ‘less’: the correlation is negative (less than zero)

# ‘greater’: the correlation is positive (greater than zero)

print(pearsonr(x=CARDIO_BASE_df["weight"].sample(100).values,y = CARDIO_BASE_df["weight"].sample(100).values))