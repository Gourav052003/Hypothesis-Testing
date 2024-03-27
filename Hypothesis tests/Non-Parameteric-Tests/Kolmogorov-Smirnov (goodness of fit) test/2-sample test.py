# two sample Kolmogorov-Smirnov test

rng = np.random.default_rng()
sample1 = stats.uniform.rvs(size=100, random_state=rng)
sample2 = stats.norm.rvs(size=110, random_state=rng)
print(stats.ks_2samp(sample1, sample2))