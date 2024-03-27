# two sample independent test
# Mann Whiteney test (handle ties cases unlike rank sums)

from scipy.stats import mannwhitneyu

males = [19, 22, 16, 29, 24]
females = [20, 11, 17, 12]
print(mannwhitneyu(males, females, method="exact"))