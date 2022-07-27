import streamlit as st
import yfinance as yf
import pandas as pd
import cufflinks as cf
import datetime
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots


st.set_page_config(page_title="Stock App", page_icon=":chart_with_upwards_trend:", layout="wide", initial_sidebar_state="collapsed")

# Title
st.markdown('''
# Stock Price Tracker
This application shows the stock price data for the 500 S&P companies
''')


# Side Navigation
st.sidebar.subheader('Input Parameters')
start_date = st.sidebar.date_input("Start Date", datetime.date(2021, 1, 1))
end_date = st.sidebar.date_input("End Date", datetime.date(2022, 6, 30))

# Get Ticker Symbols and Data
ticker_list = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/s-and-p-500-companies/master/data/constituents_symbols.txt')
tickerSymbol = st.sidebar.selectbox("Stock ticker", ticker_list)
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date)


st.sidebar.markdown("""
This application is built using Python and Streamlit by: 
[Aweda Oluwanifemi](https://www.linkedin.com/in/oluwanifemi-aweda-2b9206118/)
""")


st.title('Company Profile')
company_logo = '<img src=%s>' % tickerData.info['logo_url']
st.markdown(company_logo, unsafe_allow_html=True)
st.subheader(tickerData.info['longName']) 


col1, col2 = st.columns(2)
with col1:
    st.markdown('**Industry**: ' + tickerData.info['industry'])
    st.markdown('**Address**: ' + tickerData.info['address1'] + ', ' + tickerData.info['city'] + ', ' + tickerData.info['zip'] + ', '  +  tickerData.info['country'])
    st.markdown('**Number of Employees**: %s' % tickerData.info['fullTimeEmployees'])
with col2:
    st.markdown('**Sector**: ' + tickerData.info['sector'])
    st.markdown('**Phone**: ' + tickerData.info['phone'])
    st.markdown('**Website**: ' + tickerData.info['website'])

st.markdown('**Business Summary**')
st.info(tickerData.info['longBusinessSummary'])


fundInfo1 = {
    'Enterprise Value (USD)': tickerData.info['enterpriseValue'],
    'Enterprise To Revenue Ratio': tickerData.info['enterpriseToRevenue'],
    'Enterprise To Ebitda Ratio': tickerData.info['enterpriseToEbitda'],
    'Net Income (USD)': tickerData.info['netIncomeToCommon'],
    'Profit Margin Ratio': tickerData.info['profitMargins'],
    'Forward PE Ratio': tickerData.info['forwardPE'],
    'Payout Ratio': tickerData.info['payoutRatio'],
    "Current Ratio": tickerData.info['currentRatio'],
    "Quick Ratio": tickerData.info['quickRatio'],
    "Return on Asset": tickerData.info['returnOnAssets'],
    "Gross Profit Margin": tickerData.info['grossMargins'],
}

fundInfo2 = {
    "Operating Profit Margin": tickerData.info['operatingMargins'],
    "Debt to Equity": tickerData.info['debtToEquity'],
    "Return on Equity": tickerData.info['returnOnEquity'],
    'PEG Ratio': tickerData.info['pegRatio'],
    'Price to Book Ratio': tickerData.info['priceToBook'],
    'Forward EPS (USD)': tickerData.info['forwardEps'],
    'Beta ': tickerData.info['beta'],
    'Book Value (USD)': tickerData.info['bookValue'],
    'Dividend Rate (%)': tickerData.info['dividendRate'], 
    'Dividend Yield (%)': tickerData.info['dividendYield'],
    'Five year Avg Dividend Yield (%)': tickerData.info['fiveYearAvgDividendYield'],
    
}


st.subheader('Fundamental Information') 
col3, col4 = st.columns(2)

with col3:
    fundDF1 = pd.DataFrame.from_dict(fundInfo1, orient='index')
    fundDF1 = fundDF1.rename(columns={0: 'Value'})
    st.table(fundDF1)

with col4:
    fundDF2 = pd.DataFrame.from_dict(fundInfo2, orient='index')
    fundDF2 = fundDF2.rename(columns={0: 'Value'})
    st.table(fundDF2)


#  Bollinger bands
st.subheader('Bollinger Bands')
qf=cf.QuantFig(tickerDf,title='Market Trend',legend='top',name='GS',up_color='green', down_color='red')
qf.add_bollinger_bands(periods=20, boll_std=2, colors=['cyan','grey'], fill=True,)
qf.add_volume(name='Volume',up_color='green', down_color='red')
fig = qf.iplot(asFigure=True)
st.plotly_chart(fig, use_container_width=True)


marketInfo = {
    "Volume": tickerData.info['volume'],
    "Average Volume": tickerData.info['averageVolume'],
    "Market Cap": tickerData.info["marketCap"],
    "Float Shares": tickerData.info['floatShares'],
    "Regular Market Price (USD)": tickerData.info['regularMarketPrice'],
    'Bid Size': tickerData.info['bidSize'],
    'Ask Size': tickerData.info['askSize'],
    "Share Short": tickerData.info['sharesShort'],
    'Short Ratio': tickerData.info['shortRatio'],
    'Share Outstanding': tickerData.info['sharesOutstanding']
}

marketDF = pd.DataFrame(data=marketInfo, index=[0])
st.subheader('Stock Market Details')
st.table(marketDF)
