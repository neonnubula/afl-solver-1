  import pandas as pd

  #User input
  input_name = input("Enter the player name: (john/david) ")
  input_di = float(input("What is the disposal line?: "))
  input_gls = float(input("What is the goal line?: "))
  input_loc = input("Is the player at home or away?: (home/away) ")
  input_opp = input("Who is the opposition? ")
  input_ven = input("What stadium is the game at? ")
  input_ssns = int(input("From what season do you want results? (ex: 2021) "))

  #read the CSV data into a Dataframe
  df = pd.read_csv('test-data.csv')


  def solver():
    gamesHit = { # each diciontary entry counts the amount of games that stat correlated with the user input
      'di_under' : df.loc[(df["season"] >= input_ssns) & (df["name"] == input_name) & (df["disposals"] < input_di), "disposals"].count(),
      'di_over' : df.loc[(df["season"] >= input_ssns) & (df["name"] == input_name) & (df["disposals"] > input_di), "disposals"].count(),
      'di_under_loc' : df.loc[(df["location"] == input_loc) &(df["name"] == input_name) &(df["season"] >= input_ssns) &(df["disposals"] < input_di),"disposals"].count(),
      'di_over_loc' : df.loc[(df["location"] == input_loc) &(df["name"] == input_name) &(df["season"] >= input_ssns) &(df["disposals"] > input_di),"disposals"].count(),
      'di_under_opp' : df.loc[(df["opposition"] == input_opp) &(df["name"] == input_name) &(df["season"] >= input_ssns) &(df["disposals"] < input_di),"disposals"].count(),
      'di_over_opp' : df.loc[(df["opposition"] == input_opp) & (df["name"] == input_name) & (df["season"] >= input_ssns) & (df["disposals"] > input_di), "disposals"].count(),
      'di_under_ven' : df.loc[(df["venue"] == input_ven) & (df["name"] == input_name) & (df["season"] >= input_ssns) & (df["disposals"] < input_di), "disposals"].count(),
      'di_over_ven' : df.loc[(df["venue"] == input_ven) & (df["name"] == input_name) & (df["season"] >= input_ssns) & (df["disposals"] > input_di), "disposals"].count(),
      'di_under_2023' : df.loc[(df["season"] == 2023) & (df["name"] == input_name) & (df["disposals"] < input_di), "disposals"].count(),
      'di_over_2023' : df.loc[(df["season"] == 2023) & (df["name"] == input_name) & (df["disposals"] > input_di), "disposals"].count(),
      'gls_under' : df.loc[(df["season"] >= input_ssns) & (df["goals"] < input_gls), "goals"].count(),
      'gls_over' : df.loc[(df["season"] >= input_ssns) & (df["goals"] > input_gls), "goals"].count(),
      'gls_under_loc' : df.loc[(df["location"] == input_loc) & (df["season"] >= input_ssns) & (df["goals"] < input_gls), "goals"].count(),
      'gls_over_loc' : df.loc[(df["location"] == input_loc) & (df["season"] >= input_ssns) & (df["goals"] > input_gls), "goals"].count(),
      'gls_under_opp' : df.loc[(df["opposition"] == input_opp) & (df["season"] >= input_ssns) & (df["goals"] < input_gls), "goals"].count(),
      'gls_over_opp' : df.loc[(df["opposition"] == input_opp) & (df["season"] >= input_ssns) & (df["goals"] > input_gls), "goals"].count(),
      'gls_under_ven' : df.loc[(df["venue"] == input_ven) & (df["season"] >= input_ssns) & (df["goals"] < input_gls), "goals"].count(),
      'gls_over_ven' : df.loc[(df["venue"] == input_ven) & (df["season"] >= input_ssns) & (df["goals"] > input_gls), "goals"].count(),
      'gls_under_2023' : df.loc[(df["season"] == 2023) & (df["goals"] < input_gls), "goals"].count(),
      'gls_over_2023' : df.loc[(df["season"] == 2023) & (df["goals"] > input_gls), "goals"].count(),
      'di_over_gls_over' : df.loc[(df["season"] >= input_ssns) & (df["name"] == input_name) & (df["goals"] > input_gls) & (df["disposals"] > input_di), "disposals"].count(),
      'di_over_gls_under' : df.loc[(df["season"] >= input_ssns) & (df["name"] == input_name) & (df["goals"] < input_gls) & (df["disposals"] > input_di), "disposals"].count(),
      'di_under_gls_over' : df.loc[(df["season"] >= input_ssns) & (df["name"] == input_name) & (df["goals"] > input_gls) & (df["disposals"] < input_di), "disposals"].count(),
      'di_under_gls_under' : df.loc[(df["season"] >= input_ssns) & (df["name"] == input_name) & (df["goals"] < input_gls) & (df["disposals"] < input_di), "disposals"].count(),
      'di_over_gls_over_loc' : df.loc[ (df["season"] >= input_ssns) & (df["name"] == input_name) & (df["location"] == input_loc) & (df["goals"] > input_gls) & (df["disposals"] > input_di), "disposals"].count(),
      'di_over_gls_under_loc' : df.loc[ (df["season"] >= input_ssns) & (df["name"] == input_name) & (df["location"] == input_loc) & (df["goals"] < input_gls) & (df["disposals"] > input_di), "disposals"].count(),
      'di_under_gls_over_loc' : df.loc[ (df["season"] >= input_ssns) & (df["name"] == input_name) & (df["location"] == input_loc) & (df["goals"] > input_gls) & (df["disposals"] < input_di), "disposals"].count(),
      'di_under_gls_under_loc' : df.loc[ (df["season"] >= input_ssns) & (df["name"] == input_name) & (df["location"] == input_loc) & (df["goals"] < input_gls) & (df["disposals"] < input_di), "disposals"].count(),
      'di_over_gls_over_opp' : df.loc[ (df["season"] >= input_ssns) & (df["name"] == input_name) & (df["opposition"] == input_opp) & (df["goals"] > input_gls) & (df["disposals"] > input_di), "disposals"].count(),
      'di_over_gls_under_opp' : df.loc[ (df["season"] >= input_ssns) & (df["name"] == input_name) & (df["opposition"] == input_opp) & (df["goals"] < input_gls) & (df["disposals"] > input_di), "disposals"].count(),
      'di_under_gls_over_opp' : df.loc[ (df["season"] >= input_ssns) & (df["name"] == input_name) & (df["opposition"] == input_opp) & (df["goals"] > input_gls) & (df["disposals"] < input_di), "disposals"].count(),
      'di_under_gls_under_opp' : df.loc[ (df["season"] >= input_ssns) & (df["name"] == input_name) & (df["opposition"] == input_opp) & (df["goals"] < input_gls) & (df["disposals"] < input_di), "disposals"].count(),
      'di_over_gls_over_ven' : df.loc[ (df["season"] >= input_ssns) & (df["name"] == input_name) & (df["venue"] == input_ven) & (df["goals"] > input_gls) & (df["disposals"] > input_di), "disposals"].count(),
      'di_over_gls_under_ven' : df.loc[ (df["season"] >= input_ssns) & (df["name"] == input_name) & (df["venue"] == input_ven) & (df["goals"] < input_gls) & (df["disposals"] > input_di), "disposals"].count(),
      'di_under_gls_over_ven' : df.loc[ (df["season"] >= input_ssns) & (df["name"] == input_name) & (df["venue"] == input_ven) & (df["goals"] > input_gls) & (df["disposals"] < input_di), "disposals"].count(),
      'di_under_gls_under_ven' : df.loc[(df["season"] >= input_ssns) & (df["name"] == input_name) & (df["venue"] == input_ven) & (df["goals"] < input_gls) & (df["disposals"] < input_di), "disposals"].count(),
      'di_over_gls_over_2023' : df.loc[ (df["season"] >= input_ssns) & (df["name"] == input_name) & (df["season"] == 2023) & (df["goals"] > input_gls) & (df["disposals"] > input_di), "disposals"].count(),
      'di_over_gls_under_2023' : df.loc[ (df["season"] >= input_ssns) & (df["name"] == input_name) & (df["season"] == 2023) & (df["goals"] < input_gls) & (df["disposals"] > input_di), "disposals"].count(),
      'di_under_gls_over_2023' : df.loc[ (df["season"] >= input_ssns) & (df["name"] == input_name) & (df["season"] == 2023) & (df["goals"] > input_gls) & (df["disposals"] < input_di), "disposals"].count(),
      'di_under_gls_under_2023' : df.loc[(df["season"] >= input_ssns) &(df["name"] == input_name) &(df["season"] == 2023) &(df["goals"] < input_gls) &(df["disposals"] < input_di),"disposals"].count()
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

  gamesHit, totals, percentages = solver()


  # output NEEDS FORMATTING CORRECTIONS, AND CLEANING UP HEADERS IN THE PRINT ETC
  summary = {
    'intro': f"\n{input_name} results for disposal line of {input_di} and goals line of {input_gls}\n\nDisposals\n\n",
    'disposalsAll' : (
        f"All games Results\n"
        f"Number of games under {input_di} disposals: {gamesHit['di_under']}\n"
        f"Number of games over {input_di} disposals: {gamesHit['di_over']}\n"
        f"Percentage of games under {input_di} disposals: {percentages['pc_di_under'] * 100:.2f}%\n"
        f"Percentage of games over {input_di} disposals: {percentages['pc_di_over'] * 100:.2f}%\n"
        f"True odds for under {input_di} disposals on past performance: {1 / percentages['pc_di_under'] if percentages['pc_di_under'] else 0:.2f}\n"
        f"True odds for over {input_di} disposals on past performance: {1 / percentages['pc_di_over'] if percentages['pc_di_over'] else 0:.2f}\n"
      ),
      'disposalsLoc': (
        f"{input_loc} games Results/n"
        f"Number of {input_loc} games under {input_di} disposals: {gamesHit['di_under_loc']}/n"
        f"Number of {input_loc} games over {input_di} disposals: {gamesHit['di_over_loc']}/n"
        f"Percentage of {input_loc} games under {input_di} disposals: {percentages['pc_di_under_loc'] * 100:.2f}%/n"
        f"Percentage of {input_loc} games over {input_di} disposals: {percentages['pc_di_over_loc'] * 100:.2f}%/n"
        f"True odds for under {input_di} disposals on past {input_loc} performance: {1 / percentages['pc_di_under_loc'] if percentages['pc_di_under_loc'] else 0:.2f}/n"
        f"True odds for over {input_di} disposals on past {input_loc} performance: {1 / percentages['pc_di_over_loc'] if percentages['pc_di_over_loc'] else 0:.2f}/n"
      ),
      'disposalsOpp': (
        f"Against {input_opp} games Results/n"
        f"Number of games against {input_opp} under {input_di} disposals: {gamesHit['di_under_opp']}/n"
        f"Number of games against {input_opp} over {input_di} disposals: {gamesHit['di_over_opp']}/n"
        f"Percentage of games against {input_opp} under {input_di} disposals: {percentages['pc_di_under_opp'] * 100:.2f}%/n"
        f"Percentage of games against {input_opp} over {input_di} disposals: {percentages['pc_di_over_opp'] * 100:.2f}%/n"
        f"True odds for under {input_di} disposals on past against {input_opp} performance: {1 / percentages['pc_di_under_opp'] if percentages['pc_di_under_opp'] else 0:.2f}/n"
        f"True odds for over {input_di} disposals on past against {input_opp} performance: {1 / percentages['pc_di_over_opp'] if percentages['pc_di_over_opp'] else 0:.2f}/n"
      ),
      'disposalsVen': (
        f"At {input_ven} games Results/n"
        f"Number of at {input_ven} games under {input_di} disposals: {gamesHit['di_under_ven']}/n"
        f"Number of at {input_ven} games over {input_di} disposals: {gamesHit['di_over_ven']}/n"
        f"Percentage of at {input_ven} games under {input_di} disposals: {percentages['pc_di_under_ven'] * 100:.2f}%/n"
        f"Percentage of at {input_ven} games over {input_di} disposals: {percentages['pc_di_over_ven'] * 100:.2f}%/n"
        f"True odds for under {input_di} disposals on past at {input_ven} performance: {1 / percentages['pc_di_under_ven'] if percentages['pc_di_under_ven'] else 0:.2f}/n"
        f"True odds for over {input_di} disposals on past at {input_ven} performance: {1 / percentages['pc_di_over_ven'] if percentages['pc_di_over_ven'] else 0:.2f}/n"
      ),
      'disposals2023': (
        f"2023 Season games Results/n"
        f"Number of 2023 games under {input_di} disposals: {gamesHit['di_under_2023']}/n"
        f"Number of 2023 games over {input_di} disposals: {gamesHit['di_over_2023']}/n"
        f"Percentage of 2023 games under {input_di} disposals: {percentages['pc_di_under_2023'] * 100:.2f}%/n"
        f"Percentage of 2023 games over {input_di} disposals: {percentages['pc_di_over_2023'] * 100:.2f}%/n"
        f"True odds for under {input_di} disposals on 2023 performance: {1 / percentages['pc_di_under_2023'] if percentages['pc_di_under_2023'] else 0:.2f}/n"
        f"True odds for over {input_di} disposals on 2023 performance: {1 / percentages['pc_di_over_2023'] if percentages['pc_di_over_2023'] else 0:.2f}/n"
      ),
      'goalsIntro' : f"\nGoals\n\n",
      'goalsAll': (
        "All games Results\n"
        f"Number of games under {input_gls} goals: {gamesHit['gls_under']}\n"
        f"Number of games over {input_gls} goals: {gamesHit['gls_over']}\n"
        f"Percentage of games under {input_gls} goals: {percentages['pc_gls_under'] * 100:.2f}%\n"
        f"Percentage of games over {input_gls} goals: {percentages['pc_gls_over'] * 100:.2f}%\n"
        f"True odds for under {input_gls} goals on past performance: {1 / percentages['pc_gls_under'] if percentages['pc_gls_under'] else 0:.2f}\n"
        f"True odds for over {input_gls} goals on past performance: {1 / percentages['pc_gls_over'] if percentages['pc_gls_over'] else 0:.2f}\n"
      ),  
      'goalsLoc': (
        f"{input_loc} games Results/n"
        f"Number of {input_loc} games under {input_gls} goals: {gamesHit['gls_under_loc']}\n"
        f"Number of {input_loc} games over {input_gls} goals: {gamesHit['gls_over_loc']}\n"
        f"Percentage of {input_loc} games under {input_gls} goals: {percentages['pc_gls_under_loc'] * 100:.2f}%\n"
        f"Percentage of {input_loc} games over {input_gls} goals: {percentages['pc_gls_over_loc'] * 100:.2f}%\n"
        f"True odds for under {input_gls} goals on past {input_loc} performance: {1 / percentages['pc_gls_under_loc'] if percentages['pc_gls_under_loc'] else 0:.2f}\n"
        f"True odds for over {input_gls} goals on past {input_loc} performance: {1 / percentages['pc_gls_over_loc'] if percentages['pc_gls_over_loc'] else 0:.2f}\n"
      ),
      'goalsOpp': (
        f"Against {input_opp} games Results\n"
        f"Number of games against {input_opp} under {input_gls} goals: {gamesHit['gls_under_opp']}\n"
        f"Number of games against {input_opp} over {input_gls} goals: {gamesHit['gls_over_opp']}\n"
        f"Percentage of games against {input_opp} under {input_gls} goals: {percentages['pc_gls_under_opp'] * 100:.2f}%\n"
        f"Percentage of games against {input_opp} over {input_gls} goals: {percentages['pc_gls_over_opp'] * 100:.2f}%\n"
        f"True odds for under {input_gls} goals on past against {input_opp} performance: {1 / percentages['pc_gls_under_opp'] if percentages['pc_gls_under_opp'] else 0:.2f}\n"
        f"True odds for over {input_gls} goals on past against {input_opp} performance: {1 / percentages['pc_gls_over_opp'] if percentages['pc_gls_over_opp'] else 0:.2f}\n"
      ),
      'goalsVen': (
        f"At {input_ven} games Results\n"
        f"Number of at {input_ven} games under {input_gls} goals: {gamesHit['gls_under_ven']}\n"
        f"Number of at {input_ven} games over {input_gls} goals: {gamesHit['gls_over_ven']}\n"
        f"Percentage of at {input_ven} games under {input_gls} goals: {percentages['pc_gls_under_ven'] * 100:.2f}%\n"
        f"Percentage of at {input_ven} games over {input_gls} goals: {percentages['pc_gls_over_ven'] * 100:.2f}%\n"
        f"True odds for under {input_gls} goals on past at {input_ven} performance: {1 / percentages['pc_gls_under_ven'] if percentages['pc_gls_under_ven'] else 0:.2f}\n"
        f"True odds for over {input_gls} goals on past at {input_ven} performance: {1 / percentages['pc_gls_over_ven'] if percentages['pc_gls_over_ven'] else 0:.2f}\n"
      ),
      'goals2023': (
        f"2023 Season games Results\n"
        f"Number of 2023 games under {input_gls} goals: {gamesHit['gls_under_2023']}\n"
        f"Number of 2023 games over {input_gls} goals: {gamesHit['gls_over_2023']}\n"
        f"Percentage of 2023 games under {input_gls} goals: {percentages['pc_gls_under_2023'] * 100:.2f}%\n"
        f"Percentage of 2023 games over {input_gls} goals: {percentages['pc_gls_over_2023'] * 100:.2f}%\n"
        f"True odds for under {input_gls} goals on 2023 performance: {1 / percentages['pc_gls_under_2023'] if percentages['pc_gls_under_2023'] else 0:.2f}\n"
        f"True odds for over {input_gls} goals on 2023 performance: {1 / percentages['pc_gls_over_2023'] if percentages['pc_gls_over_2023'] else 0:.2f}\n"
      ),
      'twoLeg' : "2 LEG COMBO RESULTS",
      'twoLegAll': (
        f"Number of games with disposals over {input_di} and goals over {input_gls}: {gamesHit['di_over_gls_over']}\n"
        f"Number of games with disposals over {input_di} and goals under {input_gls}: {gamesHit['di_over_gls_under']}\n"
        f"Number of games with disposals under {input_di} and goals over {input_gls}: {gamesHit['di_under_gls_over']}\n"
        f"Number of games with disposals under {input_di} and goals under {input_gls}: {gamesHit['di_under_gls_under']}\n"
        f"Percentage of games with disposals over {input_di} and goals over {input_gls}: {percentages['pc_di_over_gls_over'] * 100:.2f}%\n"
        f"Percentage of games with disposals over {input_di} and goals under {input_gls}: {percentages['pc_di_over_gls_under'] * 100:.2f}%\n"
        f"Percentage of games with disposals under {input_di} and goals over {input_gls}: {percentages['pc_di_under_gls_over'] * 100:.2f}%\n"
        f"Percentage of games with disposals under {input_di} and goals under {input_gls}: {percentages['pc_di_under_gls_under'] * 100:.2f}%\n"
        f"True odds for games with disposals over {input_di} and goals over {input_gls} on past performance: {1 / percentages['pc_di_over_gls_over'] if percentages['pc_di_over_gls_over'] else 0:.2f}\n"
        f"True odds for games with disposals over {input_di} and goals under {input_gls} on past performance: {1 / percentages['pc_di_over_gls_under'] if percentages['pc_di_over_gls_under'] else 0:.2f}\n"
        f"True odds for games with disposals under {input_di} and goals over {input_gls} on past performance: {1 / percentages['pc_di_under_gls_over'] if percentages['pc_di_under_gls_over'] else 0:.2f}\n"
        f"True odds for games with disposals under {input_di} and goals under {input_gls} on past performance: {1 / percentages['pc_di_under_gls_under'] if percentages['pc_di_under_gls_under'] else 0:.2f}\n"
      ),
      'twoLegLoc': (
        f"{input_loc} games Results"
        f"Number of {input_loc} games with disposals over {input_di} and goals over {input_gls}: {gamesHit['di_over_gls_over_loc']}\n"
        f"Number of {input_loc} games with disposals over {input_di} and goals under {input_gls}: {gamesHit['di_over_gls_under_loc']}\n"
        f"Number of {input_loc} games with disposals under {input_di} and goals over {input_gls}: {gamesHit['di_under_gls_over_loc']}\n"
        f"Number of {input_loc} games with disposals under {input_di} and goals under {input_gls}: {gamesHit['di_under_gls_under_loc']}\n"
        f"Percentage of {input_loc} games with disposals over {input_di} and goals over {input_gls}: {percentages['pc_di_over_gls_over_loc'] * 100:.2f}%\n"
        f"Percentage of {input_loc} games with disposals over {input_di} and goals under {input_gls}: {percentages['pc_di_over_gls_under_loc'] * 100:.2f}%\n"
        f"Percentage of {input_loc} games with disposals under {input_di} and goals over {input_gls}: {percentages['pc_di_under_gls_over_loc'] * 100:.2f}%\n"
        f"Percentage of {input_loc} games with disposals under {input_di} and goals under {input_gls}: {percentages['pc_di_under_gls_under_loc'] * 100:.2f}%\n"
        f"True odds for {input_loc} games with disposals over {input_di} and goals over {input_gls} on past performance: {1 / percentages['pc_di_over_gls_over_loc'] if percentages['pc_di_over_gls_over_loc'] else 0:.2f}\n"
        f"True odds for {input_loc} games with disposals over {input_di} and goals under {input_gls} on past performance: {1 / percentages['pc_di_over_gls_under_loc'] if percentages['pc_di_over_gls_under_loc'] else 0:.2f}\n"
        f"True odds for {input_loc} games with disposals under {input_di} and goals over {input_gls} on past performance: {1 / percentages['pc_di_under_gls_over_loc'] if percentages['pc_di_under_gls_over_loc'] else 0:.2f}\n"
        f"True odds for {input_loc} games with disposals under {input_di} and goals under {input_gls} on past performance: {1 / percentages['pc_di_under_gls_under_loc'] if percentages['pc_di_under_gls_under_loc'] else 0:.2f}\n"
      ),
      'twoLegOpp': (
        f"Against {input_opp} games Results"
        f"Number of games against {input_opp} with disposals over {input_di} and goals over {input_gls}: {gamesHit['di_over_gls_over_opp']}\n"
        f"Number of games against {input_opp} with disposals over {input_di} and goals under {input_gls}: {gamesHit['di_over_gls_under_opp']}\n"
        f"Number of games against {input_opp} with disposals under {input_di} and goals over {input_gls}: {gamesHit['di_under_gls_over_opp']}\n"
        f"Number of games against {input_opp} with disposals under {input_di} and goals under {input_gls}: {gamesHit['di_under_gls_under_opp']}\n"
        f"Percentage of games against {input_opp} with disposals over {input_di} and goals over {input_gls}: {percentages['pc_di_over_gls_over_opp'] * 100:.2f}%\n"
        f"Percentage of games against {input_opp} with disposals over {input_di} and goals under {input_gls}: {percentages['pc_di_over_gls_under_opp'] * 100:.2f}%\n"
        f"Percentage of games against {input_opp} with disposals under {input_di} and goals over {input_gls}: {percentages['pc_di_under_gls_over_opp'] * 100:.2f}%\n"
        f"Percentage of games against {input_opp} with disposals under {input_di} and goals under {input_gls}: {percentages['pc_di_under_gls_under_opp'] * 100:.2f}%\n"
        f"True odds for games against {input_opp} with disposals over {input_di} and goals over {input_gls} on past performance: {1 / percentages['pc_di_over_gls_over_opp'] if percentages['pc_di_over_gls_over_opp'] else 0:.2f}\n"
        f"True odds for games against {input_opp} with disposals over {input_di} and goals under {input_gls} on past performance: {1 / percentages['pc_di_over_gls_under_opp'] if percentages['pc_di_over_gls_under_opp'] else 0:.2f}\n"
        f"True odds for games against {input_opp} with disposals under {input_di} and goals over {input_gls} on past performance: {1 / percentages['pc_di_under_gls_over_opp'] if percentages['pc_di_under_gls_over_opp'] else 0:.2f}\n"
        f"True odds for games against {input_opp} with disposals under {input_di} and goals under {input_gls} on past performance: {1 / percentages['pc_di_under_gls_under_opp'] if percentages['pc_di_under_gls_under_opp'] else 0:.2f}\n"
      ),
      'twoLegVen': (
        f"Venue {input_ven} games Results\n"
        f"Number of {input_ven} games with disposals over {input_di} and goals over {input_gls}: {gamesHit['di_over_gls_over_ven']}\n"
        f"Number of {input_ven} games with disposals over {input_di} and goals under {input_gls}: {gamesHit['di_over_gls_under_ven']}\n"
        f"Number of {input_ven} games with disposals under {input_di} and goals over {input_gls}: {gamesHit['di_under_gls_over_ven']}\n"
        f"Number of {input_ven} games with disposals under {input_di} and goals under {input_gls}: {gamesHit['di_under_gls_under_ven']}\n"
        f"Percentage of {input_ven} games with disposals over {input_di} and goals over {input_gls}: {percentages['pc_di_over_gls_over_ven'] * 100:.2f}%\n"
        f"Percentage of {input_ven} games with disposals over {input_di} and goals under {input_gls}: {percentages['pc_di_over_gls_under_ven'] * 100:.2f}%\n"
        f"Percentage of {input_ven} games with disposals under {input_di} and goals over {input_gls}: {percentages['pc_di_under_gls_over_ven'] * 100:.2f}%\n"
        f"Percentage of {input_ven} games with disposals under {input_di} and goals under {input_gls}: {percentages['pc_di_under_gls_under_ven'] * 100:.2f}%\n"
        f"True odds for {input_ven} games with disposals over {input_di} and goals over {input_gls} on past performance: {1 / percentages['pc_di_over_gls_over_ven'] if percentages['pc_di_over_gls_over_ven'] else 0:.2f}\n"
        f"True odds for {input_ven} games with disposals over {input_di} and goals under {input_gls} on past performance: {1 / percentages['pc_di_over_gls_under_ven'] if percentages['pc_di_over_gls_under_ven'] else 0:.2f}\n"
        f"True odds for {input_ven} games with disposals under {input_di} and goals over {input_gls} on past performance: {1 / percentages['pc_di_under_gls_over_ven'] if percentages['pc_di_under_gls_over_ven'] else 0:.2f}\n"
        f"True odds for {input_ven} games with disposals under {input_di} and goals under {input_gls} on past performance: {1 / percentages['pc_di_under_gls_under_ven'] if percentages['pc_di_under_gls_under_ven'] else 0:.2f}\n"
      ),
      'twoLeg2023': (
        f"2023 Season Results\n"
        f"Number of 2023 season games with disposals over {input_di} and goals over {input_gls}: {gamesHit['di_over_gls_over_2023']}\n"
        f"Number of 2023 season games with disposals over {input_di} and goals under {input_gls}: {gamesHit['di_over_gls_under_2023']}\n"
        f"Number of 2023 season games with disposals under {input_di} and goals over {input_gls}: {gamesHit['di_under_gls_over_2023']}\n"
        f"Number of 2023 season games with disposals under {input_di} and goals under {input_gls}: {gamesHit['di_under_gls_under_2023']}\n"
        f"Percentage of 2023 season games with disposals over {input_di} and goals over {input_gls}: {percentages['pc_di_over_gls_over_2023'] * 100:.2f}%\n"
        f"Percentage of 2023 season games with disposals over {input_di} and goals under {input_gls}: {percentages['pc_di_over_gls_under_2023'] * 100:.2f}%\n"
        f"Percentage of 2023 season games with disposals under {input_di} and goals over {input_gls}: {percentages['pc_di_under_gls_over_2023'] * 100:.2f}%\n"
        f"Percentage of 2023 season games with disposals under {input_di} and goals under {input_gls}: {percentages['pc_di_under_gls_under_2023'] * 100:.2f}%\n"
        f"True odds for 2023 season games with disposals over {input_di} and goals over {input_gls} on past performance: {1 / percentages['pc_di_over_gls_over_2023'] if percentages['pc_di_over_gls_over_2023'] else 0:.2f}\n"
        f"True odds for 2023 season games with disposals over {input_di} and goals under {input_gls} on past performance: {1 / percentages['pc_di_over_gls_under_2023'] if percentages['pc_di_over_gls_under_2023'] else 0:.2f}\n"
        f"True odds for 2023 season games with disposals under {input_di} and goals over {input_gls} on past performance: {1 / percentages['pc_di_under_gls_over_2023'] if percentages['pc_di_under_gls_over_2023'] else 0:.2f}\n"
        f"True odds for 2023 season games with disposals under {input_di} and goals under {input_gls} on past performance: {1 / percentages['pc_di_under_gls_under_2023'] if percentages['pc_di_under_gls_under_2023'] else 0:.2f}\n"
      )
  }

  # Printing the summary, rough and incorrect formatting and titles, maybe this but the summary needs editing certainly
  for key, value in summary.items():
      print(f"{key}: {value}\n")