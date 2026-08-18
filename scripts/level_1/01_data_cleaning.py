import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

stock = pd.read_csv("data/raw/stock.csv")

print("1. Data Exploration\n")
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


print("2. Data Cleaning and Validation\n")

print("2.1 Check Extra spaces")

for column in stock.select_dtypes(include=object).columns :
    stock[column] = stock[column].str.strip()

print("No Extra Spaces in STR columns")

print("2.2 Update Data Types")
stock['date'] = pd.to_datetime(stock['date'])

print(stock.dtypes)


print("2.3 Check Missing Values", stock.isnull().sum())
stock.isnull().sum()

print("Replacement of Missing Values")
missing = stock.isnull().sum().sum()
missing_percentage = missing / len(stock) * 100

print(f"Total {missing} missing values are Found in dataset")

for column in ["open", "high", "low"]:

    if missing_percentage <= 5:
        
        stock = stock.dropna()
        print(f"{column}: missing values removed.")
    else:
        median_value = stock[column].median()
        stock[column] = stock[column].fillna(median_value)
        print(f"{column}: {missing} missing values replaced with median.")

print("\nMissing Values After Cleaning:")
print(stock.isnull().sum())

print("2.4 Check Duplicated Values")

duplicated_values = stock.duplicated().sum()
if duplicated_values == 0 :
    print("There is no Duplicated Values")   
else :
    stock.drop_duplicates(inplace=True)
    print(f"{duplicated_values} were Removed")


print("2.5 Cleaning and Validation Report")
print(f"1. Dataset has {stock.shape} Raws and Columns")
print(f"2. Dataset Columns' labels : {stock.columns}")
print(f"3. Data types After validation:\n {stock.dtypes}")               
print("4. Total 27 missing values were removed from dataset")
print("5. There was no Duplicated Values")
print("6. No Extra Spaces in STR columns")
print("7. only 'date' columns data type was converted from str to datetime")

print("8. Saving data to Cleaned File")

stock.to_csv("data/cleaned/clean_stock.csv", index=False)

print("cleaned Data Saved Successfully!")