'''
Author  : B.M.G.G.K. Ralapaksha
Date    : 06/12/21
Topic   : Chi-square test
Input   : Contingency table of observed data

Output  : Mosaic plot of data, Chi-square contingency test results
'''

from scipy import stats
import pandas as pd
from statsmodels.graphics.mosaicplot import mosaic
import matplotlib.pyplot as plt

# Question III
# Contingency table
# index means rows, columns means columns of the dataset

print("Dataset :")
data = pd.DataFrame([[1, 10, 37], [49, 35, 9]],
                    index=['Eaten by birds', 'Not eaten by birds'],
                    columns=['Uninfected', 'Lightly infected', 'Highly infected'])
print(data, '\n')

# Question IV
# Mosaic plot

data_stack = data.stack()

fig, axes = plt.subplots(figsize=(10, 5))
mosaic(data_stack, gap=0.05, title='Mosaic pot for contingency table', ax=axes)

plt.show()

# Question V
# Chi-square test

chi_val, p_val, dof, expec_val = stats.chi2_contingency(data)

print('Chi-square test :\n \tChi-square statistics = %.3f, p - value =%.3f, dof =%.3f' % (chi_val, p_val, dof), '\n')

# Question VI
# to get expected values into a dataframe

print('Expected value table :')
expected_value = pd.DataFrame(data=expec_val[:,:],
             index=['Eaten by birds', 'Not eaten by birds'],
             columns=['Uninfected', 'Lightly infected', 'Highly infected']).round(2)

print(expected_value, '\n')

# END