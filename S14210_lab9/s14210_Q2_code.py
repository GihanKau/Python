'''
Author  : B.M.G.G.K. Ralapaksha
Date    : 06/12/21
Topic   : Independent sample t-test
Input   : horn lengths of Horned lizards as “HornedLizards.csv”

Output  : Descriptive statistics, Histograms, qqplots, Normality test values,
          One-sample t=test values
'''

from scipy import stats
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

horn_data = pd.read_csv("HornedLizards.csv")

# to remove missing values
horn_data = horn_data.dropna(axis=0, how='any')
print(horn_data)

# Subset data (since it contains two groups)

dead = horn_data.query('Survive == "dead"')['Squamosal horn length']
survived = horn_data.query('Survive == "survived"')['Squamosal horn length']

# Question III
# Descriptive statistics
des_sts = horn_data.groupby('Survive').describe()
print('Descriptive statistics : \n\t', des_sts, '\n')

# Question IV
# Histograms
# (1,2) means 1 row 2 columns (2 graphs)
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# axes[0] = left, axes[1] = right
sns.histplot(dead, kde=True, ax=axes[0],)
axes[0].set_title('Histogram of \'Dead\' sample')

sns.histplot(survived, kde=True, ax=axes[1])
axes[1].set_title('Histogram of \'Survived\' sample')

plt.xlabel('Squamosal horn length')
plt.show()

# QQ plots
from statsmodels.graphics.gofplots import qqplot
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# axes[0] = left, axes[1] = right
qqplot(dead, line='s', ax=axes[0])
axes[0].set_title('QQplot for \'Dead\' sample')

qqplot(survived, line='s', ax=axes[1])
axes[1].set_title('QQplot for \'Survived\' sample')

plt.show()

# Shapiro-Wilk test (Normality test)

stat, p = stats.shapiro(dead)
print('Normality test for \'Dead\' sample :\n \tTest statistics = %.3f, p =%.3f' % (stat, p), '\n')

stat, p = stats.shapiro(survived)
print('Normality test for \'Survived\' sample :\n \tTest statistics = %.3f, p =%.3f' % (stat, p), '\n')

# Question V

# boxplot
sns.boxplot(x='Survive', y='Squamosal horn length', data=horn_data,
            showmeans=True, meanprops={"marker": "+", "markeredgecolor": "white"})

plt.show()

# violin plot
sns.violinplot(x='Survive', y='Squamosal horn length', data=horn_data)
plt.show()

# Non-parametric test
stat, p = stats.mannwhitneyu(dead, survived, alternative="two-sided")
print('Mann whitney U test for two samples :\n \tTest statistics = %.3f, p =%.3f' % (stat, p))
