import pandas as pd

def get_list_from_csv(CSVFileName):
    return pd.read_csv(CSVFileName).to_numpy().tolist()
