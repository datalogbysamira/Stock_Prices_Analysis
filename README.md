# Stock Prices Analysis

A practical data analysis project focused on **cleaning, exploring, visualizing, and analyzing historical stock market data** using Python. The project examines daily stock prices and trading volume across multiple companies to uncover price trends, relationships, distributions, and time-series patterns.

## Project Overview

The dataset contains daily stock market observations for multiple companies, including:

* **Symbol** — Stock ticker
* **Date** — Trading date
* **Open** — Opening price
* **High** — Highest price during the day
* **Low** — Lowest price during the day
* **Close** — Closing price
* **Volume** — Number of shares traded

The analysis follows a structured workflow from **data preprocessing to exploratory analysis, visualization, and time-series analysis**.

## Objectives

* Clean and prepare raw stock market data for analysis.
* Identify and handle missing values and duplicate records.
* Standardize data types and date formats.
* Calculate descriptive statistics and understand price distributions.
* Explore relationships between stock prices and trading volume.
* Visualize stock price movements and market patterns.
* Analyze trends using time-series techniques.
* Apply moving averages to smooth short-term price fluctuations.
* Decompose time-series data into trend, seasonal, and residual components.

## Analysis Workflow

### 1. Data Cleaning & Preprocessing

The raw dataset is inspected and prepared for analysis by:

* Checking data types and missing values.
* Handling missing observations where necessary.
* Identifying and removing duplicate records.
* Converting `date` to a proper datetime format.
* Ensuring numerical columns use appropriate numeric data types.
* Validating stock price and volume values.

### 2. Exploratory Data Analysis

EDA is used to understand the structure and behavior of the stock market data through:

* Mean, median, mode, and standard deviation.
* Price and volume distributions.
* Outlier detection using boxplots.
* Relationships between `open`, `high`, `low`, and `close` prices.
* Correlation analysis between numerical variables.
* Comparison of stock behavior across different symbols.

### 3. Data Visualization

Visualizations are created to make trends and relationships easier to interpret, including:

* Line charts for stock price movements.
* Histograms for numerical distributions.
* Boxplots for outlier detection.
* Scatter plots for relationships between variables.
* Bar charts for stock comparisons.
* Customized titles, labels, legends, and axes.

Plots are exported as image files for documentation and reporting.

### 4. Time-Series Analysis

Historical stock prices are analyzed as time-series data to identify longer-term patterns.

The analysis includes:

* Daily closing-price trends.
* Moving averages for smoothing price fluctuations.
* Comparison of actual prices with smoothed trends.
* Time-series decomposition into:

  * **Trend**
  * **Seasonality**
  * **Residuals**

## Project Structure

```text
Stock_Prices_Analysis/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── stock_prices_analysis.ipynb
│
├── scripts/
│   ├── level_1/
│   ├── level_2/
│   ├── level_3/
│   └── utils/
│
├── visuals/
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Tools & Technologies

* **Python** — Data analysis and scripting
* **Pandas** — Data cleaning, manipulation, and analysis
* **NumPy** — Numerical operations
* **Matplotlib** — Data visualization
* **Seaborn** — Statistical visualization
* **Statsmodels** — Time-series analysis and decomposition
* **Jupyter Notebook** — Interactive analysis
* **Git & GitHub** — Version control and project management

## Dataset Schema

| Column   | Type    | Description                          |
| -------- | ------- | ------------------------------------ |
| `symbol` | String  | Stock ticker symbol                  |
| `date`   | Date    | Trading date                         |
| `open`   | Float   | Opening stock price                  |
| `high`   | Float   | Highest price during the trading day |
| `low`    | Float   | Lowest price during the trading day  |
| `close`  | Float   | Closing stock price                  |
| `volume` | Integer | Number of shares traded              |

## Key Outcomes

This project demonstrates a complete **data analysis workflow**, from raw financial data to meaningful insights. It provides practical experience in data quality management, exploratory analysis, statistical summaries, visualization, and time-series techniques while working with real-world-style stock market data.

## Project Status

**In Progress** — Analysis and visualizations are being developed progressively as part of the Codveda Technologies internship.

---

## 👩‍💻 Author

**Samira Kiriti**

Data Analyst | Python | SQL | Power BI | ML

LinkedIn: (https://www.linkedin.com/in/samira-kriti/)
