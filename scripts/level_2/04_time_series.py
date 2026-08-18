import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

stock = pd.read_csv("data/cleaned/clean_stock.csv", parse_dates=["date"], index_col="date")

