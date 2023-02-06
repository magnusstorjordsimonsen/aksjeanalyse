#Last ned CSV-fil fra https://live.euronext.com/nb/markets/oslo/equities/list

import os
import pandas as pd

CURR_DIR = os.getcwd() 
   
def get_df(csv_file_name_str):
    equities_df=pd.read_csv(CURR_DIR+csv_file_name_str, sep=';', skiprows=[1,2,3])
    print("Laster inn all data fra ",CURR_DIR + csv_file_name_str)
    return equities_df

def get_names_symbols_df(csv_file_name_str):
    equities_name_symbol_df=pd.read_csv(CURR_DIR+csv_file_name_str, sep=';', usecols = ['Name','Symbol'], skiprows=[1,2,3])
    print("Laster inn navn og symboler fra ",CURR_DIR + csv_file_name_str)
    return equities_name_symbol_df

def make_name_symbol_csv_from_oslo_bors_csv(input_csv_file_name, output_csv_file_name):
    name_symbol_df = get_names_symbols_df(input_csv_file_name)
    name_symbol_df.to_csv(output_csv_file_name, encoding='utf-8', sep=";")
    print(output_csv_file_name, "er nå opprettet fra", input_csv_file_name )


