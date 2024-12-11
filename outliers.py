import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

df = pd.read_csv('your_dataset.csv')

z_scores = np.abs(zscore(df.select_dtypes(include=[np.number])))
z_outliers = (z_scores > 3)

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
iqr_outliers = (df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))

print("Outliers detected using Z-Score method:")
print(z_outliers)

print("\nOutliers detected using IQR method:")
print(iqr_outliers)

sns.boxplot(data=df.select_dtypes(include=[np.number]))
plt.title('Boxplot for Numerical Features')
plt.show()
