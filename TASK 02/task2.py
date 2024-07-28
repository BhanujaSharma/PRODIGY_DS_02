import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Titanic dataset
titanic_data = pd.read_csv('/mnt/data/titanic.csv')
# Display the first few rows of the dataset
titanic_data.head()
# Check for missing values
titanic_data.isnull().sum()
# Fill missing 'Age' values with the median age
titanic_data['Age'].fillna(titanic_data['Age'].median(), inplace=True)

# Fill missing 'Embarked' values with the most frequent port of embarkation
titanic_data['Embarked'].fillna(titanic_data['Embarked'].mode()[0], inplace=True)

# Drop the 'Cabin' column
titanic_data.drop('Cabin', axis=1, inplace=True)
# Convert 'Sex' to numeric
titanic_data['Sex'] = titanic_data['Sex'].map({'male': 0, 'female': 1})

# Convert 'Embarked' to numeric
titanic_data['Embarked'] = titanic_data['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})
# Display descriptive statistics
titanic_data.describe()
# Survival rate by gender
gender_survival_rate = titanic_data.groupby('Sex')['Survived'].mean()
gender_survival_rate.plot(kind='bar', color=['blue', 'pink'])
plt.title('Survival Rate by Gender')
plt.xlabel('Gender')
plt.ylabel('Survival Rate')
plt.xticks(ticks=[0, 1], labels=['Male', 'Female'])
plt.show()
# Survival rate by class
class_survival_rate = titanic_data.groupby('Pclass')['Survived'].mean()
class_survival_rate.plot(kind='bar', color=['brown', 'green', 'orange'])
plt.title('Survival Rate by Class')
plt.xlabel('Class')
plt.ylabel('Survival Rate')
plt.show()
# Age distribution of survivors and non-survivors
sns.histplot(titanic_data[titanic_data['Survived'] == 1]['Age'], color='green', kde=True, label='Survived')
sns.histplot(titanic_data[titanic_data['Survived'] == 0]['Age'], color='red', kde=True, label='Not Survived')
plt.title('Age Distribution of Survivors and Non-Survivors')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.legend()
plt.show()
# Correlation matrix
correlation_matrix = titanic_data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
