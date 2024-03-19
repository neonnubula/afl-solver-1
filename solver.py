import pandas as pd

def solver(input_id, input_di, input_gls, input_loc, input_opp, input_ven, input_ssns):
  # Read the CSV data into a DataFrame
  df = pd.read_csv('real-data.csv')
  
  gamesHit = { # each diciontary entry counts the amount of games that stat correlated with the user input
    'di_under' : df.loc[(df["season"] >= input_ssns) & (df["playerid"] == input_id) & (df["disposals"] < input_di), "disposals"].count(),
    'di_over' : df.loc[(df["season"] >= input_ssns) & (df["playerid"] == input_id) & (df["disposals"] > input_di), "disposals"].count(),
    'di_under_loc' : df.loc[(df["location"] == input_loc) &(df["playerid"] == input_id) &(df["season"] >= input_ssns) &(df["disposals"] < input_di),"disposals"].count(),
    'di_over_loc' : df.loc[(df["location"] == input_loc) &(df["playerid"] == input_id) &(df["season"] >= input_ssns) &(df["disposals"] > input_di),"disposals"].count(),
    'di_under_opp' : df.loc[(df["opposition"] == input_opp) &(df["playerid"] == input_id) &(df["season"] >= input_ssns) &(df["disposals"] < input_di),"disposals"].count(),
    'di_over_opp' : df.loc[(df["opposition"] == input_opp) & (df["playerid"] == input_id) & (df["season"] >= input_ssns) & (df["disposals"] > input_di), "disposals"].count(),
    'di_under_ven' : df.loc[(df["venue"] == input_ven) & (df["playerid"] == input_id) & (df["season"] >= input_ssns) & (df["disposals"] < input_di), "disposals"].count(),
    'di_over_ven' : df.loc[(df["venue"] == input_ven) & (df["playerid"] == input_id) & (df["season"] >= input_ssns) & (df["disposals"] > input_di), "disposals"].count(),
    'di_under_2023' : df.loc[(df["season"] == 2023) & (df["playerid"] == input_id) & (df["disposals"] < input_di), "disposals"].count(),
    'di_over_2023' : df.loc[(df["season"] == 2023) & (df["playerid"] == input_id) & (df["disposals"] > input_di), "disposals"].count(),
    'gls_under' : df.loc[(df["season"] >= input_ssns) & (df["playerid"] == input_id) & (df["goals"] < input_gls), "goals"].count(),
    'gls_over' : df.loc[(df["season"] >= input_ssns) & (df["playerid"] == input_id) & (df["goals"] > input_gls), "goals"].count(),
    'gls_under_loc' : df.loc[(df["location"] == input_loc) & (df["season"] >= input_ssns) & (df["playerid"] == input_id) & (df["goals"] < input_gls), "goals"].count(),
    'gls_over_loc' : df.loc[(df["location"] == input_loc) & (df["season"] >= input_ssns) & (df["playerid"] == input_id) & (df["goals"] > input_gls), "goals"].count(),
    'gls_under_opp' : df.loc[(df["opposition"] == input_opp) & (df["season"] >= input_ssns) & (df["playerid"] == input_id) & (df["goals"] < input_gls), "goals"].count(),
    'gls_over_opp' : df.loc[(df["opposition"] == input_opp) & (df["season"] >= input_ssns) & (df["playerid"] == input_id) & (df["goals"] > input_gls), "goals"].count(),
    'gls_under_ven' : df.loc[(df["venue"] == input_ven) & (df["season"] >= input_ssns) & (df["playerid"] == input_id) & (df["goals"] < input_gls), "goals"].count(),
    'gls_over_ven' : df.loc[(df["venue"] == input_ven) & (df["season"] >= input_ssns) & (df["playerid"] == input_id) & (df["goals"] > input_gls), "goals"].count(),
    'gls_under_2023' : df.loc[(df["season"] == 2023) & (df["playerid"] == input_id) & (df["goals"] < input_gls), "goals"].count(),
    'gls_over_2023' : df.loc[(df["season"] == 2023) & (df["playerid"] == input_id) & (df["goals"] > input_gls), "goals"].count(),
    'di_over_gls_over' : df.loc[(df["season"] >= input_ssns) & (df["playerid"] == input_id) & (df["goals"] > input_gls) & (df["disposals"] > input_di), "disposals"].count(),
    'di_over_gls_under' : df.loc[(df["season"] >= input_ssns) & (df["playerid"] == input_id) & (df["goals"] < input_gls) & (df["disposals"] > input_di), "disposals"].count(),
    'di_under_gls_over' : df.loc[(df["season"] >= input_ssns) & (df["playerid"] == input_id) & (df["goals"] > input_gls) & (df["disposals"] < input_di), "disposals"].count(),
    'di_under_gls_under' : df.loc[(df["season"] >= input_ssns) & (df["playerid"] == input_id) & (df["goals"] < input_gls) & (df["disposals"] < input_di), "disposals"].count(),
    'di_over_gls_over_loc' : df.loc[ (df["season"] >= input_ssns) & (df["playerid"] == input_id) & (df["location"] == input_loc) & (df["goals"] > input_gls) & (df["disposals"] > input_di), "disposals"].count(),
    'di_over_gls_under_loc' : df.loc[ (df["season"] >= input_ssns) & (df["playerid"] == input_id) & (df["location"] == input_loc) & (df["goals"] < input_gls) & (df["disposals"] > input_di), "disposals"].count(),
    'di_under_gls_over_loc' : df.loc[ (df["season"] >= input_ssns) & (df["playerid"] == input_id) & (df["location"] == input_loc) & (df["goals"] > input_gls) & (df["disposals"] < input_di), "disposals"].count(),
    'di_under_gls_under_loc' : df.loc[ (df["season"] >= input_ssns) & (df["playerid"] == input_id) & (df["location"] == input_loc) & (df["goals"] < input_gls) & (df["disposals"] < input_di), "disposals"].count(),
    'di_over_gls_over_opp' : df.loc[ (df["season"] >= input_ssns) & (df["playerid"] == input_id) & (df["opposition"] == input_opp) & (df["goals"] > input_gls) & (df["disposals"] > input_di), "disposals"].count(),
    'di_over_gls_under_opp' : df.loc[ (df["season"] >= input_ssns) & (df["playerid"] == input_id) & (df["opposition"] == input_opp) & (df["goals"] < input_gls) & (df["disposals"] > input_di), "disposals"].count(),
    'di_under_gls_over_opp' : df.loc[ (df["season"] >= input_ssns) & (df["playerid"] == input_id) & (df["opposition"] == input_opp) & (df["goals"] > input_gls) & (df["disposals"] < input_di), "disposals"].count(),
    'di_under_gls_under_opp' : df.loc[ (df["season"] >= input_ssns) & (df["playerid"] == input_id) & (df["opposition"] == input_opp) & (df["goals"] < input_gls) & (df["disposals"] < input_di), "disposals"].count(),
    'di_over_gls_over_ven' : df.loc[ (df["season"] >= input_ssns) & (df["playerid"] == input_id) & (df["venue"] == input_ven) & (df["goals"] > input_gls) & (df["disposals"] > input_di), "disposals"].count(),
    'di_over_gls_under_ven' : df.loc[ (df["season"] >= input_ssns) & (df["playerid"] == input_id) & (df["venue"] == input_ven) & (df["goals"] < input_gls) & (df["disposals"] > input_di), "disposals"].count(),
    'di_under_gls_over_ven' : df.loc[ (df["season"] >= input_ssns) & (df["playerid"] == input_id) & (df["venue"] == input_ven) & (df["goals"] > input_gls) & (df["disposals"] < input_di), "disposals"].count(),
    'di_under_gls_under_ven' : df.loc[(df["season"] >= input_ssns) & (df["playerid"] == input_id) & (df["venue"] == input_ven) & (df["goals"] < input_gls) & (df["disposals"] < input_di), "disposals"].count(),
    'di_over_gls_over_2023' : df.loc[ (df["season"] == 2023) & (df["playerid"] == input_id) & (df["goals"] > input_gls) & (df["disposals"] > input_di), "disposals"].count(),
    'di_over_gls_under_2023' : df.loc[ (df["season"] == 2023) & (df["playerid"] == input_id) & (df["goals"] < input_gls) & (df["disposals"] > input_di), "disposals"].count(),
    'di_under_gls_over_2023' : df.loc[ (df["season"] == 2023) & (df["playerid"] == input_id) & (df["goals"] > input_gls) & (df["disposals"] < input_di), "disposals"].count(),
    'di_under_gls_under_2023' : df.loc[(df["season"] == 2023) &(df["playerid"] == input_id) & (df["goals"] < input_gls) &(df["disposals"] < input_di),"disposals"].count()
  }

  totals = { # used to show users how many total games the gamesHit are out of and to calcuate percentages
    'gms': gamesHit['di_over'] + gamesHit['di_under'],
    'gms_loc': gamesHit['di_over_loc'] + gamesHit['di_under_loc'],
    'gms_opp': gamesHit['di_over_opp'] + gamesHit['di_under_opp'],
    'gms_ven': gamesHit['di_over_ven'] + gamesHit['di_under_ven'],
    'gms_2023': gamesHit['di_over_2023'] + gamesHit['di_under_2023']
  }

  percentages = { #used to show the percentage  the user input for that stat hit, as well as calculate true odds based on previous games only.
    'pc_di_under': gamesHit['di_under'] / totals['gms'],
    'pc_di_over': gamesHit['di_over'] / totals['gms'],
    'pc_di_under_loc': gamesHit['di_under_loc'] / totals['gms_loc'],
    'pc_di_over_loc': gamesHit['di_over_loc'] / totals['gms_loc'],
    'pc_di_under_opp': gamesHit['di_under_opp'] / totals['gms_opp'],
    'pc_di_over_opp': gamesHit['di_over_opp'] / totals['gms_opp'],
    'pc_di_under_ven': gamesHit['di_under_ven'] / totals['gms_ven'],
    'pc_di_over_ven': gamesHit['di_over_ven'] / totals['gms_ven'],
    'pc_di_under_2023': gamesHit['di_under_2023'] / totals['gms_2023'],
    'pc_di_over_2023': gamesHit['di_over_2023'] / totals['gms_2023'],
    'pc_gls_under': gamesHit['gls_under'] / totals['gms'],
    'pc_gls_over': gamesHit['gls_over'] / totals['gms'],
    'pc_gls_under_loc': gamesHit['gls_under_loc'] / totals['gms_loc'],
    'pc_gls_over_loc': gamesHit['gls_over_loc'] / totals['gms_loc'],
    'pc_gls_under_opp': gamesHit['gls_under_opp'] / totals['gms_opp'],
    'pc_gls_over_opp': gamesHit['gls_over_opp'] / totals['gms_opp'],
    'pc_gls_under_ven': gamesHit['gls_under_ven'] / totals['gms_ven'],
    'pc_gls_over_ven': gamesHit['gls_over_ven'] / totals['gms_ven'],
    'pc_gls_under_2023': gamesHit['gls_under_2023'] / totals['gms_2023'],
    'pc_gls_over_2023': gamesHit['gls_over_2023'] / totals['gms_2023'],
    'pc_di_over_gls_over': gamesHit['di_over_gls_over'] / totals['gms'],
    'pc_di_over_gls_under': gamesHit['di_over_gls_under'] / totals['gms'],
    'pc_di_under_gls_over': gamesHit['di_under_gls_over'] / totals['gms'],
    'pc_di_under_gls_under': gamesHit['di_under_gls_under'] / totals['gms'],
    'pc_di_over_gls_over_loc': gamesHit['di_over_gls_over_loc'] / totals['gms_loc'],
    'pc_di_over_gls_under_loc': gamesHit['di_over_gls_under_loc'] / totals['gms_loc'],
    'pc_di_under_gls_over_loc': gamesHit['di_under_gls_over_loc'] / totals['gms_loc'],
    'pc_di_under_gls_under_loc': gamesHit['di_under_gls_under_loc'] / totals['gms_loc'],
    'pc_di_over_gls_over_opp': gamesHit['di_over_gls_over_opp'] / totals['gms_opp'],
    'pc_di_over_gls_under_opp': gamesHit['di_over_gls_under_opp'] / totals['gms_opp'],
    'pc_di_under_gls_over_opp': gamesHit['di_under_gls_over_opp'] / totals['gms_opp'],
    'pc_di_under_gls_under_opp': gamesHit['di_under_gls_under_opp'] /totals['gms_opp'],
    'pc_di_over_gls_over_ven': gamesHit['di_over_gls_over_ven'] / totals['gms_ven'],
    'pc_di_over_gls_under_ven': gamesHit['di_over_gls_under_ven'] / totals['gms_ven'],
    'pc_di_under_gls_over_ven': gamesHit['di_under_gls_over_ven'] / totals['gms_ven'],
    'pc_di_under_gls_under_ven': gamesHit['di_under_gls_under_ven'] / totals['gms_ven'],
    'pc_di_over_gls_over_2023': gamesHit['di_over_gls_over_2023'] / totals['gms_2023'],
    'pc_di_over_gls_under_2023': gamesHit['di_over_gls_under_2023'] / totals['gms_2023'],
    'pc_di_under_gls_over_2023': gamesHit['di_under_gls_over_2023'] / totals['gms_2023'],
    'pc_di_under_gls_under_2023': gamesHit['di_under_gls_under_2023'] / totals['gms_2023']
  }
  return gamesHit, totals, percentages
