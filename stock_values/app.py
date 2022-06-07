import streamlit as st

def intro():
    """
    Just a simple start site with some information and no function
    :return:None
    """
    import streamlit as st
    from PIL import Image

    # Load main image
    image = Image.open('drawing.png')
    st.image(image, width=128)

    # Welcome/Willkommen/Witaj
    st.write("# Welcome to BandBioinfo site! 👋")
    st.sidebar.success("Select section to work.")

    st.markdown(
        """
        This is pilot app to present some possibilities of this framework.
        
        First functionality is to present stock closing price and volume of any stock selected by YOU! 
        
        **👈 Select a section from the dropdown on the left** to see some what can you do!

        """
    )

def prices_intervals():
    """
    Funtion to collect data about proces of selected stock and interval of prices by choice
    :return:None
    """
    import yfinance as yf
    import streamlit as st

    # Some info
    st.write("""
    # Simple Stock Price App
    Shown are the stock **closing price** and ***volume*** !
    """)

    # place to insert stock symbol
    ticker = st.text_input(label='Please insert market stock ticker',value='MSFT')

    #load data about stock
    tickerData = yf.Ticker(ticker)
    # choices
    displayIntervals = {'1 day': '1d', '5 days': '5d', '1 month': '1mo', '3 months': '3mo', '6 months': '6mo',
                        '1 year': '1y',
                        '2 years': '2y', '5 years': '5y', '10 years': '10y', 'all': 'max'}

    # check if selected symbol exist
    if tickerData.info['regularMarketPrice'] is not None:
        # what is the name of company
        st.subheader(f"You are looking at data about {tickerData.info['longName']}")

        # pick interval
        period = st.select_slider('Pick an interval', displayIntervals.keys())

        # get data to present
        tickerDf = tickerData.history(period=displayIntervals[period])

        # show data
        st.write("""
        ## Closing Price
        """)
        st.line_chart(tickerDf.Close)
        st.write("""
        ## Volume Price
        """)
        st.line_chart(tickerDf.Volume)

    elif ticker is not None or ticker != '':
        st.subheader('Sorry object with this name do not exist try something else')
    else:
        pass

def select_date():

    import yfinance as yf
    import streamlit as st

    st.write("""
    # Simple Stock Price App
    Shown are the stock **closing price** and ***volume***!
    """)
    ticker = st.text_input(label='Please insert market stock ticker',value='MSFT')
    tickerData = yf.Ticker(ticker)


    if tickerData.info['regularMarketPrice'] is not None:

        begin = st.date_input(label="From")
        end = st.date_input(label="To")
        if begin > end:
            st.write("Sorry, beginning date if before end day, please re-select dates")
        else:
            tickerDf = tickerData.history(start=begin, end=end)

            st.write("""
            ## Closing Price
            """)
            st.line_chart(tickerDf.Close)
            st.write("""
            ## Volume Price
            """)
            st.line_chart(tickerDf.Volume)

    elif ticker is not None or ticker != '':
        st.subheader('Sorry object with this name do not exist try something else')
    else:
        pass