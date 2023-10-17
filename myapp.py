import yfinance as yf
import streamlit as st
import pandas as pd

#Header
st.write("""
# Simple Stock Price App 
        

Show are the stock closing price and volume of Google!



"""
)

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75

#define ticker symbol
tickerSymbol = "GOOGL"

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2020-12-25', end='2023-10-15')
#Open High      Low Close   Volume      Dividends       Stock Splits


st.write("""
### Closing price
"""
)
st.line_chart(tickerDf.Close)

st.write("""
### Volume
"""
)
st.line_chart(tickerDf.Volume)