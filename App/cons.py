# import time
# import datetime
# import pandas as pd
# import plotly.express as px
# from dateutil import parser
#
# ticker = 'UAH=X'
# period1 = ()
# # period2 = input(parser.parse(("Please give start date in '%Y-%m-%d' format:\t")
# interval = '1d'  # 1d, 1m
# # date1 = datetime.date(period1).timetuple()))
# query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'
#
# df = pd.read_csv(query_string)
#
# fig = px.line(df, x='Date', y='Close', title='Apple Share Prices over time (2014)')
# fig.show()
# # df.to_csv('AAPL.csv')
