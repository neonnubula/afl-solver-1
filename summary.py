import matplotlib.pyplot as plt


# output NEEDS FORMATTING CORRECTIONS, AND CLEANING UP HEADERS IN THE PRINT ETC
def generate_summary(gamesHit, totals, percentages, input_name, input_di,
                     input_gls, input_loc, input_opp, input_ven, input_ssns):

  # Generate horizontal bar graph for the number of games over and under disposal line
  fig, ax = plt.subplots()
  categories = ['Under ' + str(input_di), 'Over ' + str(input_di)]
  values = [gamesHit['di_under'], gamesHit['di_over']]
  ax.barh(categories, values, color=['skyblue', 'orange'])
  ax.set_xlabel('Number of Games')
  ax.set_title('Number of Games Over and Under ' + str(input_di) +
               ' Disposals')
  plt.tight_layout()
  disposal_games_barh_path = 'static/disposal_games_barh.png'
  plt.savefig(disposal_games_barh_path)
  plt.close()
  
  # Generate pie chart for percentage of games
  fig, ax = plt.subplots()
  labels = ['Under ' + str(input_di), 'Over ' + str(input_di)]
  sizes = [percentages['pc_di_under'] * 100, percentages['pc_di_over'] * 100]
  ax.pie(sizes,
         labels=labels,
         autopct='%1.1f%%',
         startangle=90,
         colors=['skyblue', 'orange'])
  ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
  plt.title('Percentage of Games Over and Under ' + str(input_di) +
            ' Disposals')
  plt.tight_layout()
  disposal_percentage_pie_path = 'static/disposal_percentage_pie.png'
  plt.savefig(disposal_percentage_pie_path)
  plt.close()

  # Generate horizontal bar graph for the number of games over and under goal line
  fig, ax = plt.subplots()
  categories = ['Under ' + str(input_gls), 'Over ' + str(input_gls)]
  values = [gamesHit['gls_under'], gamesHit['gls_over']]
  ax.barh(categories, values, color=['lightgreen', 'red'])
  ax.set_xlabel('Number of Games')
  ax.set_title('Number of Games Over and Under ' + str(input_gls) + ' Goals')
  plt.tight_layout()
  goals_games_barh_path = 'static/goals_games_barh.png'
  plt.savefig(goals_games_barh_path)
  plt.close()
  
  # Generate pie chart for the percentage of games
  fig, ax = plt.subplots()
  labels = ['Under ' + str(input_gls), 'Over ' + str(input_gls)]
  sizes = [percentages['pc_gls_under'] * 100, percentages['pc_gls_over'] * 100]
  ax.pie(sizes,
         labels=labels,
         autopct='%1.1f%%',
         startangle=90,
         colors=['lightgreen', 'red'])
  ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
  plt.title('Percentage of Games Over and Under ' + str(input_gls) + ' Goals')
  plt.tight_layout()
  goals_percentage_pie_path = 'static/goals_percentage_pie.png'
  plt.savefig(goals_percentage_pie_path)
  plt.close()

  # Generate horizontal bar graph for Two Leg Same Game Multi results
  fig, ax = plt.subplots()
  categories = ['Disposals Over & Goals Over', 'Disposals Over & Goals Under',
                'Disposals Under & Goals Over', 'Disposals Under & Goals Under']
  values = [gamesHit['di_over_gls_over'], gamesHit['di_over_gls_under'],
            gamesHit['di_under_gls_over'], gamesHit['di_under_gls_under']]
  colors = ['gold', 'lightblue', 'lightgreen', 'salmon']
  ax.barh(categories, values, color=colors)
  ax.set_xlabel('Number of Games')
  ax.set_title('Two Leg SGM for All Games: Disposals and Goals Over/Under')
  plt.tight_layout()
  sgm_games_barh_path = 'static/sgm_games_barh.png'
  plt.savefig(sgm_games_barh_path)
  plt.close()
  
  # Generate pie chart for the percentage share of Two Leg SGM results
  fig, ax = plt.subplots()
  labels = ['Over Disposals & Over Goals', 'Over Disposals & Under Goals',
            'Under Disposals & Over Goals', 'Under Disposals & Under Goals']
  sizes = [percentages['pc_di_over_gls_over'] * 100, percentages['pc_di_over_gls_under'] * 100,
           percentages['pc_di_under_gls_over'] * 100, percentages['pc_di_under_gls_under'] * 100]
  ax.pie(sizes,
         labels=labels,
         autopct='%1.1f%%',
         startangle=90,
         colors=colors)
  ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
  plt.title('Percentage Share of Two Leg SGM Results')
  plt.tight_layout()
  sgm_percentage_pie_path = 'static/sgm_percentage_pie.png'
  plt.savefig(sgm_percentage_pie_path)
  plt.close()


  
  summary = {
      'Report Requested':
      f"\n{input_name} results for disposal line of {input_di} and goals line of {input_gls} for games since {input_ssns}",
      'Results Graphs': (f"<img src='{sgm_games_barh_path}'/> <img src='{sgm_percentage_pie_path}'/><br>"
                         f"<img src='{disposal_games_barh_path}'/>     <img src='{disposal_percentage_pie_path}'/><br>"
                         f"<img src='{goals_games_barh_path}'/> <img src='{goals_percentage_pie_path}'/><br>"),
      'Disposals from All Games Requested': 
      (
       f"All games Results<br>"
       f"Number of games under {input_di} disposals: {gamesHit['di_under']} out of {totals['gms']} games<br>"
       f"Number of games over {input_di} disposals: {gamesHit['di_over']} out of {totals['gms']} games<br>"
       f"Percentage of games under {input_di} disposals: {percentages['pc_di_under'] * 100:.2f}%<br>"
       f"Percentage of games over {input_di} disposals: {percentages['pc_di_over'] * 100:.2f}%<br>"
       f"True odds for under {input_di} disposals on past performance: ${1 / percentages['pc_di_under'] if percentages['pc_di_under'] else 0:.2f}<br>"
       f"True odds for over {input_di} disposals on past performance: ${1 / percentages['pc_di_over'] if percentages['pc_di_over'] else 0:.2f}<br>"
       ),
      'Disposals based on Home or Away Games':
      (f"{input_loc} games Results<br>"
       f"Number of {input_loc} games under {input_di} disposals: {gamesHit['di_under_loc']} out of {totals['gms_loc']} games<br>"
       f"Number of {input_loc} games over {input_di} disposals: {gamesHit['di_over_loc']} out of {totals['gms_loc']} games<br>"
       f"Percentage of {input_loc} games under {input_di} disposals: {percentages['pc_di_under_loc'] * 100:.2f}%<br>"
       f"Percentage of {input_loc} games over {input_di} disposals: {percentages['pc_di_over_loc'] * 100:.2f}%<br>"
       f"True odds for under {input_di} disposals on past {input_loc} performance: ${1 / percentages['pc_di_under_loc'] if percentages['pc_di_under_loc'] else 0:.2f}<br>"
       f"True odds for over {input_di} disposals on past {input_loc} performance: ${1 / percentages['pc_di_over_loc'] if percentages['pc_di_over_loc'] else 0:.2f}<br>"
       ),
      'Disposals against Opposition':
      (f"Against {input_opp} games Results<br>"
       f"Number of games against {input_opp} under {input_di} disposals: {gamesHit['di_under_opp']} out of {totals['gms_opp']} games<br>"
       f"Number of games against {input_opp} over {input_di} disposals: {gamesHit['di_over_opp']} out of {totals['gms_opp']} games<br>"
       f"Percentage of games against {input_opp} under {input_di} disposals: {percentages['pc_di_under_opp'] * 100:.2f}%<br>"
       f"Percentage of games against {input_opp} over {input_di} disposals: {percentages['pc_di_over_opp'] * 100:.2f}%<br>"
       f"True odds for under {input_di} disposals on past against {input_opp} performance: ${1 / percentages['pc_di_under_opp'] if percentages['pc_di_under_opp'] else 0:.2f}<br>"
       f"True odds for over {input_di} disposals on past against {input_opp} performance: ${1 / percentages['pc_di_over_opp'] if percentages['pc_di_over_opp'] else 0:.2f}<br>"
       ),
      'Disposals by Venue':
      (f"At {input_ven} games Results<br>"
       f"Number of at {input_ven} games under {input_di} disposals: {gamesHit['di_under_ven']} out of {totals['gms_ven']} games<br>"
       f"Number of at {input_ven} games over {input_di} disposals: {gamesHit['di_over_ven']} out of {totals['gms_ven']} games<br>"
       f"Percentage of at {input_ven} games under {input_di} disposals: {percentages['pc_di_under_ven'] * 100:.2f}%<br>"
       f"Percentage of at {input_ven} games over {input_di} disposals: {percentages['pc_di_over_ven'] * 100:.2f}%<br>"
       f"True odds for under {input_di} disposals on past at {input_ven} performance: ${1 / percentages['pc_di_under_ven'] if percentages['pc_di_under_ven'] else 0:.2f}<br>"
       f"True odds for over {input_di} disposals on past at {input_ven} performance: ${1 / percentages['pc_di_over_ven'] if percentages['pc_di_over_ven'] else 0:.2f}<br>"
       ),
      'Disposals in 2023':
      (f"2023 Season games Results<br>"
       f"Number of 2023 games under {input_di} disposals: {gamesHit['di_under_2023']} out of {totals['gms_2023']} games<br>"
       f"Number of 2023 games over {input_di} disposals: {gamesHit['di_over_2023']} out of {totals['gms_2023']} games<br>"
       f"Percentage of 2023 games under {input_di} disposals: {percentages['pc_di_under_2023'] * 100:.2f}%<br>"
       f"Percentage of 2023 games over {input_di} disposals: {percentages['pc_di_over_2023'] * 100:.2f}%<br>"
       f"True odds for under {input_di} disposals on 2023 performance: ${1 / percentages['pc_di_under_2023'] if percentages['pc_di_under_2023'] else 0:.2f}<br>"
       f"True odds for over {input_di} disposals on 2023 performance: ${1 / percentages['pc_di_over_2023'] if percentages['pc_di_over_2023'] else 0:.2f}<br>"
       ),
      'goalsIntro':
      "Goals<br><br>",
      'Goals based on All Games Requested':
      ("All games Results<br>"
       f"Number of games under {input_gls} goals: {gamesHit['gls_under']} out of {totals['gms']} games<br>"
       f"Number of games over {input_gls} goals: {gamesHit['gls_over']} out of {totals['gms']} games<br>"
       f"Percentage of games under {input_gls} goals: {percentages['pc_gls_under'] * 100:.2f}%<br>"
       f"Percentage of games over {input_gls} goals: {percentages['pc_gls_over'] * 100:.2f}%<br>"
       f"True odds for under {input_gls} goals on past performance: ${1 / percentages['pc_gls_under'] if percentages['pc_gls_under'] else 0:.2f}<br>"
       f"True odds for over {input_gls} goals on past performance: ${1 / percentages['pc_gls_over'] if percentages['pc_gls_over'] else 0:.2f}<br>"
       ),
      'Goals by Home or Away':
      (f"{input_loc} games Results<br>"
       f"Number of {input_loc} games under {input_gls} goals: {gamesHit['gls_under_loc']} out of {totals['gms_loc']} games<br>"
       f"Number of {input_loc} games over {input_gls} goals: {gamesHit['gls_over_loc']} out of {totals['gms_loc']} games<br>"
       f"Percentage of {input_loc} games under {input_gls} goals: {percentages['pc_gls_under_loc'] * 100:.2f}%<br>"
       f"Percentage of {input_loc} games over {input_gls} goals: {percentages['pc_gls_over_loc'] * 100:.2f}%<br>"
       f"True odds for under {input_gls} goals on past {input_loc} performance: ${1 / percentages['pc_gls_under_loc'] if percentages['pc_gls_under_loc'] else 0:.2f}<br>"
       f"True odds for over {input_gls} goals on past {input_loc} performance: ${1 / percentages['pc_gls_over_loc'] if percentages['pc_gls_over_loc'] else 0:.2f}<br>"
       ),
      'Goals Against Opposition':
      (f"Against {input_opp} games Results<br>"
       f"Number of games against {input_opp} under {input_gls} goals: {gamesHit['gls_under_opp']} out of {totals['gms_opp']} games<br>"
       f"Number of games against {input_opp} over {input_gls} goals: {gamesHit['gls_over_opp']} out of {totals['gms_opp']} games<br>"
       f"Percentage of games against {input_opp} under {input_gls} goals: {percentages['pc_gls_under_opp'] * 100:.2f}%<br>"
       f"Percentage of games against {input_opp} over {input_gls} goals: {percentages['pc_gls_over_opp'] * 100:.2f}%<br>"
       f"True odds for under {input_gls} goals on past against {input_opp} performance: ${1 / percentages['pc_gls_under_opp'] if percentages['pc_gls_under_opp'] else 0:.2f}<br>"
       f"True odds for over {input_gls} goals on past against {input_opp} performance: ${1 / percentages['pc_gls_over_opp'] if percentages['pc_gls_over_opp'] else 0:.2f}<br>"
       ),
      'Goals by Venue':
      (f"At {input_ven} games Results<br>"
       f"Number of at {input_ven} games under {input_gls} goals: {gamesHit['gls_under_ven']} out of {totals['gms_ven']} games<br>"
       f"Number of at {input_ven} games over {input_gls} goals: {gamesHit['gls_over_ven']} out of {totals['gms_ven']} games<br>"
       f"Percentage of at {input_ven} games under {input_gls} goals: {percentages['pc_gls_under_ven'] * 100:.2f}%<br>"
       f"Percentage of at {input_ven} games over {input_gls} goals: {percentages['pc_gls_over_ven'] * 100:.2f}%<br>"
       f"True odds for under {input_gls} goals on past at {input_ven} performance: ${1 / percentages['pc_gls_under_ven'] if percentages['pc_gls_under_ven'] else 0:.2f}<br>"
       f"True odds for over {input_gls} goals on past at {input_ven} performance: ${1 / percentages['pc_gls_over_ven'] if percentages['pc_gls_over_ven'] else 0:.2f}<br>"
       ),
      'Goals in 2023':
      (f"2023 Season games Results<br>"
       f"Number of 2023 games under {input_gls} goals: {gamesHit['gls_under_2023']} out of {totals['gms_2023']} games<br>"
       f"Number of 2023 games over {input_gls} goals: {gamesHit['gls_over_2023']} out of {totals['gms_2023']} games<br>"
       f"Percentage of 2023 games under {input_gls} goals: {percentages['pc_gls_under_2023'] * 100:.2f}%<br>"
       f"Percentage of 2023 games over {input_gls} goals: {percentages['pc_gls_over_2023'] * 100:.2f}%<br>"
       f"True odds for under {input_gls} goals on 2023 performance: ${1 / percentages['pc_gls_under_2023'] if percentages['pc_gls_under_2023'] else 0:.2f}<br>"
       f"True odds for over {input_gls} goals on 2023 performance: ${1 / percentages['pc_gls_over_2023'] if percentages['pc_gls_over_2023'] else 0:.2f}<br>"
       ),
      'twoLeg':
      "2 LEG COMBO RESULTS<br>",
      'Two Leg Same Game Multi for All Games Requested':
      (f"Number of games with disposals over {input_di} and goals over {input_gls}: {gamesHit['di_over_gls_over']} out of {totals['gms']} games<br>"
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
      'Two Leg Same Game Multi by Home or Away':
      (f"{input_loc} games Results<br>"
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
      'Two Leg Same Game Multi versus Opposition':
      (f"Against {input_opp} games Results<br>"
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
      'Two Leg Same Game Multi by Venue':
      (f"At {input_ven} games Results<br>"
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
      'Two Leg Same Game Multi in 2023':
      (f"2023 Season Results<br>"
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
