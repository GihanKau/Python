'''
Author  : B.M.G.G.K. Ralapaksha
Date    : 06/12/21
Topic   : Paired t-test
Input   : "BlackbirdTestosterone.csv" file

Output  : Descriptive statistics, Histograms, qqplots, Normality test values,
          paired sample t=test values
'''

from scipy import stats
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

rate_data = pd.read_csv("BlackbirdTestosterone.csv")

# Question III
# Descriptive statistics
des_sts_before = rate_data['log before'].describe()
des_sts_after = rate_data['log after'].describe()
des_sts_difference = rate_data['dif in logs'].describe()

print('Descriptive statistics :\n')
print('log before : \n\t', 'Mean : ', round(des_sts_before['mean'], 3), ', SD : ', round(des_sts_before['std'], 3), '\n')
print('log after : \n\t', 'Mean : ', round(des_sts_after['mean'], 3), ', SD : ', round(des_sts_after['std'], 3), '\n')
print('log difference : \n\t', 'Mean : ', round(des_sts_difference['mean'], 3), ', SD : ', round(des_sts_difference['std'], 3), '\n')

# Question IV

# Histograms

sns.histplot(rate_data['dif in logs'], kde=True, bins=10)
plt.title('Histogram of \'log difference\'')
plt.xlabel('log difference')

plt.show()

# QQ plots

from statsmodels.graphics.gofplots import qqplot

qqplot(rate_data['dif in logs'], line='s')
plt.title('QQplot of \'log difference\'')

plt.show()

# Shapiro-Wilk test (Normality test)

stat, p = stats.shapiro(rate_data['dif in logs'])
print('Normality test for \'log difference\' :\n \tTest statistics = %.3f, p - value =%.3f' % (stat, p), '\n')

# Question V

# boxplot
sns.boxplot(data=rate_data[['Before', 'After']],
            showmeans=True, meanprops={"marker": "+", "markeredgecolor": "white"})
plt.ylabel('Antibody production rate')
plt.show()

# violin plot
sns.violinplot(data=rate_data[['Before', 'After']])
plt.ylabel('Antibody production rate')
plt.show()

# Parametric test (paired-sample t-test)

stat, p = stats.ttest_rel(rate_data['log before'], rate_data['log after'], alternative='greater')
print('Paired-sample t-test :\n \tTest statistics = %.3f, p - value =%.3f' % (stat, p))