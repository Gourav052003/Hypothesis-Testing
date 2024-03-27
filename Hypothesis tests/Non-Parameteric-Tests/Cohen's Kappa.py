# Kohen's kappa acore

"""
Suppose two art museum curators are asked to rate 15 paintings on whether they’re good enough to be shown in a new exhibit.

"""

from sklearn.metrics import cohen_kappa_score

#define array of ratings for both raters
rater1 = [0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0]
rater2 = [0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0]

#calculate Cohen's Kappa
print(cohen_kappa_score(rater1, rater2))

# Cohen’s Kappa turns out to be 0.33628.

# Based on the table earlier, we would say that the two raters only had a “fair” level of agreement.
