import pandas as pd

def get_csv_option_list(CSVFileName):
    return pd.read_csv(CSVFileName)
