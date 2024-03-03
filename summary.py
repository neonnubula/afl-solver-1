# output NEEDS FORMATTING CORRECTIONS, AND CLEANING UP HEADERS IN THE PRINT ETC
def generate_summary(gamesHit, totals, percentages, input_name, input_di, input_gls, input_loc, input_opp, input_ven, input_ssns):
  summary = {
    'Report Requested': f"\n{input_name} results for disposal line of {input_di} and goals line of {input_gls} for games since {input_ssns}",
    'Disposals from All Games Requested' : (
      f"All games Results<br>"
      f"Number of games under {input_di} disposals: {gamesHit['di_under']} out of {totals['gms']} games<br>"
      f"Number of games over {input_di} disposals: {gamesHit['di_over']} out of {totals['gms']} games<br>"
      f"Percentage of games under {input_di} disposals: {percentages['pc_di_under'] * 100:.2f}%<br>"
      f"Percentage of games over {input_di} disposals: {percentages['pc_di_over'] * 100:.2f}%<br>"
      f"True odds for under {input_di} disposals on past performance: ${1 / percentages['pc_di_under'] if percentages['pc_di_under'] else 0:.2f}<br>"
      f"True odds for over {input_di} disposals on past performance: ${1 / percentages['pc_di_over'] if percentages['pc_di_over'] else 0:.2f}<br>"
    ),
    'Disposals based on Home or Away Games': (
      f"{input_loc} games Results<br>"
      f"Number of {input_loc} games under {input_di} disposals: {gamesHit['di_under_loc']} out of {totals['gms_loc']} games<br>"
      f"Number of {input_loc} games over {input_di} disposals: {gamesHit['di_over_loc']} out of {totals['gms_loc']} games<br>"
      f"Percentage of {input_loc} games under {input_di} disposals: {percentages['pc_di_under_loc'] * 100:.2f}%<br>"
      f"Percentage of {input_loc} games over {input_di} disposals: {percentages['pc_di_over_loc'] * 100:.2f}%<br>"
      f"True odds for under {input_di} disposals on past {input_loc} performance: ${1 / percentages['pc_di_under_loc'] if percentages['pc_di_under_loc'] else 0:.2f}<br>"
      f"True odds for over {input_di} disposals on past {input_loc} performance: ${1 / percentages['pc_di_over_loc'] if percentages['pc_di_over_loc'] else 0:.2f}<br>"
    ),
    'Disposals against Opposition': (
      f"Against {input_opp} games Results<br>"
      f"Number of games against {input_opp} under {input_di} disposals: {gamesHit['di_under_opp']} out of {totals['gms_opp']} games<br>"
      f"Number of games against {input_opp} over {input_di} disposals: {gamesHit['di_over_opp']} out of {totals['gms_opp']} games<br>"
      f"Percentage of games against {input_opp} under {input_di} disposals: {percentages['pc_di_under_opp'] * 100:.2f}%<br>"
      f"Percentage of games against {input_opp} over {input_di} disposals: {percentages['pc_di_over_opp'] * 100:.2f}%<br>"
      f"True odds for under {input_di} disposals on past against {input_opp} performance: ${1 / percentages['pc_di_under_opp'] if percentages['pc_di_under_opp'] else 0:.2f}<br>"
      f"True odds for over {input_di} disposals on past against {input_opp} performance: ${1 / percentages['pc_di_over_opp'] if percentages['pc_di_over_opp'] else 0:.2f}<br>"
    ),
    'Disposals by Venue': (
      f"At {input_ven} games Results<br>"
      f"Number of at {input_ven} games under {input_di} disposals: {gamesHit['di_under_ven']} out of {totals['gms_ven']} games<br>"
      f"Number of at {input_ven} games over {input_di} disposals: {gamesHit['di_over_ven']} out of {totals['gms_ven']} games<br>"
      f"Percentage of at {input_ven} games under {input_di} disposals: {percentages['pc_di_under_ven'] * 100:.2f}%<br>"
      f"Percentage of at {input_ven} games over {input_di} disposals: {percentages['pc_di_over_ven'] * 100:.2f}%<br>"
      f"True odds for under {input_di} disposals on past at {input_ven} performance: ${1 / percentages['pc_di_under_ven'] if percentages['pc_di_under_ven'] else 0:.2f}<br>"
      f"True odds for over {input_di} disposals on past at {input_ven} performance: ${1 / percentages['pc_di_over_ven'] if percentages['pc_di_over_ven'] else 0:.2f}<br>"
    ),
    'Disposals in 2023': (
      f"2023 Season games Results<br>"
      f"Number of 2023 games under {input_di} disposals: {gamesHit['di_under_2023']} out of {totals['gms_2023']} games<br>"
      f"Number of 2023 games over {input_di} disposals: {gamesHit['di_over_2023']} out of {totals['gms_2023']} games<br>"
      f"Percentage of 2023 games under {input_di} disposals: {percentages['pc_di_under_2023'] * 100:.2f}%<br>"
      f"Percentage of 2023 games over {input_di} disposals: {percentages['pc_di_over_2023'] * 100:.2f}%<br>"
      f"True odds for under {input_di} disposals on 2023 performance: ${1 / percentages['pc_di_under_2023'] if percentages['pc_di_under_2023'] else 0:.2f}<br>"
      f"True odds for over {input_di} disposals on 2023 performance: ${1 / percentages['pc_di_over_2023'] if percentages['pc_di_over_2023'] else 0:.2f}<br>"
    ),
      'goalsIntro' : "Goals<br><br>",
      'Goals based on All Games Requested': (
        "All games Results<br>"
        f"Number of games under {input_gls} goals: {gamesHit['gls_under']} out of {totals['gms']} games<br>"
        f"Number of games over {input_gls} goals: {gamesHit['gls_over']} out of {totals['gms']} games<br>"
        f"Percentage of games under {input_gls} goals: {percentages['pc_gls_under'] * 100:.2f}%<br>"
        f"Percentage of games over {input_gls} goals: {percentages['pc_gls_over'] * 100:.2f}%<br>"
        f"True odds for under {input_gls} goals on past performance: ${1 / percentages['pc_gls_under'] if percentages['pc_gls_under'] else 0:.2f}<br>"
        f"True odds for over {input_gls} goals on past performance: ${1 / percentages['pc_gls_over'] if percentages['pc_gls_over'] else 0:.2f}<br>"
      ),  
      'Goals by Home or Away': (
        f"{input_loc} games Results<br>"
        f"Number of {input_loc} games under {input_gls} goals: {gamesHit['gls_under_loc']} out of {totals['gms_loc']} games<br>"
        f"Number of {input_loc} games over {input_gls} goals: {gamesHit['gls_over_loc']} out of {totals['gms_loc']} games<br>"
        f"Percentage of {input_loc} games under {input_gls} goals: {percentages['pc_gls_under_loc'] * 100:.2f}%<br>"
        f"Percentage of {input_loc} games over {input_gls} goals: {percentages['pc_gls_over_loc'] * 100:.2f}%<br>"
        f"True odds for under {input_gls} goals on past {input_loc} performance: ${1 / percentages['pc_gls_under_loc'] if percentages['pc_gls_under_loc'] else 0:.2f}<br>"
        f"True odds for over {input_gls} goals on past {input_loc} performance: ${1 / percentages['pc_gls_over_loc'] if percentages['pc_gls_over_loc'] else 0:.2f}<br>"
      ),
      'Goals Against Opposition': (
        f"Against {input_opp} games Results<br>"
        f"Number of games against {input_opp} under {input_gls} goals: {gamesHit['gls_under_opp']} out of {totals['gms_opp']} games<br>"
        f"Number of games against {input_opp} over {input_gls} goals: {gamesHit['gls_over_opp']} out of {totals['gms_opp']} games<br>"
        f"Percentage of games against {input_opp} under {input_gls} goals: {percentages['pc_gls_under_opp'] * 100:.2f}%<br>"
        f"Percentage of games against {input_opp} over {input_gls} goals: {percentages['pc_gls_over_opp'] * 100:.2f}%<br>"
        f"True odds for under {input_gls} goals on past against {input_opp} performance: ${1 / percentages['pc_gls_under_opp'] if percentages['pc_gls_under_opp'] else 0:.2f}<br>"
        f"True odds for over {input_gls} goals on past against {input_opp} performance: ${1 / percentages['pc_gls_over_opp'] if percentages['pc_gls_over_opp'] else 0:.2f}<br>"
      ),
      'Goals by Venue': (
        f"At {input_ven} games Results<br>"
        f"Number of at {input_ven} games under {input_gls} goals: {gamesHit['gls_under_ven']} out of {totals['gms_ven']} games<br>"
        f"Number of at {input_ven} games over {input_gls} goals: {gamesHit['gls_over_ven']} out of {totals['gms_ven']} games<br>"
        f"Percentage of at {input_ven} games under {input_gls} goals: {percentages['pc_gls_under_ven'] * 100:.2f}%<br>"
        f"Percentage of at {input_ven} games over {input_gls} goals: {percentages['pc_gls_over_ven'] * 100:.2f}%<br>"
        f"True odds for under {input_gls} goals on past at {input_ven} performance: ${1 / percentages['pc_gls_under_ven'] if percentages['pc_gls_under_ven'] else 0:.2f}<br>"
        f"True odds for over {input_gls} goals on past at {input_ven} performance: ${1 / percentages['pc_gls_over_ven'] if percentages['pc_gls_over_ven'] else 0:.2f}<br>"
      ),
      'Goals in 2023': (
        f"2023 Season games Results<br>"
        f"Number of 2023 games under {input_gls} goals: {gamesHit['gls_under_2023']} out of {totals['gms_2023']} games<br>"
        f"Number of 2023 games over {input_gls} goals: {gamesHit['gls_over_2023']} out of {totals['gms_2023']} games<br>"
        f"Percentage of 2023 games under {input_gls} goals: {percentages['pc_gls_under_2023'] * 100:.2f}%<br>"
        f"Percentage of 2023 games over {input_gls} goals: {percentages['pc_gls_over_2023'] * 100:.2f}%<br>"
        f"True odds for under {input_gls} goals on 2023 performance: ${1 / percentages['pc_gls_under_2023'] if percentages['pc_gls_under_2023'] else 0:.2f}<br>"
        f"True odds for over {input_gls} goals on 2023 performance: ${1 / percentages['pc_gls_over_2023'] if percentages['pc_gls_over_2023'] else 0:.2f}<br>"
      ),
      'twoLeg' : "2 LEG COMBO RESULTS<br>",
      'Two Leg Same Game Multi for All Games Requested': (
        f"Number of games with disposals over {input_di} and goals over {input_gls}: {gamesHit['di_over_gls_over']} out of {totals['gms']} games<br>"
        f"Number of games with disposals over {input_di} and goals under {input_gls}: {gamesHit['di_over_gls_under']} out of {totals['gms']} games<br>"
        f"Number of games with disposals under {input_di} and goals over {input_gls}: {gamesHit['di_under_gls_over']} out of {totals['gms']} games<br>"
        f"Number of games with disposals under {input_di} and goals under {input_gls}: {gamesHit['di_under_gls_under']} out of {totals['gms']} games<br>"
        f"Percentage of games with disposals over {input_di} and goals over {input_gls}: {percentages['pc_di_over_gls_over'] * 100:.2f}%<br>"
        f"Percentage of games with disposals over {input_di} and goals under {input_gls}: {percentages['pc_di_over_gls_under'] * 100:.2f}%<br>"
        f"Percentage of games with disposals under {input_di} and goals over {input_gls}: {percentages['pc_di_under_gls_over'] * 100:.2f}%<br>"
        f"Percentage of games with disposals under {input_di} and goals under {input_gls}: {percentages['pc_di_under_gls_under'] * 100:.2f}%<br>"
        f"True odds for games with disposals over {input_di} and goals over {input_gls} on past performance: ${1 / percentages['pc_di_over_gls_over'] if percentages['pc_di_over_gls_over'] else 0:.2f}<br>"
        f"True odds for games with disposals over {input_di} and goals under {input_gls} on past performance: ${1 / percentages['pc_di_over_gls_under'] if percentages['pc_di_over_gls_under'] else 0:.2f}<br>"
        f"True odds for games with disposals under {input_di} and goals over {input_gls} on past performance: ${1 / percentages['pc_di_under_gls_over'] if percentages['pc_di_under_gls_over'] else 0:.2f}<br>"
        f"True odds for games with disposals under {input_di} and goals under {input_gls} on past performance: ${1 / percentages['pc_di_under_gls_under'] if percentages['pc_di_under_gls_under'] else 0:.2f}<br>"
      ),
      'Two Leg Same Game Multi by Home or Away': (
        f"{input_loc} games Results<br>"
        f"Number of {input_loc} games with disposals over {input_di} and goals over {input_gls}: {gamesHit['di_over_gls_over_loc']} out of {totals['gms_loc']} games<br>"
        f"Number of {input_loc} games with disposals over {input_di} and goals under {input_gls}: {gamesHit['di_over_gls_under_loc']} out of {totals['gms_loc']} games<br>"
        f"Number of {input_loc} games with disposals under {input_di} and goals over {input_gls}: {gamesHit['di_under_gls_over_loc']} out of {totals['gms_loc']} games<br>"
        f"Number of {input_loc} games with disposals under {input_di} and goals under {input_gls}: {gamesHit['di_under_gls_under_loc']} out of {totals['gms_loc']} games<br>"
        f"Percentage of {input_loc} games with disposals over {input_di} and goals over {input_gls}: {percentages['pc_di_over_gls_over_loc'] * 100:.2f}%<br>"
        f"Percentage of {input_loc} games with disposals over {input_di} and goals under {input_gls}: {percentages['pc_di_over_gls_under_loc'] * 100:.2f}%<br>"
        f"Percentage of {input_loc} games with disposals under {input_di} and goals over {input_gls}: {percentages['pc_di_under_gls_over_loc'] * 100:.2f}%<br>"
        f"Percentage of {input_loc} games with disposals under {input_di} and goals under {input_gls}: {percentages['pc_di_under_gls_under_loc'] * 100:.2f}%<br>"
        f"True odds for {input_loc} games with disposals over {input_di} and goals over {input_gls} on past performance: ${1 / percentages['pc_di_over_gls_over_loc'] if percentages['pc_di_over_gls_over_loc'] else 0:.2f}<br>"
        f"True odds for {input_loc} games with disposals over {input_di} and goals under {input_gls} on past performance: ${1 / percentages['pc_di_over_gls_under_loc'] if percentages['pc_di_over_gls_under_loc'] else 0:.2f}<br>"
        f"True odds for {input_loc} games with disposals under {input_di} and goals over {input_gls} on past performance: ${1 / percentages['pc_di_under_gls_over_loc'] if percentages['pc_di_under_gls_over_loc'] else 0:.2f}<br>"
        f"True odds for {input_loc} games with disposals under {input_di} and goals under {input_gls} on past performance: ${1 / percentages['pc_di_under_gls_under_loc'] if percentages['pc_di_under_gls_under_loc'] else 0:.2f}<br>"
      ),
      'Two Leg Same Game Multi versus Opposition': (
        f"Against {input_opp} games Results<br>"
        f"Number of games against {input_opp} with disposals over {input_di} and goals over {input_gls}: {gamesHit['di_over_gls_over_opp']} out of {totals['gms_opp']} games<br>"
        f"Number of games against {input_opp} with disposals over {input_di} and goals under {input_gls}: {gamesHit['di_over_gls_under_opp']} out of {totals['gms_opp']} games<br>"
        f"Number of games against {input_opp} with disposals under {input_di} and goals over {input_gls}: {gamesHit['di_under_gls_over_opp']} out of {totals['gms_opp']} games<br>"
        f"Number of games against {input_opp} with disposals under {input_di} and goals under {input_gls}: {gamesHit['di_under_gls_under_opp']} out of {totals['gms_opp']} games<br>"
        f"Percentage of games against {input_opp} with disposals over {input_di} and goals over {input_gls}: {percentages['pc_di_over_gls_over_opp'] * 100:.2f}%<br>"
        f"Percentage of games against {input_opp} with disposals over {input_di} and goals under {input_gls}: {percentages['pc_di_over_gls_under_opp'] * 100:.2f}%<br>"
        f"Percentage of games against {input_opp} with disposals under {input_di} and goals over {input_gls}: {percentages['pc_di_under_gls_over_opp'] * 100:.2f}%<br>"
        f"Percentage of games against {input_opp} with disposals under {input_di} and goals under {input_gls}: {percentages['pc_di_under_gls_under_opp'] * 100:.2f}%<br>"
        f"True odds for games against {input_opp} with disposals over {input_di} and goals over {input_gls} on past performance: ${1 / percentages['pc_di_over_gls_over_opp'] if percentages['pc_di_over_gls_over_opp'] else 0:.2f}<br>"
        f"True odds for games against {input_opp} with disposals over {input_di} and goals under {input_gls} on past performance: ${1 / percentages['pc_di_over_gls_under_opp'] if percentages['pc_di_over_gls_under_opp'] else 0:.2f}<br>"
        f"True odds for games against {input_opp} with disposals under {input_di} and goals over {input_gls} on past performance: ${1 / percentages['pc_di_under_gls_over_opp'] if percentages['pc_di_under_gls_over_opp'] else 0:.2f}<br>"
        f"True odds for games against {input_opp} with disposals under {input_di} and goals under {input_gls} on past performance: ${1 / percentages['pc_di_under_gls_under_opp'] if percentages['pc_di_under_gls_under_opp'] else 0:.2f}<br>"
      ),
      'Two Leg Same Game Multi by Venue': (
        f"At {input_ven} games Results<br>"
        f"Number of {input_ven} games with disposals over {input_di} and goals over {input_gls}: {gamesHit['di_over_gls_over_ven']} out of {totals['gms_ven']} games<br>"
        f"Number of {input_ven} games with disposals over {input_di} and goals under {input_gls}: {gamesHit['di_over_gls_under_ven']} out of {totals['gms_ven']} games<br>"
        f"Number of {input_ven} games with disposals under {input_di} and goals over {input_gls}: {gamesHit['di_under_gls_over_ven']} out of {totals['gms_ven']} games<br>"
        f"Number of {input_ven} games with disposals under {input_di} and goals under {input_gls}: {gamesHit['di_under_gls_under_ven']} out of {totals['gms_ven']} games<br>"
        f"Percentage of {input_ven} games with disposals over {input_di} and goals over {input_gls}: {percentages['pc_di_over_gls_over_ven'] * 100:.2f}%<br>"
        f"Percentage of {input_ven} games with disposals over {input_di} and goals under {input_gls}: {percentages['pc_di_over_gls_under_ven'] * 100:.2f}%<br>"
        f"Percentage of {input_ven} games with disposals under {input_di} and goals over {input_gls}: {percentages['pc_di_under_gls_over_ven'] * 100:.2f}%<br>"
        f"Percentage of {input_ven} games with disposals under {input_di} and goals under {input_gls}: {percentages['pc_di_under_gls_under_ven'] * 100:.2f}%<br>"
        f"True odds for {input_ven} games with disposals over {input_di} and goals over {input_gls} on past performance: ${1 / percentages['pc_di_over_gls_over_ven'] if percentages['pc_di_over_gls_over_ven'] else 0:.2f}<br>"
        f"True odds for {input_ven} games with disposals over {input_di} and goals under {input_gls} on past performance: ${1 / percentages['pc_di_over_gls_under_ven'] if percentages['pc_di_over_gls_under_ven'] else 0:.2f}<br>"
        f"True odds for {input_ven} games with disposals under {input_di} and goals over {input_gls} on past performance: ${1 / percentages['pc_di_under_gls_over_ven'] if percentages['pc_di_under_gls_over_ven'] else 0:.2f}<br>"
        f"True odds for {input_ven} games with disposals under {input_di} and goals under {input_gls} on past performance: ${1 / percentages['pc_di_under_gls_under_ven'] if percentages['pc_di_under_gls_under_ven'] else 0:.2f}<br>"
      ),
      'Two Leg Same Game Multi in 2023': (
        f"2023 Season Results<br>"
        f"Number of 2023 season games with disposals over {input_di} and goals over {input_gls}: {gamesHit['di_over_gls_over_2023']} out of {totals['gms_2023']} games<br>"
        f"Number of 2023 season games with disposals over {input_di} and goals under {input_gls}: {gamesHit['di_over_gls_under_2023']} out of {totals['gms_2023']} games<br>"
        f"Number of 2023 season games with disposals under {input_di} and goals over {input_gls}: {gamesHit['di_under_gls_over_2023']} out of {totals['gms_2023']} games<br>"
        f"Number of 2023 season games with disposals under {input_di} and goals under {input_gls}: {gamesHit['di_under_gls_under_2023']} out of {totals['gms_2023']} games<br>"
        f"Percentage of 2023 season games with disposals over {input_di} and goals over {input_gls}: {percentages['pc_di_over_gls_over_2023'] * 100:.2f}%<br>"
        f"Percentage of 2023 season games with disposals over {input_di} and goals under {input_gls}: {percentages['pc_di_over_gls_under_2023'] * 100:.2f}%<br>"
        f"Percentage of 2023 season games with disposals under {input_di} and goals over {input_gls}: {percentages['pc_di_under_gls_over_2023'] * 100:.2f}%<br>"
        f"Percentage of 2023 season games with disposals under {input_di} and goals under {input_gls}: {percentages['pc_di_under_gls_under_2023'] * 100:.2f}%<br>"
        f"True odds for 2023 season games with disposals over {input_di} and goals over {input_gls} on past performance: ${1 / percentages['pc_di_over_gls_over_2023'] if percentages['pc_di_over_gls_over_2023'] else 0:.2f}<br>"
        f"True odds for 2023 season games with disposals over {input_di} and goals under {input_gls} on past performance: ${1 / percentages['pc_di_over_gls_under_2023'] if percentages['pc_di_over_gls_under_2023'] else 0:.2f}<br>"
        f"True odds for 2023 season games with disposals under {input_di} and goals over {input_gls} on past performance: ${1 / percentages['pc_di_under_gls_over_2023'] if percentages['pc_di_under_gls_over_2023'] else 0:.2f}<br>"
        f"True odds for 2023 season games with disposals under {input_di} and goals under {input_gls} on past performance: ${1 / percentages['pc_di_under_gls_under_2023'] if percentages['pc_di_under_gls_under_2023'] else 0:.2f}<br>"
      )
      }
  return summary