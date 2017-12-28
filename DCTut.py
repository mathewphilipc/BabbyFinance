# Exploring the use of Pandas to analyze time series data

# Note that the Yahoo API endpoint has recently changed
# More info @ https://github.com/pydata/pandas-datareader/issues/315

import pandas_datareader as pdr
import datetime
#print("hello world")
aapl = pdr.get_data_yahoo('AAPL',
	start=datetime.datetime(2006, 10, 1),
	end=datetime.datetime(2012, 1, 1))

# Alternatively:
import quandl 
#aapl = quandl.get("WIKI/AAPL", start_date="2006-10-01", end_date="2012-01-01")

# Show first and last rows of 'aapl'
print("\n\n\n*****First few rows of aapl*****\n")
print(aapl.head())
print("\n\n\n*****Last few rows of aapl*****\n")
print(aapl.tail())
print("\n\n\n*****Summary of aapl*****\n")
print(aapl.describe())

# This data contains the four columns with the opening and closing price per
# day and the extreme high and low price movements for the Apple stock each
# day. You also get two extra columns: Volume and Adj Close.

# Volume = number of shares traded during a single day
# Adj Close = ???

import pandas as pd
aapl.to_csv('data/aapl_oh1c.csv')
df = pd.read_csv('data/aapl_oh1c.csv', header=0, index_col='Date', parse_dates=True)

print("\n\n\n*****Index of aapl (roughly speaking, the row labels)*****\n")
print(aapl.index)
print("\n\n\n*****Columns of aapl (i.e., the column labels)*****\n")
print(aapl.columns)

# We 'subset' the Close column by only selecting the last 10 observations of
# the DataFrame

print("\n\n\n*****Last ten Close values*****\n")
ts = aapl['Close'][-10:]
print(ts)
#print(type(ts))