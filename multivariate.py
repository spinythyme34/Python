import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.linear_model import LinearRegression

# Load the data
data = pd.read_csv('data.csv')

# Clean the data
data.dropna(inplace=True)

# Calculate summary statistics
print(data.describe())

# Visualize the data
plt.figure(figsize=(10,6))

# Scatter plot
plt.subplot(1, 3, 1)
plt.scatter(data['variable1'], data['variable2'])
plt.title('Scatter Plot')

# Bar plot
plt.subplot(1, 3, 2)
data['variable1'].value_counts().plot(kind='bar')
plt.title('Bar Plot')

# Histogram
plt.subplot(1, 3, 3)
plt.hist(data['variable1'])
plt.title('Histogram')

plt.tight_layout()
plt.show()

# Correlation analysis
corr_matrix = data.corr()
print(corr_matrix)

# Heatmap
plt.figure(figsize=(10,6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)
plt.title('Correlation Heatmap')
plt.show()

# Regression analysis
X = data[['variable1', 'variable2']]
y = data['dependent_variable']
model = LinearRegression()
model.fit(X, y)
print(model.coef_)
print(model.intercept_)
