
# Stock Comparison App

## Overview
The Stock Comparison App allows users to analyze and compare historical data for three stocks using their ticker symbols and a selected date range. The app connects to the WRDS database for data retrieval and leverages Streamlit for an interactive web interface.

---

## Features
- Fetch historical stock data for three user-specified stocks.
- Calculate key metrics such as 50-day and 200-day moving averages and annualized volatility.
- Visualize stock prices with overlays of moving averages.
- Compare volatility across the selected stocks via a bar chart.

---

## Requirements
- Python 3.7 or higher.
- WRDS credentials for accessing the database.
- Libraries:
  - `wrds`
  - `pandas`
  - `numpy`
  - `streamlit`
  - `matplotlib`

---

## Installation

1. Clone or download the repository.
2. Install the required Python libraries using pip:

   ```bash
   pip install wrds pandas numpy streamlit matplotlib
   ```

3. Save your WRDS credentials for database access.

---

## How to Use

1. Save the script as `stock_comparison.py`.
2. Run the app using Streamlit:

   ```bash
   streamlit run stock_comparison.py
    In terminal input streamlit run "file path"
   ```

3. In the Streamlit interface:
   - Enter the ticker symbols for three stocks (e.g., AAPL, TSLA, AMZN).
   - Select a start and end date for the analysis.
4. View the summary metrics, visualizations, and volatility comparison.

---

## Outputs

1. **Summary Metrics**: Displays volatility for each selected stock.
2. **Visualization**:
   - Stock prices with 50-day and 200-day moving averages.
3. **Comparison Chart**: A bar chart showing the annualized volatility of the selected stocks.

---

## Troubleshooting
- Ensure your WRDS credentials are valid and configured correctly.
- If a ticker symbol is not found, verify its availability in the WRDS database.

---

## Author
Developed to provide a streamlined approach for financial analysis using WRDS and Streamlit.
