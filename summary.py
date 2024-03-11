import matplotlib.pyplot as plt
import math

# output NEEDS FORMATTING CORRECTIONS, AND CLEANING UP HEADERS IN THE PRINT ETC
def generate_summary(gamesHit, totals, percentages, input_name, input_di,
                     input_gls, input_loc, input_opp, input_ven, input_ssns):
  #graphGenPath = 'FlaskWebProject1/'
  graphGenPath = ''
  staticPath = 'static/graphs/'
  # # Generate horizontal bar graph for the number of games over and under disposal line
  fig, ax = plt.subplots()
  categories = ['Under ' + str(input_di), 'Over ' + str(input_di)]
  values = [gamesHit['di_under'], gamesHit['di_over']]
  ax.barh(categories, values, color=['skyblue', 'orange'])
  ax.set_xlabel('Number of Games')
  ax.set_title('Number of Games Over and Under ' + str(input_di) +
               ' Disposals')
  plt.tight_layout()
  disposal_games_barh_path = staticPath + 'disposal_games_barh.png'
  plt.savefig(graphGenPath + disposal_games_barh_path)
  plt.close()
  
  # Generate pie chart for percentage of games
  fig, ax = plt.subplots()
  labels = ['Under ' + str(input_di), 'Over ' + str(input_di)]
  # Ensure there are no nan values passed to pie chart generator. Disposals under assumed to be 100% for sake of the graph
  if math.isnan(percentages['pc_di_under']) or math.isnan(percentages['pc_di_under']):
    sizes = [100, 0]
  else:
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
  disposal_percentage_pie_path = staticPath + 'disposal_percentage_pie.png'
  plt.savefig(graphGenPath + disposal_percentage_pie_path)
  plt.close()

  # Generate horizontal bar graph for the number of games over and under goal line
  fig, ax = plt.subplots()
  categories = ['Under ' + str(input_gls), 'Over ' + str(input_gls)]
  values = [gamesHit['gls_under'], gamesHit['gls_over']]
  ax.barh(categories, values, color=['lightgreen', 'red'])
  ax.set_xlabel('Number of Games')
  ax.set_title('Number of Games Over and Under ' + str(input_gls) + ' Goals')
  plt.tight_layout()
  goals_games_barh_path = staticPath + 'goals_games_barh.png'
  plt.savefig(graphGenPath + goals_games_barh_path)
  plt.close()
  
  # Generate pie chart for the percentage of games
  fig, ax = plt.subplots()
  labels = ['Under ' + str(input_gls), 'Over ' + str(input_gls)]
  # Ensure there are no nan values passed to pie chart generator. Goals under assumed to be 100% for sake of the graph
  if math.isnan(percentages['pc_gls_under']) or math.isnan(percentages['pc_gls_over']):
    sizes = [100, 0]
  else:
    sizes = [percentages['pc_gls_under'] * 100, percentages['pc_gls_over'] * 100]
  ax.pie(sizes,
         labels=labels,
         autopct='%1.1f%%',
         startangle=90,
         colors=['lightgreen', 'red'])
  ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
  plt.title('Percentage of Games Over and Under ' + str(input_gls) + ' Goals')
  plt.tight_layout()
  goals_percentage_pie_path = staticPath + 'goals_percentage_pie.png'
  plt.savefig(graphGenPath + goals_percentage_pie_path)
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
  sgm_games_barh_path = staticPath + 'sgm_games_barh.png'
  plt.savefig(graphGenPath + sgm_games_barh_path)
  plt.close()
  
  # Generate pie chart for the percentage share of Two Leg SGM results
  fig, ax = plt.subplots()
  labels = ['Over Disposals & Over Goals', 'Over Disposals & Under Goals',
            'Under Disposals & Over Goals', 'Under Disposals & Under Goals']
  # Ensure there are no nan values passed to pie chart generator. Disposals and Goals under assumed to be 100% for sake of the graph
  # Backslash character enables splitting of if condition over two lines
  if math.isnan(percentages['pc_di_over_gls_over']) or math.isnan(percentages['pc_di_over_gls_under']) \
  or math.isnan(percentages['pc_di_under_gls_over']) or math.isnan(percentages['pc_di_under_gls_under']):
    sizes = [0, 0, 0, 100]
  else:
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
  sgm_percentage_pie_path = staticPath + 'sgm_percentage_pie.png'
  plt.savefig(graphGenPath + sgm_percentage_pie_path)
  plt.close()


  
  summary = [
      ['Summary Results', 'Heading'],
      ['Report Requested', 'Statement', f'{input_name} results for disposal line of {input_di} and goals line of {input_gls} for games since {input_ssns}'],
      [
        [
          f'{sgm_games_barh_path}', 
          f'{sgm_percentage_pie_path}', 
          f'{disposal_games_barh_path}', 
          f'{disposal_percentage_pie_path}', 
          f'{goals_games_barh_path}', 
          f'{goals_percentage_pie_path}'
        ],
        'Graph'
      ],
      ['Disposals from All Games Requested', "Stats", [
            [f"Number of games under {input_di} disposals:", f"{gamesHit['di_under']} out of {totals['gms']} games"],
            [f"Number of games over {input_di} disposals:", f" {gamesHit['di_over']} out of {totals['gms']} games"],
            [f"Percentage of games under {input_di} disposals:", f" {'N/A' if totals['gms'] == 0 else '{0:.2f}%'.format(percentages['pc_di_under'] * 100)}"],
            [f"Percentage of games over {input_di} disposals:", f" {'N/A' if totals['gms'] == 0 else '{0:.2f}%'.format(percentages['pc_di_over'] * 100)}"],
            [f"True odds for under {input_di} disposals on past performance:", f" {'N/A' if percentages['pc_di_under'] == 0 or totals['gms'] == 0 else '${0:.2f}'.format(1 / percentages['pc_di_under'])}"],
            [f"True odds for over {input_di} disposals on past performance:", f" {'N/A' if percentages['pc_di_over'] == 0 or totals['gms'] == 0 else '${0:.2f}'.format(1 / percentages['pc_di_over'])}"]
          ]
      ],
      [f'Disposals based on Home or Away Games - {input_loc} games Results', 'Stats', [
            [f"Number of {input_loc} games under {input_di} disposals:", f"{gamesHit['di_under_loc']} out of {totals['gms_loc']} games"],
            [f"Number of {input_loc} games over {input_di} disposals:", f" {gamesHit['di_over_loc']} out of {totals['gms_loc']} games"],
            [f"Percentage of {input_loc} games under {input_di} disposals:", f" {'N/A' if totals['gms_loc'] == 0 else '{0:.2f}%'.format(percentages['pc_di_under_loc'] * 100)}"],
            [f"Percentage of {input_loc} games over {input_di} disposals:", f" {'N/A' if totals['gms_loc'] == 0 else '{0:.2f}%'.format(percentages['pc_di_over_loc'] * 100)}"],
            [f"True odds for under {input_di} disposals on past {input_loc} performance:", f" {'N/A' if percentages['pc_di_under_loc'] == 0 or totals['gms_loc'] == 0 else '${0:.2f}'.format(1 / percentages['pc_di_under_loc'])}"],
            [f"True odds for over {input_di} disposals on past {input_loc} performance:", f" {'N/A' if percentages['pc_di_over_loc'] == 0 or totals['gms_loc'] == 0 else '${0:.2f}'.format(1 / percentages['pc_di_over_loc']) }"]
         ]
      ],
      [f'Disposals against Opposition - Against {input_opp} games Results', 'Stats', [
            [f"Number of games against {input_opp} under {input_di} disposals:", f"{gamesHit['di_under_opp']} out of {totals['gms_opp']} games"],
            [f"Number of games against {input_opp} over {input_di} disposals:", f"{gamesHit['di_over_opp']} out of {totals['gms_opp']} games"],
            [f"Percentage of games against {input_opp} under {input_di} disposals:", f"{'N/A' if totals['gms_opp'] == 0 else '{0:.2f}%'.format(percentages['pc_di_under_opp'] * 100)}"],
            [f"Percentage of games against {input_opp} over {input_di} disposals:", f"{'N/A' if totals['gms_opp'] == 0 else '{0:.2f}%'.format(percentages['pc_di_over_opp'] * 100)}"],
            [f"True odds for under {input_di} disposals on past against {input_opp} performance:", f"{'N/A' if percentages['pc_di_under_opp'] == 0 or totals['gms_opp'] == 0 else '${0:.2f}'.format(1 / percentages['pc_di_under_opp'])}"],
            [f"True odds for over {input_di} disposals on past against {input_opp} performance:", f"{'N/A' if percentages['pc_di_over_opp'] == 0 or totals['gms_opp'] == 0 else '${0:.2f}'.format(1 / percentages['pc_di_over_opp'])}"]
        ]
      ],
      [f'Disposals by Venue - At {input_ven} games Results', 'Stats', [
            [f"Number of at {input_ven} games under {input_di} disposals:", f"{gamesHit['di_under_ven']} out of {totals['gms_ven']} games"],
            [f"Number of at {input_ven} games over {input_di} disposals:", f"{gamesHit['di_over_ven']} out of {totals['gms_ven']} games"],
            [f"Percentage of at {input_ven} games under {input_di} disposals:", f"{'N/A' if totals['gms_ven'] == 0 else '{0:.2f}%'.format(percentages['pc_di_under_ven'] * 100)}"],
            [f"Percentage of at {input_ven} games over {input_di} disposals:", f"{'N/A' if totals['gms_ven'] == 0 else '{0:.2f}%'.format(percentages['pc_di_over_ven'] * 100)}"],
            [f"True odds for under {input_di} disposals on past at {input_ven} performance:", f"{'N/A' if percentages['pc_di_under_ven'] == 0 or totals['gms_ven'] == 0 else '${0:.2f}'.format(1 / percentages['pc_di_under_ven'])}"],
            [f"True odds for over {input_di} disposals on past at {input_ven} performance:", f"{'N/A' if percentages['pc_di_over_ven'] == 0 or totals['gms_ven'] == 0 else '${0:.2f}'.format(1 / percentages['pc_di_over_ven'])}"]
        ]
      ],
      ['Disposals in 2023 - Season games Results', 'Stats', [
            [f"Number of 2023 games under {input_di} disposals:", f"{gamesHit['di_under_2023']} out of {totals['gms_2023']} games"],
            [f"Number of 2023 games over {input_di} disposals:", f"{gamesHit['di_over_2023']} out of {totals['gms_2023']} games"],
            [f"Percentage of 2023 games under {input_di} disposals:", f"{'N/A' if totals['gms_2023'] == 0 else '{0:.2f}%'.format(percentages['pc_di_under_2023'] * 100)}"],
            [f"Percentage of 2023 games over {input_di} disposals:", f"{'N/A' if totals['gms_2023'] == 0 else '{0:.2f}%'.format(percentages['pc_di_over_2023'] * 100)}"],
            [f"True odds for under {input_di} disposals on 2023 performance:", f"{'N/A' if percentages['pc_di_under_2023'] == 0 or totals['gms_2023'] == 0 else '${0:.2f}'.format(1 / percentages['pc_di_under_2023'])}"],
            [f"True odds for over {input_di} disposals on 2023 performance:", f"{'N/A' if percentages['pc_di_over_2023'] == 0 or totals['gms_2023'] == 0 else '${0:.2f}'.format(1 / percentages['pc_di_over_2023'])}"]
        ]
      ],
      ['Goals', 'Heading'],
      ['Goals based on All Games Requested', 'Stats', [
            [f"Number of games under {input_gls} goals:", f"{gamesHit['gls_under']} out of {totals['gms']} games"],
            [f"Number of games over {input_gls} goals:", f"{gamesHit['gls_over']} out of {totals['gms']} games"],
            [f"Percentage of games under {input_gls} goals:", f"{'N/A' if totals['gms'] == 0 else '{0:.2f}%'.format(percentages['pc_gls_under'] * 100)}"],
            [f"Percentage of games over {input_gls} goals:", f"{'N/A' if totals['gms'] == 0 else '{0:.2f}%'.format(percentages['pc_gls_over'] * 100)}"],
            [f"True odds for under {input_gls} goals on past performance:", f"{'N/A' if percentages['pc_gls_under'] == 0 or totals['gms'] == 0 else '${0:.2f}'.format(1 / percentages['pc_gls_under'])}"],
            [f"True odds for over {input_gls} goals on past performance:", f"{'N/A' if percentages['pc_gls_over'] == 0 or totals['gms'] == 0 else '${0:.2f}'.format(1 / percentages['pc_gls_over'])}"]
        ]
      ],
      [f'Goals by Home or Away - {input_loc} games Results', 'Stats', [
            [f"Number of {input_loc} games under {input_gls} goals:", f"{gamesHit['gls_under_loc']} out of {totals['gms_loc']} games"],
            [f"Number of {input_loc} games over {input_gls} goals:", f"{gamesHit['gls_over_loc']} out of {totals['gms_loc']} games"],
            [f"Percentage of {input_loc} games under {input_gls} goals:", f"{'N/A' if totals['gms_loc'] == 0 else '{0:.2f}%'.format(percentages['pc_gls_under_loc'] * 100)}"],
            [f"Percentage of {input_loc} games over {input_gls} goals:", f"{'N/A' if totals['gms_loc'] == 0 else '{0:.2f}%'.format(percentages['pc_gls_over_loc'] * 100)}"],
            [f"True odds for under {input_gls} goals on past {input_loc} performance:", f"{'N/A' if percentages['pc_gls_under_loc'] == 0 or totals['gms_loc'] == 0 else '${0:.2f}'.format(1 / percentages['pc_gls_under_loc'])}"],
            [f"True odds for over {input_gls} goals on past {input_loc} performance:", f"{'N/A' if percentages['pc_gls_over_loc'] == 0 or totals['gms_loc'] == 0 else '${0:.2f}'.format(1 / percentages['pc_gls_over_loc'])}"]
        ]
      ],
      [f'Goals Against Opposition - Against {input_opp} games Results', 'Stats', [
            [f"Number of games against {input_opp} under {input_gls} goals:", f"{gamesHit['gls_under_opp']} out of {totals['gms_opp']} games"],
            [f"Number of games against {input_opp} over {input_gls} goals:", f"{gamesHit['gls_over_opp']} out of {totals['gms_opp']} games"],
            [f"Percentage of games against {input_opp} under {input_gls} goals:", f"{'N/A' if totals['gms_opp'] == 0 else '{0:.2f}%'.format(percentages['pc_gls_under_opp'] * 100)}"],
            [f"Percentage of games against {input_opp} over {input_gls} goals:", f"{'N/A' if totals['gms_opp'] == 0 else '{0:.2f}%'.format(percentages['pc_gls_over_opp'] * 100)}"],
            [f"True odds for under {input_gls} goals on past {input_loc} performance:", f"{'N/A' if percentages['pc_gls_under_opp'] == 0 or totals['gms_opp'] == 0 else '${0:.2f}'.format(1 / percentages['pc_gls_under_opp'])}"],
            [f"True odds for over {input_gls} goals on past {input_loc} performance:", f"{'N/A' if percentages['pc_gls_over_opp'] == 0 or totals['gms_opp'] == 0 else '${0:.2f}'.format(1 / percentages['pc_gls_over_opp'])}"]
        ]
      ],
      [f'Goals by Venue - At {input_ven} games Results', 'Stats', [
            [f"Number of at {input_ven} games under {input_gls} goals:", f"{gamesHit['gls_under_ven']} out of {totals['gms_ven']} games"],
            [f"Number of at {input_ven} games over {input_gls} goals:", f"{gamesHit['gls_over_ven']} out of {totals['gms_ven']} games"],
            [f"Percentage of at {input_ven} games under {input_gls} goals:", f"{'N/A' if totals['gms_ven'] == 0 else '{0:.2f}%'.format(percentages['pc_gls_under_ven'] * 100)}"],
            [f"Percentage of at {input_ven} games over {input_gls} goals:", f"{'N/A' if totals['gms_ven'] == 0 else '{0:.2f}%'.format(percentages['pc_gls_over_ven'] * 100)}"],
            [f"True odds for under {input_gls} goals on past {input_ven} performance:", f"{'N/A' if percentages['pc_gls_under_ven'] == 0 or totals['gms_ven'] == 0 else '${0:.2f}'.format(1 / percentages['pc_gls_under_ven'])}"],
            [f"True odds for over {input_gls} goals on past {input_ven} performance:", f"{'N/A' if percentages['pc_gls_over_ven'] == 0 or totals['gms_ven'] == 0 else '${0:.2f}'.format(1 / percentages['pc_gls_over_ven'])}"]
        ]
      ],
      ['Goals in 2023 - Season games Results', 'Stats', [
            [f"Number of 2023 games under {input_gls} goals:", f"{gamesHit['gls_under_2023']} out of {totals['gms_2023']} games"],
            [f"Number of 2023 games over {input_gls} goals:", f"{gamesHit['gls_over_2023']} out of {totals['gms_2023']} games"],
            [f"Percentage of 2023 games under {input_gls} goals:", f"{'N/A' if totals['gms_2023'] == 0 else '{0:.2f}%'.format(percentages['pc_gls_under_2023'] * 100)}"],
            [f"Percentage of 2023 games over {input_gls} goals:", f"{'N/A' if totals['gms_2023'] == 0 else '{0:.2f}%'.format(percentages['pc_gls_over_2023'] * 100)}"],
            [f"True odds for under {input_gls} goals on 2023 performance:", f"{'N/A' if percentages['pc_gls_under_2023'] == 0 or totals['gms_2023'] == 0 else '${0:.2f}'.format(1 / percentages['pc_gls_under_2023'])}"],
            [f"True odds for over {input_gls} goals on 2023 performance:", f"{'N/A' if percentages['pc_gls_over_2023'] == 0 or totals['gms_2023'] == 0 else '${0:.2f}'.format(1 / percentages['pc_gls_over_2023'])}"]
        ]
      ],
      ['Two Leg Combo Results', 'Heading'],
      ["2 LEG COMBO RESULTS - Two Leg Same Game Multi for All Games Requested", 'Stats', [
            [f"Number of games with disposals over {input_di} and goals over {input_gls}:", f"{gamesHit['di_over_gls_over']} out of {totals['gms']} games"],
            [f"Number of games with disposals over {input_di} and goals under {input_gls}:", f"{gamesHit['di_over_gls_under']} out of {totals['gms']} games"],
            [f"Number of games with disposals under {input_di} and goals over {input_gls}:", f"{gamesHit['di_under_gls_over']} out of {totals['gms']} games"],
            [f"Number of games with disposals under {input_di} and goals under {input_gls}:", f"{gamesHit['di_under_gls_under']} out of {totals['gms']} games"],
            [f"Percentage of games with disposals over {input_di} and goals over {input_gls}:", f"{'N/A' if totals['gms'] == 0 else '{0:.2f}%'.format(percentages['pc_di_over_gls_over'] * 100)}"],
            [f"Percentage of games with disposals over {input_di} and goals under {input_gls}:", f"{'N/A' if totals['gms'] == 0 else '{0:.2f}%'.format(percentages['pc_di_over_gls_under'] * 100)}"],
            [f"Percentage of games with disposals under {input_di} and goals over {input_gls}:", f"{'N/A' if totals['gms'] == 0 else '{0:.2f}%'.format(percentages['pc_di_under_gls_over'] * 100)}"],
            [f"Percentage of games with disposals under {input_di} and goals under {input_gls}:", f"{'N/A' if totals['gms'] == 0 else '{0:.2f}%'.format(percentages['pc_di_under_gls_under'] * 100)}"],
            [f"True odds for games with disposals over {input_di} and goals over {input_gls} on past performance:", f"{'N/A' if percentages['pc_di_over_gls_over'] == 0 or totals['gms'] == 0 else '${0:.2f}'.format(1 / percentages['pc_di_over_gls_over'])}"],
            [f"True odds for games with disposals over {input_di} and goals under {input_gls} on past performance:", f"{'N/A' if percentages['pc_di_over_gls_under'] == 0 or totals['gms'] == 0 else '${0:.2f}'.format(1 / percentages['pc_di_over_gls_under'])}"],
            [f"True odds for games with disposals under {input_di} and goals over {input_gls} on past performance:", f"{'N/A' if percentages['pc_di_under_gls_over'] == 0 or totals['gms'] == 0 else '${0:.2f}'.format(1 / percentages['pc_di_under_gls_over'])}"],
            [f"True odds for games with disposals under {input_di} and goals under {input_gls} on past performance:", f"{'N/A' if percentages['pc_di_under_gls_under'] == 0 or totals['gms'] == 0 else '${0:.2f}'.format(1 / percentages['pc_di_under_gls_under'])}"]
        ]
      ],
      [f'Two Leg Same Game Multi by Home or Away - {input_loc} games Results', 'Stats', [
            [f"Number of {input_loc} games with disposals over {input_di} and goals over {input_gls}:", f"{gamesHit['di_over_gls_over_loc']} out of {totals['gms_loc']} games"],
            [f"Number of {input_loc} games with disposals over {input_di} and goals under {input_gls}:", f"{gamesHit['di_over_gls_under_loc']} out of {totals['gms_loc']} games"],
            [f"Number of {input_loc} games with disposals under {input_di} and goals over {input_gls}:", f"{gamesHit['di_under_gls_over_loc']} out of {totals['gms_loc']} games"],
            [f"Number of {input_loc} games with disposals under {input_di} and goals under {input_gls}:", f"{gamesHit['di_under_gls_under_loc']} out of {totals['gms_loc']} games"],
            [f"Percentage of {input_loc} games with disposals over {input_di} and goals over {input_gls}:", f"{'N/A' if totals['gms_loc'] == 0 else '{0:.2f}%'.format(percentages['pc_di_over_gls_over_loc'] * 100)}"],
            [f"Percentage of {input_loc} games with disposals over {input_di} and goals under {input_gls}:", f"{'N/A' if totals['gms_loc'] == 0 else '{0:.2f}%'.format(percentages['pc_di_over_gls_under_loc'] * 100)}"],
            [f"Percentage of {input_loc} games with disposals under {input_di} and goals over {input_gls}:", f"{'N/A' if totals['gms_loc'] == 0 else '{0:.2f}%'.format(percentages['pc_di_under_gls_over_loc'] * 100)}"],
            [f"Percentage of {input_loc} games with disposals under {input_di} and goals under {input_gls}:", f"{'N/A' if totals['gms_loc'] == 0 else '{0:.2f}%'.format(percentages['pc_di_under_gls_under_loc'] * 100)}"],
            [f"True odds for {input_loc} games with disposals over {input_di} and goals over {input_gls} on past performance:", f"{'N/A' if percentages['pc_di_over_gls_over_loc'] == 0 or totals['gms_loc'] == 0 else '${0:.2f}'.format(1 / percentages['pc_di_over_gls_over_loc'])}"],
            [f"True odds for {input_loc} games with disposals over {input_di} and goals under {input_gls} on past performance:", f"{'N/A' if percentages['pc_di_over_gls_under_loc']== 0 or totals['gms_loc'] == 0 else '${0:.2f}'.format(1 / percentages['pc_di_over_gls_under_loc'])}"],
            [f"True odds for {input_loc} games with disposals under {input_di} and goals over {input_gls} on past performance:", f"{'N/A' if percentages['pc_di_under_gls_over_loc'] == 0 or totals['gms_loc'] == 0 else '${0:.2f}'.format(1 / percentages['pc_di_under_gls_over_loc'])}"],
            [f"True odds for {input_loc} games with disposals under {input_di} and goals under {input_gls} on past performance:", f"{'N/A' if percentages['pc_di_under_gls_under_loc'] == 0 or totals['gms_loc'] == 0 else '${0:.2f}'.format(1 / percentages['pc_di_under_gls_under_loc'])}"]
        ]
      ],
      [f'Two Leg Same Game Multi versus Opposition - Against {input_opp} games Results', 'Stats', [
            [f"Number of games against {input_opp} with disposals over {input_di} and goals over {input_gls}:", f"{gamesHit['di_over_gls_over_opp']} out of {totals['gms_opp']} games"],
            [f"Number of games against {input_opp} with disposals over {input_di} and goals under {input_gls}:", f"{gamesHit['di_over_gls_under_opp']} out of {totals['gms_opp']} games"],
            [f"Number of games against {input_opp} with disposals under {input_di} and goals over {input_gls}:", f"{gamesHit['di_under_gls_over_opp']} out of {totals['gms_opp']} games"],
            [f"Number of games against {input_opp} with disposals under {input_di} and goals under {input_gls}:", f"{gamesHit['di_under_gls_under_opp']} out of {totals['gms_opp']} games"],
            [f"Percentage of games against {input_opp} with disposals over {input_di} and goals over {input_gls}:", f"{'N/A' if totals['gms_opp'] == 0 else '{0:.2f}%'.format(percentages['pc_di_over_gls_over_opp'] * 100)}"],
            [f"Percentage of games against {input_opp} with disposals over {input_di} and goals under {input_gls}:", f"{'N/A' if totals['gms_opp'] == 0 else '{0:.2f}%'.format(percentages['pc_di_over_gls_under_opp'] * 100)}"],
            [f"Percentage of games against {input_opp} with disposals under {input_di} and goals over {input_gls}:", f"{'N/A' if totals['gms_opp'] == 0 else '{0:.2f}%'.format(percentages['pc_di_under_gls_over_opp'] * 100)}"],
            [f"Percentage of games against {input_opp} with disposals under {input_di} and goals under {input_gls}:", f"{'N/A' if totals['gms_opp'] == 0 else '{0:.2f}%'.format(percentages['pc_di_under_gls_under_opp'] * 100)}"],
            [f"True odds for games against {input_opp} with disposals over {input_di} and goals over {input_gls} on past performance:", f"{'N/A' if percentages['pc_di_over_gls_over_opp'] == 0 or totals['gms_opp'] == 0 else '${0:.2f}'.format(1 / percentages['pc_di_over_gls_over_opp'])}"],
            [f"True odds for games against {input_opp} with disposals over {input_di} and goals under {input_gls} on past performance:", f"{'N/A' if percentages['pc_di_over_gls_under_opp'] == 0 or totals['gms_opp'] == 0 else '${0:.2f}'.format(1 / percentages['pc_di_over_gls_under_opp'])}"],
            [f"True odds for games against {input_opp} with disposals under {input_di} and goals over {input_gls} on past performance:", f"{'N/A' if percentages['pc_di_under_gls_over_opp'] == 0 or totals['gms_opp'] == 0 else '${0:.2f}'.format(1 / percentages['pc_di_under_gls_over_opp'])}"],
            [f"True odds for games against {input_opp} with disposals under {input_di} and goals under {input_gls} on past performance:", f"{'N/A' if percentages['pc_di_under_gls_under_opp'] == 0 or totals['gms_opp'] == 0 else '${0:.2f}'.format(1 / percentages['pc_di_under_gls_under_opp'])}"]
        ]
      ],
      [f'Two Leg Same Game Multi by Venue - At {input_ven} games Results', 'Stats', [
            [f"Number of {input_ven} games with disposals over {input_di} and goals over {input_gls}:", f"{gamesHit['di_over_gls_over_ven']} out of {totals['gms_ven']} games"],
            [f"Number of {input_ven} games with disposals over {input_di} and goals under {input_gls}:", f"{gamesHit['di_over_gls_under_ven']} out of {totals['gms_ven']} games"],
            [f"Number of {input_ven} games with disposals under {input_di} and goals over {input_gls}:", f"{gamesHit['di_under_gls_over_ven']} out of {totals['gms_ven']} games"],
            [f"Number of {input_ven} games with disposals under {input_di} and goals under {input_gls}:", f"{gamesHit['di_under_gls_under_ven']} out of {totals['gms_ven']} games"],
            [f"Percentage of {input_ven} games with disposals over {input_di} and goals over {input_gls}:", f"{'N/A' if totals['gms_ven'] == 0 else '{0:.2f}%'.format(percentages['pc_di_over_gls_over_ven'] * 100)}"],
            [f"Percentage of {input_ven} games with disposals over {input_di} and goals under {input_gls}:", f"{'N/A' if totals['gms_ven'] == 0 else '{0:.2f}%'.format(percentages['pc_di_over_gls_under_ven'] * 100)}"],
            [f"Percentage of {input_ven} games with disposals under {input_di} and goals over {input_gls}:", f"{'N/A' if totals['gms_ven'] == 0 else '{0:.2f}%'.format(percentages['pc_di_under_gls_over_ven'] * 100)}"],
            [f"Percentage of {input_ven} games with disposals under {input_di} and goals under {input_gls}:", f"{'N/A' if totals['gms_ven'] == 0 else '{0:.2f}%'.format(percentages['pc_di_under_gls_under_ven'] * 100)}"],
            [f"True odds for {input_ven} games with disposals over {input_di} and goals over {input_gls} on past performance:", f"{'N/A' if percentages['pc_di_over_gls_over_ven'] == 0 or totals['gms_ven'] == 0 else '${0:.2f}'.format(1 / percentages['pc_di_over_gls_over_ven'])}"],
            [f"True odds for {input_ven} games with disposals over {input_di} and goals under {input_gls} on past performance:", f"{'N/A' if percentages['pc_di_over_gls_under_ven'] == 0 or totals['gms_ven'] == 0 else '${0:.2f}'.format(1 / percentages['pc_di_over_gls_under_ven'])}"],
            [f"True odds for {input_ven} games with disposals under {input_di} and goals over {input_gls} on past performance:", f"{'N/A' if percentages['pc_di_under_gls_over_ven'] == 0 or totals['gms_ven'] == 0 else '${0:.2f}'.format(1 / percentages['pc_di_under_gls_over_ven'])}"],
            [f"True odds for {input_ven} games with disposals under {input_di} and goals under {input_gls} on past performance:", f"{'N/A' if percentages['pc_di_under_gls_under_ven'] == 0 or totals['gms_ven'] == 0 else '${0:.2f}'.format(1 / percentages['pc_di_under_gls_under_ven'])}"]
        ]
      ],
      ['Two Leg Same Game Multi in 2023 - 2023 Season Results', 'Stats', [
            [f"Number of 2023 season games with disposals over {input_di} and goals over {input_gls}:", f"{gamesHit['di_over_gls_over_2023']} out of {totals['gms_2023']} games"],
            [f"Number of 2023 season games with disposals over {input_di} and goals under {input_gls}:", f"{gamesHit['di_over_gls_under_2023']} out of {totals['gms_2023']} games"],
            [f"Number of 2023 season games with disposals under {input_di} and goals over {input_gls}:", f"{gamesHit['di_under_gls_over_2023']} out of {totals['gms_2023']} games"],
            [f"Number of 2023 season games with disposals under {input_di} and goals under {input_gls}:", f"{gamesHit['di_under_gls_under_2023']} out of {totals['gms_2023']} games"],
            [f"Percentage of 2023 season games with disposals over {input_di} and goals over {input_gls}:", f"{'N/A' if totals['gms_2023'] == 0 else '{0:.2f}%'.format(percentages['pc_di_over_gls_over_2023'] * 100)}"],
            [f"Percentage of 2023 season games with disposals over {input_di} and goals under {input_gls}:", f"{'N/A' if totals['gms_2023'] == 0 else '{0:.2f}%'.format(percentages['pc_di_over_gls_under_2023'] * 100)}"],
            [f"Percentage of 2023 season games with disposals under {input_di} and goals over {input_gls}:", f"{'N/A' if totals['gms_2023'] == 0 else '{0:.2f}%'.format(percentages['pc_di_under_gls_over_2023'] * 100)}"],
            [f"Percentage of 2023 season games with disposals under {input_di} and goals under {input_gls}:", f"{'N/A' if totals['gms_2023'] == 0 else '{0:.2f}%'.format(percentages['pc_di_under_gls_under_2023'] * 100)}"],
            [f"True odds for 2023 season games with disposals over {input_di} and goals over {input_gls} on past performance:", f"{'N/A' if percentages['pc_di_over_gls_over_2023'] == 0 or totals['gms_2023'] == 0 else '${0:.2f}'.format(1 / percentages['pc_di_over_gls_over_2023'])}"],
            [f"True odds for 2023 season games with disposals over {input_di} and goals under {input_gls} on past performance:", f"{'N/A' if percentages['pc_di_over_gls_under_2023'] == 0 or totals['gms_2023'] == 0 else '${0:.2f}'.format(1 / percentages['pc_di_over_gls_under_2023'])}"],
            [f"True odds for 2023 season games with disposals under {input_di} and goals over {input_gls} on past performance:", f"{'N/A' if percentages['pc_di_under_gls_over_2023'] == 0 or totals['gms_2023'] == 0 else '${0:.2f}'.format(1 / percentages['pc_di_under_gls_over_2023'])}"],
            [f"True odds for 2023 season games with disposals under {input_di} and goals under {input_gls} on past performance:", f"{'N/A' if percentages['pc_di_under_gls_under_2023'] == 0 or totals['gms_2023'] == 0 else '${0:.2f}'.format(1 / percentages['pc_di_under_gls_under_2023'])}"]
        ]
      ]
  ]

  return summary
