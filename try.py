import pandas as pd
import yfinance as yf
import datetime
import plotly
import plotly.graph_objects as go
import autots

from datetime import date, timedelta
today = date.today()

first_date = today.strftime("%Y-%m-%d")
end_date = first_date
second_date = date.today() - timedelta(days=730)
second_date = second_date.strftime("%Y-%m-%d")
start_date = second_date

crypto_data = yf.download(tickers='ETH-USD', period = '22h', interval = '15m')
crypto_data["Date"] = crypto_data.index
crypto_data = crypto_data[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
crypto_data.reset_index(drop=True, inplace=True)
print(crypto_data.head())
print(crypto_data.shape)

figure = go.Figure(data=[go.Candlestick(x=crypto_data["Date"],
                                        open=crypto_data["Open"],
                                        high=crypto_data["High"],
                                        low=crypto_data["Low"],
                                        close=crypto_data["Close"])])
figure.update_layout(title = "Cryptocurrency Price",
                     xaxis_rangeslider_visible=True)
figure.show()

# data = yf.download(tickers='BTC-USD', period = '22h', interval = '15m')
# print(data)
