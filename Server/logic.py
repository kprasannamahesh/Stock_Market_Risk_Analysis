import pandas as pd
import yfinance as yf

def download_stock_data(ticker, start_date, end_date, csv_filename):
    # Download historical stock data
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    
    # Save the data to a CSV file
    stock_data.to_csv(csv_filename)

    print(f"Stock data downloaded and saved to {csv_filename}")

# Example usage:
ticker = ""  # Ticker symbol of the stock (e.g., "AAPL" for Apple Inc.)
start_date = ""  # Start date of the data
end_date = ""  # End date of the data
csv_filename = "stock_data.csv"  # Name of the CSV file to save the data

# download_stock_data(ticker, start_date, end_date, csv_filename)

def calculate_mean_return(csv_filename):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_filename)

    # Calculate the daily returns
    df['Daily Return'] = df['Adj Close'].pct_change()*100
    print(df['Daily Return'])
    # Drop rows with NaN values (first row will have NaN since it doesn't have a previous day)
    df.dropna(inplace=True)

    # Calculate the mean return
    mean_return = df['Daily Return'].mean()

    return mean_return

# Example usage:
csv_filename = "stock_data.csv"  # Replace with the actual filename
mean_return = calculate_mean_return(csv_filename)
print("Mean return:", mean_return)
