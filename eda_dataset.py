"""
To learn Exploratory Data Analysis (EDA) Descriptive statistics, visualization, and plotting,
Handling missing data and outliers
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

# 1. LOAD THE DATASET
np.random.seed(42)
data = {
    'CustomerID': range(101, 111),
    'Age': [25, 30, 22, 35, np.nan, 28, 45, 110, 29, 32],
    'MonthlyCharges': [50.5, 70.0, 65.2, np.nan, 80.0, 55.0, 60.5, 95.0, 1200.0, 68.0],
    'TenureMonths': [12, 24, 6, 36, 18, 15, 48, 60, 2, 30],
    'Churn': ['No', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No']
}

df = pd.DataFrame(data)

print("--- Initial Dataset ---")
print(df.head())
print("\nDataset Info:")
print(df.info())


# 2. PERFORM DESCRIPTIVE STATISTICS
print("\n--- Descriptive Statistics ---")
print("Summary Statistics:\n", df.describe())

print("Mean Age:", df['Age'].mean())
print("Median Age:", df['Age'].median())
print("Mode Age:", df['Age'].mode()[0])
print("Standard Deviation (MonthlyCharges):", df['MonthlyCharges'].std())
print("Variance (MonthlyCharges):", df['MonthlyCharges'].var())
print("Min / Max Tenure:", df['TenureMonths'].min(), "/", df['TenureMonths'].max())
print("Quantiles (TenureMonths):\n", df['TenureMonths'].quantile([0.25, 0.50, 0.75]))


# 3. PERFORM DATA VISUALIZATION
sns.set_theme(style="whitegrid")

plt.figure(figsize=(6, 4))
plt.hist(df['TenureMonths'], bins=5, color='skyblue', edgecolor='black')
plt.title('Tenure Distribution')
plt.xlabel('Tenure (Months)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 4))
sns.boxplot(x=df['MonthlyCharges'], color='lightgreen')
plt.title('Box Plot of Monthly Charges')
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 4))
plt.scatter(df['TenureMonths'], df['MonthlyCharges'], color='purple')
plt.title('Tenure vs Monthly Charges')
plt.xlabel('Tenure (Months)')
plt.ylabel('Monthly Charges')
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 4))
numeric_df = df[['Age', 'MonthlyCharges', 'TenureMonths']].dropna()
corr_matrix = numeric_df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.tight_layout()
plt.show()


# 4. HANDLE MISSING DATA
print("\n--- Handling Missing Data ---")
print("Missing values count per column:\n", df.isnull().sum())

df['Age'] = df['Age'].fillna(df['Age'].mean())
df['MonthlyCharges'] = df['MonthlyCharges'].fillna(df['MonthlyCharges'].mean())

print("\nMissing values after mean imputation:\n", df.isnull().sum())


# 5. DETECT AND HANDLE OUTLIERS
print("\n--- Handling Outliers ---")

df['Age_Zscore'] = zscore(df['Age'])
df['Charges_Zscore'] = zscore(df['MonthlyCharges'])

outliers = df[(df['Age_Zscore'].abs() > 2) | (df['Charges_Zscore'].abs() > 2)]
print("Detected Outliers:\n", outliers[['CustomerID', 'Age', 'MonthlyCharges']])

df_no_outliers = df[(df['Age_Zscore'].abs() <= 2) & (df['Charges_Zscore'].abs() <= 2)].copy()

def cap_outliers(series):
    upper_limit = series.mean() + 2 * series.std()
    lower_limit = series.mean() - 2 * series.std()
    return series.clip(lower=lower_limit, upper=upper_limit)

df['Age_Capped'] = cap_outliers(df['Age'])
df['MonthlyCharges_Capped'] = cap_outliers(df['MonthlyCharges'])


# 6. VERIFY AND SAVE CLEANED DATASET
final_df = df.drop(columns=['Age_Zscore', 'Charges_Zscore'])

print("\n--- Final Cleaned Dataset ---")
print(final_df.head(10))

print("\nRemaining null values:", final_df.isnull().sum().sum())

final_df.to_csv('cleaned_customer_churn.csv', index=False)
print("\nCleaned dataset saved successfully as 'cleaned_customer_churn.csv'.")

"""
--> Output
--- Initial Dataset ---
   CustomerID   Age  MonthlyCharges  TenureMonths Churn
0         101  25.0            50.5            12    No
1         102  30.0            70.0            24    No
2         103  22.0            65.2             6   Yes
3         104  35.0             NaN            36    No
4         105   NaN            80.0            18   Yes

Dataset Info:
<class 'pandas.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 5 columns):
 #   Column          Non-Null Count  Dtype  
---  ------          --------------  -----  
 0   CustomerID      10 non-null     int64  
 1   Age             9 non-null      float64
 2   MonthlyCharges  9 non-null      float64
 3   TenureMonths    10 non-null     int64  
 4   Churn           10 non-null     str    
dtypes: float64(2), int64(2), str(1)
memory usage: 532.0 bytes
None

--- Descriptive Statistics ---
Summary Statistics:
        CustomerID         Age  MonthlyCharges  TenureMonths
count    10.00000    9.000000        9.000000     10.000000
mean    105.50000   39.555556      193.800000     25.100000
std       3.02765   27.217233      377.559528     18.585837
min     101.00000   22.000000       50.500000      2.000000
25%     103.25000   28.000000       60.500000     12.750000
50%     105.50000   30.000000       68.000000     21.000000
75%     107.75000   35.000000       80.000000     34.500000
max     110.00000  110.000000     1200.000000     60.000000
Mean Age: 39.55555555555556
Median Age: 30.0
Mode Age: 22.0
Standard Deviation (MonthlyCharges): 377.55952841902956
Variance (MonthlyCharges): 142551.1975
Min / Max Tenure: 2 / 60
Quantiles (TenureMonths):
 0.25    12.75
0.50    21.00
0.75    34.50
Name: TenureMonths, dtype: float64

--- Handling Missing Data ---
Missing values count per column:
 CustomerID        0
Age               1
MonthlyCharges    1
TenureMonths      0
Churn             0
dtype: int64

Missing values after mean imputation:
 CustomerID        0
Age               0
MonthlyCharges    0
TenureMonths      0
Churn             0
dtype: int64

--- Handling Outliers ---
Detected Outliers:
    CustomerID    Age  MonthlyCharges
7         108  110.0            95.0
8         109   29.0          1200.0

--- Final Cleaned Dataset ---
   CustomerID         Age  MonthlyCharges  TenureMonths Churn  Age_Capped  MonthlyCharges_Capped
0         101   25.000000            50.5            12    No   25.000000              50.500000
1         102   30.000000            70.0            24    No   30.000000              70.000000
2         103   22.000000            65.2             6   Yes   22.000000              65.200000
3         104   35.000000           193.8            36    No   35.000000             193.800000
4         105   39.555556            80.0            18   Yes   39.555556              80.000000
5         106   28.000000            55.0            15    No   28.000000              55.000000
6         107   45.000000            60.5            48    No   45.000000              60.500000
7         108  110.000000            95.0            60   Yes   90.876862              95.000000
8         109   29.000000          1200.0             2   Yes   29.000000             905.733074
9         110   32.000000            68.0            30    No   32.000000              68.000000

Remaining null values: 0

Cleaned dataset saved successfully as 'cleaned_customer_churn.csv'.

==================================================
"""