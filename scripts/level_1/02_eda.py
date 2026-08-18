import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

stock = pd.read_csv("data/cleaned/clean_stock.csv", parse_dates=["date"], index_col="date")

print("# ============================================================")
print("1. Data Exploration")
print("# ============================================================")
print("1.1 First 5 Records\n")
print(stock.head(5))
print("1.2 Last 5 Records\n")
print(stock.tail(5))
print("1.3 Dataset Information\n")
print(stock.info)
print("1.4 Number of Raws * Columns\n")
print(stock.shape)
print("1.5 Dataset Columns' label\n")
print(stock.columns)
print("1.6 Data types\n")
print(stock.dtypes)
print("1.7 Summary Statistics\n")
print(stock.describe())

print("# ============================================================")
print("2. Summary Statistics in Details")
print("# ============================================================")
Mean = stock.mean(numeric_only=True).round(2)

print("Mean\n",Mean)
print("# ============================================================")

Median = stock.median(numeric_only=True).round(2)

print("Median\n",Median)
print("# ============================================================")
Standard_Deviation = stock.std(numeric_only=True).round(2)

print("Standard_Deviation\n",Standard_Deviation)
print("# ============================================================")
Mode = stock.mode(numeric_only=True).round(2)

print("Mode\n",Mode)
print("# ============================================================")
Min = stock.min(numeric_only=True).round(2)

print("Min\n",Min)
print("# ============================================================")
Max = stock.max(numeric_only=True).round(2)

print("Max\n",Max)
print("# ============================================================")
Q1 = stock.quantile(0.25,numeric_only=True)

print("Q1\n",Q1)
print("# ============================================================")
Q3 = stock.quantile(0.75, numeric_only=True)

print("Q3\n",Q3)
print("# ============================================================")

IQR = Q3 - Q1

print("IQR\n",IQR)
print("# ============================================================")

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

numeric_stock = stock.select_dtypes(include=np.number)

def find_outliers(group):
    Q_1 = group.quantile(0.25)
    Q_3 = group.quantile(0.75)
    IQR_ = Q_3 - Q_1

    lower_out = Q_1 - 1.5 * IQR_
    upper_out = Q_3 + 1.5 * IQR_

    return ((group < lower_out) | (group > upper_out))

outliers = stock.groupby("symbol")[numeric_stock.columns].apply(find_outliers)
print("Outliers\n", outliers)
print("Outliers Number: ", outliers.sum())
print("# ============================================================")

Skewness = stock.skew(numeric_only= True)
print("Skewness\n", Skewness)
print("# ============================================================")

unique_symbols = stock['symbol'].unique()
unique_symbols_no = stock['symbol'].nunique()

print('Unique Symbols',unique_symbols)
print('Number of Unique Symbols',unique_symbols_no)
print("# ============================================================")

Correlations = stock.corr(numeric_only=True)
print('Correlations Between Numeric Values',Correlations)
print("# ============================================================")
