import streamlit as st
import yfinance as yf
import pandas as pd
import cufflinks as cf
import datetime
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots


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

\nTutorials from [Chanin Nantasenamat](https://medium.com/@chanin.nantasenamat) (aka [Data Professor](http://youtube.com/dataprofessor))
""")



company_logo = '<img src=%s>' % tickerData.info['logo_url']
st.markdown(company_logo, unsafe_allow_html=True)

company_name = tickerData.info['longName']
st.header('**%s**' % company_name)

company_employees = tickerData.info['fullTimeEmployees']
st.header('Fulltime employees: %s' % company_employees)

company_summary = tickerData.info['longBusinessSummary']
st.info(company_summary)


#  Bollinger bands
st.header('**Bollinger Bands**')
qf=cf.QuantFig(tickerDf,title='Market Chart',legend='top',name='GS',up_color='green', down_color='red')
qf.add_bollinger_bands(periods=20, boll_std=2, colors=['cyan','grey'], fill=True,)
qf.add_volume(name='Volume',up_color='green', down_color='red')
fig = qf.iplot(asFigure=True)
st.plotly_chart(fig)


# # Candlestick plot
# prices = tickerDf['Close']
# volumes = tickerDf['Volume']

# lower = prices.min()
# upper = prices.max()
# prices_ax = np.linspace(lower,upper, num=20)

# vol_ax = np.zeros(20)


# # Accumulate volume for each price points (Create bins)
# for i in range(0, len(volumes)):
#     if(prices[i] >= prices_ax[0] and prices[i] < prices_ax[1]):
#         vol_ax[0] += volumes[i]   
        
#     elif(prices[i] >= prices_ax[1] and prices[i] < prices_ax[2]):
#         vol_ax[1] += volumes[i]  
        
#     elif(prices[i] >= prices_ax[2] and prices[i] < prices_ax[3]):
#         vol_ax[2] += volumes[i] 
        
#     elif(prices[i] >= prices_ax[3] and prices[i] < prices_ax[4]):
#         vol_ax[3] += volumes[i]  
        
#     elif(prices[i] >= prices_ax[4] and prices[i] < prices_ax[5]):
#         vol_ax[4] += volumes[i]  
        
#     elif(prices[i] >= prices_ax[5] and prices[i] < prices_ax[6]):
#         vol_ax[5] += volumes[i] 
        
#     elif(prices[i] >= prices_ax[6] and prices[i] < prices_ax[7]):
#         vol_ax[6] += volumes[i] 

#     elif(prices[i] >= prices_ax[7] and prices[i] < prices_ax[8]):
#         vol_ax[7] += volumes[i] 

#     elif(prices[i] >= prices_ax[8] and prices[i] < prices_ax[9]):
#         vol_ax[8] += volumes[i] 

#     elif(prices[i] >= prices_ax[9] and prices[i] < prices_ax[10]):
#         vol_ax[9] += volumes[i] 

#     elif(prices[i] >= prices_ax[10] and prices[i] < prices_ax[11]):
#         vol_ax[10] += volumes[i] 

#     elif(prices[i] >= prices_ax[11] and prices[i] < prices_ax[12]):
#         vol_ax[11] += volumes[i] 

#     elif(prices[i] >= prices_ax[12] and prices[i] < prices_ax[13]):
#         vol_ax[12] += volumes[i] 

#     elif(prices[i] >= prices_ax[13] and prices[i] < prices_ax[14]):
#         vol_ax[13] += volumes[i] 

#     elif(prices[i] >= prices_ax[14] and prices[i] < prices_ax[15]):
#         vol_ax[14] += volumes[i]   
        
#     elif(prices[i] >= prices_ax[15] and prices[i] < prices_ax[16]):
#         vol_ax[15] += volumes[i] 
        
#     elif(prices[i] >= prices_ax[16] and prices[i] < prices_ax[17]):
#         vol_ax[16] += volumes[i]         
        
#     elif(prices[i] >= prices_ax[17] and prices[i] < prices_ax[18]):
#         vol_ax[17] += volumes[i]         
        
#     elif(prices[i] >= prices_ax[18] and prices[i] < prices_ax[19]):
#         vol_ax[18] += volumes[i] 
    
#     else:
#         vol_ax[19] += volumes[i]


# # make plots
# fig = make_subplots(
#         rows=1, cols=2,
#         column_widths=[0.2, 0.8],
#         specs=[[{}, {}]],
#         horizontal_spacing = 0.01
#     )

# fig.add_trace(
#         go.Bar(
#                 x = vol_ax, 
#                 y= prices_ax,
#                 text = np.around(prices_ax,2),
#                 textposition='auto',
#                 orientation = 'h'
#             ),
#         row = 1, col =1
#     )

# dateStr = tickerDf.index.strftime("%d-%m-%Y %H:%M:%S")

# fig.add_trace(
#     go.Candlestick(x=dateStr,
#                 open=tickerDf['Open'],
#                 high=tickerDf['High'],
#                 low=tickerDf['Low'],
#                 close=tickerDf['Close'],
#                 yaxis= "y2"  
#             ),
#         row = 1, col=2
#     )
        
# fig.update_layout(
#     title_text='Market Profile Chart (US S&P 500)', # title of plot
#     bargap=0.01, # gap between bars of adjacent location coordinates,
#     showlegend=False,
    
#     xaxis = dict(
#             showticklabels = False
#         ),
#     yaxis = dict(
#             showticklabels = False
#         ),
    
#     yaxis2 = dict(
#             title = "Price (USD)",
#             side="right"
#         )
# )

# fig.update_yaxes(nticks=20)
# fig.update_yaxes(side="right")
# fig.update_layout(height=800)

# config={
#         'modeBarButtonsToAdd': ['drawline']
#     }

# st.plotly_chart(fig, use_container_width=True, config=config)