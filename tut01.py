import yfinance as yf
import pandas as pd
import streamlit as st


st.write("""
## Simple Stock Price App
Shown are the stock closing price and volume of Google!
""")

# Define the ticker symbol
tickerSymbol = 'MSFT'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2025-5-31')

st.line_chart(tickerDf.Close)   
st.line_chart(tickerDf.Volume)




# Stop the Streamlit app
st.stop()