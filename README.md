**Task-02**
Perform data cleaning and exploratory data analysis (EDA) on a dataset of your choice, such as the Titanic dataset from Kaggle. Explore the relationships between variables and identify patterns and trends in the data.

Sample Dataset :- https://www.kaggle.com/c/titanic/data

This project analyzes the Titanic dataset, a well-known dataset from the Titanic disaster, to explore and visualize various factors related to passenger survival. The dataset contains information about passengers, including their demographics, class, fare, and more. The project aims to uncover insights into what factors influenced survival rates during the tragedy.

### Key Steps and Visualizations:

1. **Data Loading and Basic Exploration:**
   - The dataset is loaded using pandas and basic information such as the number of rows and columns, data types, and summary statistics are reviewed. Missing values and duplicate records are also identified and addressed.

2. **Data Cleaning:**
   - The 'Cabin' column, which has many missing values, is dropped.
   - Missing values in the 'Age' column are filled with the mean age, and missing values in the 'Embarked' column are filled with the most frequent value (mode).

3. **Data Visualization:**
   - **Survival Counts:** A count plot shows the number of survivors and non-survivors.
   - **Survival by Gender:** A count plot illustrates survival rates by gender, revealing that a higher proportion of females survived compared to males.
   - **Class Distribution:** A plot displays the distribution of passengers across different classes (1st, 2nd, 3rd).
   - **Survival by Class:** A count plot shows survival rates across different passenger classes, highlighting that higher-class passengers had higher survival rates.
   - **Embarkment Points:** Visualizations show the distribution of passengers from different embarkation points (Southampton, Cherbourg, Queenstown).
   - **Family Size (Siblings/Spouses and Parents/Children):** Count plots depict the number of passengers with varying numbers of siblings/spouses (SibSp) and parents/children (Parch) aboard.
   - **Fare and Age Distributions:** Histograms with kernel density estimates (KDE) show the distribution of fares paid by passengers and the distribution of ages.
   - **Age Categories and Survival Rates:** The 'Age' column is categorized into groups (e.g., Infant, Child, Teenager, etc.), and survival rates are calculated for each age category.

4. **Correlation Analysis:**
   - A heatmap of the correlation matrix for numerical features (including transformed categorical variables like 'Sex' and 'Embarked') helps identify potential relationships between variables and survival.

### Insights and Findings:
- **Gender and Survival:** Women had a higher survival rate than men, possibly due to the "women and children first" policy during evacuation.
- **Class and Survival:** Passengers in higher classes (1st and 2nd) had better survival rates than those in the 3rd class.
- **Embarkation Points:** The embarkation point had an impact on survival rates, with some variations among passengers from different ports.
- **Age and Survival:** Younger passengers and children had higher survival rates, particularly in certain age categories.

The project provides a comprehensive exploration of the Titanic dataset, combining data cleaning, visualization, and analysis to draw meaningful insights into the factors influencing passenger survival during the Titanic disaster.


**Overview of the Dataset:**
The data has been split into two groups:

training set (train.csv)
test set (test.csv)
The training set should be used to build your machine learning models. For the training set, we provide the outcome (also known as the “ground truth”) for each passenger. Your model will be based on “features” like passengers’ gender and class. You can also use feature engineering to create new features.

The test set should be used to see how well your model performs on unseen data. For the test set, we do not provide the ground truth for each passenger. It is your job to predict these outcomes. For each passenger in the test set, use the model you trained to predict whether or not they survived the sinking of the Titanic.

Here is the overview of the dataset:
![Screenshot 2024-07-28 093630](https://github.com/user-attachments/assets/b6d697cc-7f1f-40e0-9768-349deb080704)
![Screenshot 2024-07-28 093541](https://github.com/user-attachments/assets/e2e80339-eaa7-48c6-9574-85c9051de89e)
![Screenshot 2024-07-28 093550](https://github.com/user-attachments/assets/f5ccd555-1537-4fbc-95b7-11b2c4294a9d)
![Screenshot 2024-07-28 093557](https://github.com/user-attachments/assets/cd0f6cb9-8370-4542-9ffb-0e6485caf9cf)
![Screenshot 2024-07-28 093606](https://github.com/user-attachments/assets/dcf9117a-c103-472c-950f-521cb56e2bf8)
![Screenshot 2024-07-28 093612](https://github.com/user-attachments/assets/dfc3adf2-a38c-4bb6-bd29-498e3d528c1e)
![Screenshot 2024-07-28 093618](https://github.com/user-attachments/assets/458fbd9c-3d39-4e1e-a703-23b21f2e2fa9)
![Screenshot 2024-07-28 093630](https://github.com/user-attachments/assets/ea067411-6f85-4617-b8b9-a6c3389a72f5)







