import streamlit as st
import yfinance as yf
import datetime as dt


st.title('Simple stock price analysis app')
st.write(
'''
shown are the stock closing price and volume of google    
'''
)
tickerSymbol='GOOGL'
tickerData=yf.Ticker(tickerSymbol)
tickerDf=tickerData.history(period='1d',start='2010-5-31',end=dt.datetime.now())

tickerSymbol1='AMZN'
tickerData1=yf.Ticker(tickerSymbol)
tickerDf1=tickerData.history(period='1d',start='2010-5-31',end=dt.datetime.now())

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

st.write(
'''
shown are the stock closing price and volume of Amazon    
'''
)

st.line_chart(tickerDf1.Close)
st.line_chart(tickerDf1.Volume)

text="""
import streamlit as st
import yfinance as yf
import datetime as dt

st.title('Simple stock price analysis app')
st.write(
'''
shown are the stock closing price and volume of google    
'''
)
tickerSymbol='GOOGL'
tickerData=yf.Ticker(tickerSymbol)
tickerDf=tickerData.history(period='1d',start='2010-5-31',end=dt.datetime.now())

tickerSymbol1='AMZN'
tickerData1=yf.Ticker(tickerSymbol)
tickerDf1=tickerData.history(period='1d',start='2010-5-31',end=dt.datetime.now())

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

st.write(
'''
shown are the stock closing price and volume of Amazon    
'''
)

st.line_chart(tickerDf1.Close)
st.line_chart(tickerDf1.Volume)

"""

st.text('THE SOURCE CODE')
st.code(text)

st.balloons()
#st.audio('alert.wav')
#st.map()

#a=st.text_input('Your name:')
#st.text('Your name is ' + a)

# st.file_uploader('pdf')


st.write('By')
st.image('bala.jpg')