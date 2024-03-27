# two way annova

# A botanist wants to know whether or not plant growth is influenced by sunlight exposure and watering frequency. 
# She plants 30 seeds and lets them grow for two months under different conditions for sunlight exposure and watering frequency. 
# After two months, she records the height of each plant, in inches

# To perform a two-way ANOVA to determine if watering frequency and sunlight exposure have a significant effect on plant growth, and 
# to determine if there is any interaction effect between watering frequency and sunlight exposure.


# water: how frequently each plant was watered: daily or weekly
# sun: how much sunlight exposure each plant received: low, medium, or high
# height: the height of each plant (in inches) after two months

import numpy as np
import pandas as pd

#create data
df = pd.DataFrame({'water': np.repeat(['daily', 'weekly'], 15),
                   'sun': np.tile(np.repeat(['low', 'med', 'high'], 5), 2),
                   'height': [6, 6, 6, 5, 6, 5, 5, 6, 4, 5,
                              6, 6, 7, 8, 7, 3, 4, 4, 4, 5,
                              4, 4, 4, 4, 4, 5, 6, 6, 7, 8]})

#view first ten rows of data 
print(df[:10])

import statsmodels.api as sm
from statsmodels.formula.api import ols

#perform two-way ANOVA
model = ols('height ~ C(water) + C(sun) + C(water):C(sun)', data=df).fit()
print(sm.stats.anova_lm(model, typ=2))

# water: p-value = .000527
# sun: p-value = .0000002
# water*sun: p-value = .120667

# Since the p-values for water and sun are both less than .05, this means that both factors have a statistically significant effect on plant height.
# And since the p-value for the interaction effect (.120667) is not less than .05, this tells us that there is no significant interaction effect between 
# sunlight exposure and watering frequency.