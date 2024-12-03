
# Stock Comparison App Documentation

## Overview
This application allows users to compare three stocks based on their historical data and financial metrics using WRDS (Wharton Research Data Services) and Streamlit. Users can input stock ticker symbols and a date range to visualize and analyze stock prices, moving averages, and volatility.

---

## Features
- Input three stock ticker symbols and a date range.
- Fetch historical stock data from WRDS.
- Calculate financial metrics such as volatility and moving averages.
- Visualize stock prices with 50-day and 200-day moving averages.
- Compare annualized volatility across the selected stocks.

---

## Code Structure

### Import Libraries
The script imports the following libraries:
- **wrds**: For connecting to WRDS database.
- **pandas**: For data manipulation.
- **numpy**: For numerical calculations.
- **streamlit**: For building the web interface.
- **matplotlib.pyplot**: For visualizing stock data.

### Streamlit User Interface
- Inputs: 
  - Ticker symbols for three stocks.
  - Start and end dates for fetching historical data.
- Outputs:
  - Summary metrics for each stock.
  - Plots of stock prices and moving averages.
  - Bar chart comparing annualized volatility.

### WRDS Database Interaction
- Fetch stock `permno` using ticker symbols from `crsp.stocknames`.
- Retrieve historical stock data (price, returns, and volume) from `crsp.dsf`.
- Calculate metrics: Rolling moving averages (50-day and 200-day) and annualized volatility.

### Visualization
- **Price Plots**: Display stock prices and moving averages using Matplotlib.
- **Volatility Bar Chart**: Compare annualized volatility for the selected stocks using Streamlit's bar chart feature.

### Error Handling
- Ensures user-friendly error messages if ticker symbols are invalid or data is unavailable.

### Connection Management
- Securely connects to WRDS using credentials.
- Ensures connection is closed after data retrieval.

---

## Functions

### `fetch_stock_data(ticker, start_date, end_date)`
Fetches stock data from WRDS for a given ticker symbol and date range.
- **Parameters**:
  - `ticker`: Stock ticker symbol.
  - `start_date`: Start date for data retrieval.
  - `end_date`: End date for data retrieval.
- **Returns**: Pandas DataFrame containing stock data (price, returns, volume).

### `calculate_metrics(data)`
Calculates financial metrics for the stock data.
- **Parameters**:
  - `data`: Pandas DataFrame with stock data.
- **Returns**: DataFrame with additional columns for returns, moving averages, and volatility.

### `plot_data(data, ticker, metric="prc", title="Price")`
Generates a plot of stock prices and moving averages.
- **Parameters**:
  - `data`: Stock data DataFrame.
  - `ticker`: Stock ticker symbol.
  - `metric`: Data column to plot (default: `"prc"`).
  - `title`: Plot title.

---

## Requirements
- WRDS credentials for database access.
- Python libraries: `wrds`, `pandas`, `numpy`, `streamlit`, `matplotlib`.
- Streamlit installed for running the web application.

---

## How to Run
1. Install required libraries: `pip install wrds pandas numpy streamlit matplotlib`.
2. Save the script as `stock_comparison.py`.
3. Run the app: `streamlit run stock_comparison.py`.
4. Enter ticker symbols and date range in the Streamlit interface.

---

## Output
- **Summary Metrics**: Volatility and moving averages for each stock.
- **Plots**: Stock prices and moving averages over time.
- **Bar Chart**: Comparison of annualized volatility.

---

## Additional Notes
- Ensure WRDS credentials are correctly configured before running the app.
- Cached data fetches optimize performance using `@st.cache_data`.
- Data availability depends on WRDS database records.

---

## Author
Generated and documented for enhanced understanding and usability.
