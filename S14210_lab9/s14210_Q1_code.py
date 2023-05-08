'''
Author  : B.M.G.G.K. Ralapaksha
Date    : 06/12/21
Topic   : One sample t-test
Input   : Body-temperature measurements on randomly chosen healthy people
          as “Temperature.csv” file.

Output  : Descriptive statistics, Histogram, qqplot, Normality test values,
          One-sample t=test values
'''


from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Question III

temp_data = pd.read_csv("Temperature.csv")
print('Dataset : \n', temp_data, "\n")

# -------Descriptive statistics----------

des_sts = temp_data.describe()

print('Descriptive statistics : \n', round(des_sts, 3), "\n")

# Question IV

# histogram using matplotlib

# plt.hist(temp_data)
# plt.title('Body temperature')
# plt.show()

# -------Histogram using seaborn---------
sns.histplot(temp_data, bins=15, kde=True)
plt.xlabel("Body temperature (F)")
plt.title('Histogram of temperature data')

plt.show()

# --------------QQ plot------------------

from statsmodels.graphics.gofplots import qqplot
qqplot(temp_data['temperature'], line='s')
plt.title('QQplot for temperature')
plt.show()

# ---Shapiro-Wilk test (Normality test)---

stat, p = stats.shapiro(temp_data)
print('Normality test : \n \tTest statistics = %.3f, p - value =%.3f' % (stat, p), '\n')

# ----------One-sample t-test-------------

check_value = 98.6

stat, p = stats.ttest_1samp(temp_data, check_value, alternative="two-sided")
print('One-sample t-test : \n \tTest statistics = %.3f, p - value = %.3f' % (stat, p), '\n')



