import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

stock = pd.read_csv("data/cleaned/clean_stock.csv",parse_dates=["date"], index_col="date")

print(stock.head())


# ============================================================
# 1. Histograms: Distribution of Numerical Values
# ============================================================
stock.hist(bins = 30)
plt.title("The Distribution of Numerical Variables")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("outputs/Figures/Histograms.png", dpi = 300)
plt.show()

# ============================================================
# 2. BoxPlots: Ouliers of Numerical Values
# ============================================================
numeric_stock = stock.select_dtypes(include=np.number)
for column in numeric_stock.columns :
    plt.figure(figsize=(8,4))
    sns.boxplot(x= stock[column])
    plt.tight_layout()
    plt.title(f'Outliers of {column} variables')
    plt.xlabel(column)
    plt.savefig(f"outputs/Figures/{column}_boxplot.png", dpi = 300)
    plt.show()

# ============================================================
# 3. Difference Between Mean and Median and Std
# ============================================================

summary_statistic = pd.DataFrame({
    "Mean": stock[["open", "high", "low", "close"]].mean(),
    "Median": stock[["open", "high", "low", "close"]].median(),
    "STD": stock[['open','high','low','close']].std()
}).round(2)

# Create the clustered bar chart
ax = summary_statistic.plot(
    kind="bar",
    figsize=(10, 6)
)

# Add the numerical value above each bar
for container in ax.containers:
    ax.bar_label(container, fmt="%.2f", padding=3)

# Customize the chart
plt.title("Summary statistics comparision of Stock Prices")
plt.xlabel("Price Variable")
plt.ylabel("Price")
plt.xticks(rotation=0)
plt.legend(title="Statistic")
plt.tight_layout()
plt.savefig("outputs/Figures/summary_statistic.png", dpi = 300)

plt.show()

# ============================================================
# 4. Scatter Plot: Numerical Variables VS Companies
# ============================================================
plt.figure(figsize=(12, 8))
sns.scatterplot(data=stock, x = 'open', y = 'close')
plt.title("The Relationship between open Prices and Close Prices")
plt.savefig(f"outputs/Figures/open_close_Scatterplot.png", dpi = 300)
plt.show()

plt.figure(figsize=(12, 8))
sns.scatterplot(data=stock, x = 'open', y = 'high')
plt.tight_layout()
plt.title("The Relationship between open Prices and high Prices")
plt.savefig(f"outputs/Figures/open_high_Scatterplot.png", dpi = 300)
plt.show()
plt.figure(figsize=(12, 8))
sns.scatterplot(data=stock, x = 'open', y = 'low')
plt.tight_layout()
plt.title("The Relationship between open Prices and low Prices")
plt.savefig(f"outputs/Figures/open_low_Scatterplot.png", dpi = 300)
plt.show()
plt.figure(figsize=(12, 8))
sns.scatterplot(data=stock, x = 'open', y = 'volume')
plt.tight_layout()
plt.title("The Relationship between open Prices and the number of shares traded during the trading session")
plt.savefig(f"outputs/Figures/open_volume_Scatterplot.png", dpi = 300)
plt.show()

plt.figure(figsize=(12, 8))
sns.scatterplot(data=stock, x = 'close', y = 'high')
plt.tight_layout()
plt.title("The Relationship between close Prices and high Prices")
plt.savefig(f"outputs/Figures/close_high_Scatterplot.png", dpi = 300)
plt.show()
plt.figure(figsize=(12, 8))
sns.scatterplot(data=stock, x = 'close', y = 'low')
plt.tight_layout()
plt.title("The Relationship between close Prices and low Prices")
plt.savefig(f"outputs/Figures/close_low_Scatterplot.png", dpi = 300)
plt.show()
plt.figure(figsize=(12, 8))
sns.scatterplot(data=stock, x = 'close', y = 'volume')
plt.tight_layout()
plt.title("The Relationship between close Prices and the number of shares traded during the trading session")
plt.savefig(f"outputs/Figures/close_volume_Scatterplot.png", dpi = 300)
plt.show()

# ============================================================
# 5. Correlation: The linear Relationship between numerical values
# ============================================================
numeric_stock = stock.select_dtypes(include=np.number)
correlation = stock.corr(numeric_only=True)
print(correlation)
plt.figure(figsize=(8,4))

sns.heatmap(
    correlation,
    annot= True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)
plt.savefig("outputs/Figures/correlation.png", dpi = 300)
plt.show()
