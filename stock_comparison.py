# Import necessary libraries
import wrds
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

# Connect to WRDS (You'll need your WRDS credentials)
db = wrds.Connection()

# Streamlit app title
st.title("Stock Comparison App")
st.write("Select three stocks to compare based on their historical data and financial metrics.")

# User input for selecting stocks
stock1 = st.text_input("Enter the ticker symbol for Stock 1:", value="AAPL")
stock2 = st.text_input("Enter the ticker symbol for Stock 2:", value="TSLA")
stock3 = st.text_input("Enter the ticker symbol for Stock 3:", value="AMZN")
start_date = st.date_input("Start Date", pd.to_datetime("2022-01-01"))
end_date = st.date_input("End Date", pd.to_datetime("2023-01-01"))

# Function to fetch stock data
@st.cache_data
def fetch_stock_data(ticker, start_date, end_date):
    try:
        # Map ticker to permno
        permno_query = f"""
        SELECT permno
        FROM crsp.stocknames
        WHERE ticker = '{ticker}'
        ORDER BY namedt DESC
        LIMIT 1
        """
        permno_df = db.raw_sql(permno_query)
        if permno_df.empty:
            st.error(f"Ticker '{ticker}' not found in WRDS.")
            return None
        
        permno = permno_df['permno'].iloc[0]

        # Fetch stock data using permno
        query = f"""
        SELECT date, prc, ret, vol
        FROM crsp.dsf
        WHERE permno = {permno}
        AND date BETWEEN '{start_date}' AND '{end_date}'
        """
        data = db.raw_sql(query)
        data['date'] = pd.to_datetime(data['date'])
        data = data.set_index('date')
        return data

    except Exception as e:
        st.error(f"Error fetching data for ticker '{ticker}': {e}")
        return None

# Fetch data for the selected stocks
data1 = fetch_stock_data(stock1, start_date, end_date)
data2 = fetch_stock_data(stock2, start_date, end_date)
data3 = fetch_stock_data(stock3, start_date, end_date)

# Check if data was successfully fetched
if data1 is None or data2 is None or data3 is None:
    st.stop()

# Calculate metrics for each stock
def calculate_metrics(data):
    data['returns'] = data['ret']
    data['50_MA'] = data['prc'].rolling(window=50).mean()
    data['200_MA'] = data['prc'].rolling(window=200).mean()
    data['volatility'] = data['returns'].std() * np.sqrt(252)  # Annualized volatility
    return data

data1 = calculate_metrics(data1)
data2 = calculate_metrics(data2)
data3 = calculate_metrics(data3)

# Display summary metrics for each stock
st.write(f"### Summary Metrics for {stock1}")
st.write(f"Volatility: {data1['volatility'].iloc[-1]:.4f}")
st.write(f"### Summary Metrics for {stock2}")
st.write(f"Volatility: {data2['volatility'].iloc[-1]:.4f}")
st.write(f"### Summary Metrics for {stock3}")
st.write(f"Volatility: {data3['volatility'].iloc[-1]:.4f}")

# Visualization function
def plot_data(data, ticker, metric="prc", title="Price"):
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data[metric], label=f"{ticker} {title}")
    plt.plot(data.index, data['50_MA'], label="50-Day MA", linestyle="--")
    plt.plot(data.index, data['200_MA'], label="200-Day MA", linestyle="--")
    plt.title(f"{ticker} {title} and Moving Averages")
    plt.legend()
    st.pyplot(plt)

# Display plots for each stock
st.write("### Stock Prices and Moving Averages")
plot_data(data1, stock1)
plot_data(data2, stock2)
plot_data(data3, stock3)

# Risk analysis bar chart
st.write("### Volatility Comparison")
vol_df = pd.DataFrame({
    "Stock": [stock1, stock2, stock3],
    "Volatility": [data1['volatility'].iloc[-1], data2['volatility'].iloc[-1], data3['volatility'].iloc[-1]]
})
st.bar_chart(vol_df.set_index("Stock"))

# Close the WRDS connection
db.close()

if __name__ == "__main__":
    import os
    # Automatically start the Streamlit app
    os.system("streamlit run stock_comparison.py")

