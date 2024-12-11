import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('your_dataset.csv')

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

iqr_outliers = (df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))

print("Outliers detected using IQR method:")
print(iqr_outliers)

# Plot boxplot for numerical features
sns.boxplot(data=df.select_dtypes(include=[np.number]))
plt.title('Boxplot for Numerical Features')
plt.show()
