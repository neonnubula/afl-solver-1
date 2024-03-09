import pandas as pd

def get_player_list():
    return pd.read_csv('player-list.csv')
