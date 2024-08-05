import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(
    "C:\\Users\\Admin\Documents\\AIO---262-Trinh-Xd\\Module 2\\Week 04\\advertising.csv")


def correlation(x, y):
    # Your code here #
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sqrt(np.sum((x - x_mean)**2) * np.sum((y - y_mean)**2))

    if denominator == 0:
        return 0  # Handle cases where the denominator is zero

    return numerator / denominator

# Question 5


'''
x = data['TV']
y = data['Radio']
corr_xy = correlation(x, y)
print(f" Correlation between TV and Sales : { round ( corr_xy , 2)}")
'''

# Question 6
'''
features = ['TV', 'Radio', 'Newspaper']

for feature_1 in features:
    for feature_2 in features:
        correlation_value = correlation(data[feature_1], data[feature_2])
        print(
            f" Correlation between { feature_1 } and {feature_2 }: {round(correlation_value , 2)}")
        
'''

# Question 7

x = data['Radio']
y = data['Newspaper']

result = np.corrcoef(x, y)  # Your code here #
print(result)


# Question 8
print(data.corr())

# Question 9
plt.figure(figsize=(10, 8))
# Your code here #
data_corr = data.corr()
sns.heatmap(data_corr, annot=True, fmt=".2f", linewidth=.5)
plt.show()
