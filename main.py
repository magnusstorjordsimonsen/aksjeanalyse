from datetime import datetime, timedelta
import equities_oslo_bors_csv_to_dataframe
import download_stock_data

def run():
  
    equities_oslo_bors_csv_to_dataframe.make_name_symbol_csv_from_oslo_bors_csv("\Euronext_Equities_2023-02-06.csv", "all_stocks_oslo_bors.csv")
    equities_oslo_bors_csv_to_dataframe.make_name_symbol_csv_from_oslo_bors_csv(r"\Euronext_Equities_2023-02-06.csv", r"technology.csv")

    eq_names_symbols_df = equities_oslo_bors_csv_to_dataframe.get_names_symbols_df(r"\technology.csv")

    print(eq_names_symbols_df)





    #stock_df = download_stock_data.get_stock_df_from_yf("YAR")
    #print(stock_df)

    from_date = datetime.today() - timedelta(days=30*12*5) 
    to_date = datetime.today()

    av_interval_sma1 = 50  # Simple Moving Average interall
    av_interval_sma2 = 20  # Simple Moving Average interall
    rsi_interval = 14   # Relative Strength Index
    rsi_ema_bool = True # True: Use exponential moving average in RSI. False: Use simple moving average  in RSI
    av_interval_std = rsi_interval # Intervall for rolling standard deviation
    bollinger_factor = 2     # Number of std between sma and upper/lower bollinger band
    date = "Date"
    close = "Close"
    volume = "Volume"

    
if __name__ == "__main__":
    run()
