

import yfinance as yf
import pandas as pd

def get_stock_df_from_yf(symbol, start=None, end=None):
    df = yf.download(symbol+".OL", progress=True , period="max", interval="1d", start=start, end = end)
    return df





