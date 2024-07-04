import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('Bank Customer Churn Prediction.csv')

# First individual scatterplots

# Create scatter plots for each pair of variables with hue for 'churn'
plt.figure(figsize=(12, 10))

# Scatter plot for credit_score vs. age
plt.subplot(2, 2, 1)
sns.scatterplot(data=df, x='credit_score', y='age', hue='churn')
plt.title('Credit Score vs Age')

# Scatter plot for balance vs. estimated_salary
plt.subplot(2, 2, 2)
sns.scatterplot(data=df, x='balance', y='estimated_salary', hue='churn')
plt.title('Balance vs Estimated Salary')

# Scatter plot for credit_score vs. balance
plt.subplot(2, 2, 3)
sns.scatterplot(data=df, x='credit_score', y='balance', hue='churn')
plt.title('Credit Score vs Balance')

# Scatter plot for age vs. estimated_salary
plt.subplot(2, 2, 4)
sns.scatterplot(data=df, x='age', y='estimated_salary', hue='churn')
plt.title('Age vs Estimated Salary')

plt.tight_layout()
plt.show()



# Now a single scatterplot for all

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('Bank Customer Churn Prediction.csv')

# Initialize the figure
plt.figure(figsize=(15, 10))

# Scatter plot for credit_score vs. age
sns.scatterplot(data=df, x='credit_score', y='age', hue='churn', palette='viridis', label='Credit Score vs Age')

# Scatter plot for balance vs. estimated_salary
sns.scatterplot(data=df, x='balance', y='estimated_salary', hue='churn', palette='coolwarm', label='Balance vs Estimated Salary', marker='o')

# Scatter plot for credit_score vs. balance
sns.scatterplot(data=df, x='credit_score', y='balance', hue='churn', palette='Spectral', label='Credit Score vs Balance', marker='x')

# Scatter plot for age vs. estimated_salary
sns.scatterplot(data=df, x='age', y='estimated_salary', hue='churn', palette='husl', label='Age vs Estimated Salary', marker='s')

# Add titles and labels
plt.title('Multiple Scatter Plots on a Single Plot')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.legend()

# Show the plot
plt.show()


# Now a heatmap

# Select the relevant columns
relevant_columns = ['credit_score', 'age', 'balance', 'estimated_salary', 'tenure', 'products_number', 'credit_card', 'active_member']

# Calculate the correlation matrix
corr_matrix = df[relevant_columns].corr()

# Create a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)

# Add a title
plt.title('Correlation Heatmap of Selected Features')

# Show the plot
plt.show()