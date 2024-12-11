import pandas as pd
from scipy.stats import ttest_ind

# Load the data with the correct encoding
file_path = '/content/pizza.csv'
# Display data to confirm structure
print(pizza_data.info())
print(pizza_data.head())

# Extract the data for each unit based on the column names
unit1 = pizza_data['Making Unit 1']
unit2 = pizza_data['Making Unit 2']

# Perform an independent samples t-test
t_stat, p_value = ttest_ind(unit1, unit2, equal_var=False)  # Welch's t-test if variances may differ

# Print the t-statistic and p-value
print("t-statistic:", t_stat)
print("p-value:", p_value)

# Interpret the result
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference in the average diameter.")
else:
    print("Fail to reject the null hypothesis: No significant difference in average diameter.")

