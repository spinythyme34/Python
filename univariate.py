# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Load the data
data = pd.read_csv('data.csv')

# Clean the data
data.dropna(inplace=True)

# Calculate summary statistics
print(data.describe())

# Visualize the data
plt.figure(figsize=(10,6))

# Histogram
plt.subplot(1, 3, 1)
plt.hist(data['variable'])
plt.title('Histogram')

# Box Plot
plt.subplot(1, 3, 2)
plt.boxplot(data['variable'])
plt.title('Box Plot')

# Bar Plot (for categorical data)
# plt.subplot(1, 3, 3)
# data['variable'].value_counts().plot(kind='bar')
# plt.title('Bar Plot')

plt.tight_layout()
plt.show()

# Detect outliers
Q1 = data['variable'].quantile(0.25)
Q3 = data['variable'].quantile(0.75)
IQR = Q3 - Q1
outliers = data[(data['variable'] < Q1 - 1.5 * IQR) | (data['variable'] > Q3 + 1.5 * IQR)]
print(outliers)

# Check for normality
print(stats.normaltest(data['variable']))
