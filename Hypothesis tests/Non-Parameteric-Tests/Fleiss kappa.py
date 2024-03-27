# kohen's kappa version for more than 2
# fleiss_kappa
from statsmodels.stats.inter_rater import fleiss_kappa
import pandas as pd

rater1 = [0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0]
rater2 = [0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0]
rater3 = [0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0]

rating_table = pd.DataFrame({'rater1':rater1,"rater2":rater2,"rater3":rater3})
melted_table = pd.melt(rating_table)
crosstab_table = pd.crosstab(melted_table["variable"],melted_table["value"])

print(fleiss_kappa(crosstab_table))
