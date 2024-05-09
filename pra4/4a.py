import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
np.random.seed(42)
sample1 = np.random.normal(loc=10, scale=2, size=30)
sample2 = np.random.normal(loc=12, scale=2, size=30)
t_statistic, p_value = stats.ttest_ind(sample1, sample2)
alpha = 0.05
plt.hist(sample1, alpha=0.5, label='Sample 1', color='blue')
plt.hist(sample2, alpha=0.5, label='Sample 2', color='orange')
plt.axvline(np.mean(sample1), color='blue', linestyle='dashed', linewidth=2)
plt.axvline(np.mean(sample2), color='orange', linestyle='dashed', linewidth=2)
if p_value < alpha:
    critical_region = np.linspace(min(sample1.min(), sample2.min()), max(sample1.max(), sample2.max()), 1000)
    plt.fill_between(critical_region, 0, 5, color='red', alpha=0.3, label='Critical Region')
plt.legend()
plt.show()
if p_value < alpha:
    if np.mean(sample1) > np.mean(sample2):
        print("Conclusion: Sample 1 mean is significantly higher than Sample 2.")
    else:
        print("Conclusion: Sample 2 mean is significantly higher than Sample 1.")
else:
    print("Conclusion: No significant difference between sample means.")
