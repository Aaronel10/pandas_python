import pandas as pd
from datetime import datetime

d_parser = lambda x: datetime.strptime(x, '%Y-%m-%d %I-%p')
df = pd.read_csv('ETH_1h.csv', parse_dates=['Date'], date_parser=d_parser)
# print(df.loc[0, 'Date'])
# print(df['Date'])
# pd.datetime is deprecated use datetime module instead
# say you want to run a function on an entire series
# print(df['Date'].dt.day_name())
df['DayOfWeek'] = df['Date'].dt.day_name()
# print(df['Date'].max())
# get time delta by subtracting 2 dates
# print(df['Date'].max() - df['Date'].min())
# create a filter
#filt = (df['Date'] >= '2019') & (df['Date'] < '2020')
filt = (df['Date'] >= pd.to_datetime('2019-01-01')) & (df['Date'] < pd.to_datetime('2020-01-01'))
#print(df.loc[filt])
df.set_index('Date', inplace=True)
print(df.loc['2020-01-01']['High'].max())

# if you want to change a data set from hourly to daily or etc you do something called resampling
highs = df['High'].resample('D').max()
# print(highs['2020-01-01'])
df = df.resample('W').agg({'Close': 'mean', 'High': 'max', 'Low':'min', 'Volume': 'sum'})
print(df)