import streamlit as st
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
import cufflinks as cf
import datetime
import numpy as np
import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go

# App title
st.markdown('''
# Stock Forecast and Price App
Shown are the stock price data for query companies, and the analysis graphs.

Babcock University Computer Science Department
''')
st.write('---')

# Sidebar
st.sidebar.subheader('Query parameters')
start_date = st.sidebar.date_input("Start date", datetime.date(2019, 1, 1))
end_date = st.sidebar.date_input("End date", datetime.date(2021, 2, 28))

# Retrieving tickers data
ticker_list = pd.read_csv('constituents_symbols.txt')
tickerSymbol = st.sidebar.selectbox('Stock ticker', ticker_list) # Select ticker symbol
tickerData = yf.Ticker(tickerSymbol) # Get ticker data
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date) #get the historical prices for this ticker

new_data = tickerDf

exp1 = new_data['Close'].ewm(span=12, adjust=False).mean()
exp2 = new_data['Close'].ewm(span=26, adjust=False).mean()
new_data['MACD'] = exp1 - exp2
new_data['Signal line'] = new_data['MACD'].ewm(span=9, adjust=False).mean()
# new_data.reset_index(level=0, inplace=True) 
new_data['Date'] = new_data.index

# fig, ax = plt.subplots()
# new_data[['MACD', 'Signal line']].plot(ax=ax)
# new_data['Close'].plot(ax=ax, alpha=0.25, secondary_y=True)

# Ticker information
string_logo = '<img src=%s>' % tickerData.info['logo_url']
st.markdown(string_logo, unsafe_allow_html=True)

string_name = tickerData.info['longName']
st.header('**%s**' % string_name)

string_summary = tickerData.info['longBusinessSummary']
st.info(string_summary)

# Ticker data
st.header('**Ticker data**')
st.write(tickerDf)

# Bollinger bands
st.header('**Bollinger Bands**')
qf=cf.QuantFig(tickerDf,title='First Quant Figure',legend='top',name='GS')
qf.add_bollinger_bands()
fig = qf.iplot(asFigure=True)
st.plotly_chart(fig)

st.header('**MACD**')
fig, ax = plt.subplots()
new_data[['MACD', 'Signal line']].plot(ax=ax)
new_data['Close'].plot(ax=ax, alpha=0.25, secondary_y=True)
st.pyplot(fig)

st.header('**Points**')
fig, ax = plt.subplots(2, 2)
new_data['Open'].plot(ax=ax[0, 0], title="Open")
new_data['High'].plot(ax=ax[0, 1], title="High")
new_data['Low'].plot(ax=ax[1, 0], title="Low")
new_data['Close'].plot(ax=ax[1, 1], title="Close")
plt.tight_layout()
st.pyplot(fig)


st.header('**Forecasting**')
n_days = st.slider('Days of prediction:', 1, 30)
period = n_days

# Predict forecast with Prophet.
df_train = new_data[['Date','Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# Show and plot forecast
st.subheader('Forecast data')
st.write(forecast.tail())
    
st.write(f'Forecast plot for {n_days} days')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write("Forecast components")
fig2 = m.plot_components(forecast)
st.write(fig2)
####
#st.write('---')
#st.write(tickerData.info)

st.markdown('''
**Credits**
- [Chanin Nantasenamat](https://medium.com/@chanin.nantasenamat)
- [Aweda Oluwanifemi](https://twitter.com/adenifesimi1)
- Built in `Python` using `streamlit`,`yfinance`, `cufflinks`, `pandas` and `datetime`
''')
