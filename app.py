from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Read the CSV data into a DataFrame
df = pd.read_csv('test-data.csv')

# Global variables for form inputs
input_name = None
input_di = None
input_gls = None
input_loc = None
input_opp = None
input_ven = None
input_ssns = None
input_time = None
input_day = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global input_name, input_di, input_gls, input_loc, input_opp, input_ven
    global input_ssns, input_time, input_day
    if request.method == 'POST':
        # Extract data from form
        results = {
            'player_name': request.form.get('player_name'),
            'disposal_line': float(request.form.get('disposal_line')),
            'goal_line': float(request.form.get('goal_line')),
            'location': request.form.get('location'),
            'opposition': request.form.get('opposition'),
            'venue': request.form.get('venue'),
            'season': int(request.form.get('season')),
            'time': request.form.get('time'),
            'day_of_week': request.form.get('day_of_week')
        }
        # Assign variables from results dictionary
        input_name = results['player_name']
        input_di = results['disposal_line']
        input_gls = results['goal_line']
        input_loc = results['location']
        input_opp = results['opposition']
        input_ven = results['venue']
        input_ssns = results['season']
        input_time = results['time']
        input_day = results['day_of_week']

        # Temporary response for debugging
        return "Form submitted successfully"
    else:
        # Render the form template
        return render_template('index.html')


# Read the CSV data into a DataFrame
df = pd.read_csv('test-data.csv')


#functions to analyze the csv
#di
#define function to count over and under of the user input vs disposal line
def count_di(value):
  di_under = df.loc[(df["season"] >= input_ssns) & (df["name"] == input_name) & (df["disposals"] < input_di), "disposals"].count()
  di_over = df.loc[(df["season"] >= input_ssns) & (df["name"] == input_name) & (df["disposals"] > input_di), "disposals"].count()
  return di_under, di_over

#define function for user input loc to count over and under of the user input vs disposal line
def count_di_loc(value):
  di_under_loc = df.loc[(df["location"] == input_loc) &(df["name"] == input_name) &(df["season"] >= input_ssns) &(df["disposals"] < input_di),"disposals"].count()
  di_over_loc = df.loc[(df["location"] == input_loc) &(df["name"] == input_name) &(df["season"] >= input_ssns) &(df["disposals"] > input_di),"disposals"].count()
  return di_under_loc, di_over_loc

#define the function for user input opp to count over and under of the user input vs di line
def count_di_opp(value):
  di_under_opp = df.loc[(df["opposition"] == input_opp) &(df["name"] == input_name) &(df["season"] >= input_ssns) &(df["disposals"] < input_di),"disposals"].count()
  di_over_opp = df.loc[(df["opposition"] == input_opp) & (df["name"] == input_name) & (df["season"] >= input_ssns) & (df["disposals"] > input_di), "disposals"].count()
  return di_under_opp, di_over_opp

#define the function for user input ven to count over and under of the user input vs di line
def count_di_ven(value):
  di_under_ven = df.loc[(df["venue"] == input_ven) & (df["name"] == input_name) & (df["season"] >= input_ssns) & (df["disposals"] < input_di), "disposals"].count()
  di_over_ven = df.loc[(df["venue"] == input_ven) & (df["name"] == input_name) & (df["season"] >= input_ssns) & (df["disposals"] > input_di), "disposals"].count()
  return di_under_ven, di_over_ven

#define the function for user input 2023 ssns to count over and under of the user input vs di line
def count_di_2023(value):
  di_under_2023 = df.loc[(df["season"] == 2023) & (df["name"] == input_name) & (df["disposals"] < input_di), "disposals"].count()
  di_over_2023 = df.loc[(df["season"] == 2023) & (df["name"] == input_name) & (df["disposals"] > input_di), "disposals"].count()
  return di_under_2023, di_over_2023

#define the function for user input time to count over and under of the user input vs di line
def count_di_time(value):
  di_under_time = df.loc[(df["time"] == input_time) & (df["name"] == input_name) & (df["season"] >= input_ssns) & (df["disposals"] < input_di), "disposals"].count()
  di_over_time = df.loc[(df["time"] == input_time) & (df["name"] == input_name) & (df["season"] >= input_ssns) & (df["disposals"] > input_di), "disposals"].count()
  return di_under_time, di_over_time

#define the function for user input day of week to count over and under of the user input vs di line
def count_di_day(value):
  di_under_day = df.loc[(df["dayofweek"] == input_day) & (df["name"] == input_name) & (df["season"] >= input_ssns) & (df["disposals"] < input_di), "disposals"].count()
  di_over_day = df.loc[(df["dayofweek"] == input_day) & (df["name"] == input_name) & (df["season"] >= input_ssns) & (df["disposals"] > input_di), "disposals"].count()
  return di_under_day, di_over_day

#gls
#define function to count over and under of the user input vs gl line
def count_gls(value):
  gls_under = df.loc[(df["season"] >= input_ssns) & (df["goals"] < input_gls), "goals"].count()
  gls_over = df.loc[(df["season"] >= input_ssns) & (df["goals"] > input_gls), "goals"].count()
  return gls_under, gls_over

#define function for user input loc to count over and under of the user input vs gl line
def count_gls_loc(value):
  gls_under_loc = df.loc[(df["location"] == input_loc) & (df["season"] >= input_ssns) & (df["goals"] < input_gls), "goals"].count()
  gls_over_loc = df.loc[(df["location"] == input_loc) & (df["season"] >= input_ssns) & (df["goals"] > input_gls), "goals"].count()
  return gls_under_loc, gls_over_loc

#define the function for user input opp to count over and under of the user input vs gls line
def count_gls_opp(value):
  gls_under_opp = df.loc[(df["opposition"] == input_opp) & (df["season"] >= input_ssns) & (df["goals"] < input_gls), "goals"].count()
  gls_over_opp = df.loc[(df["opposition"] == input_opp) & (df["season"] >= input_ssns) & (df["goals"] > input_gls), "goals"].count()
  return gls_under_opp, gls_over_opp

#define the function for user input ven to count over and under of the user input vs gls line
def count_gls_ven(value):
  gls_under_ven = df.loc[(df["venue"] == input_ven) & (df["season"] >= input_ssns) & (df["goals"] < input_gls), "goals"].count()
  gls_over_ven = df.loc[(df["venue"] == input_ven) & (df["season"] >= input_ssns) & (df["goals"] > input_gls), "goals"].count()
  return gls_under_ven, gls_over_ven

#define the function for user input 2023 ssns to count over and under of the user input vs gls line
def count_gls_2023(value):
  gls_under_2023 = df.loc[(df["season"] == 2023) & (df["goals"] < input_gls), "goals"].count()
  gls_over_2023 = df.loc[(df["season"] == 2023) & (df["goals"] > input_gls), "goals"].count()
  return gls_under_2023, gls_over_2023

#define the function for user input time to count over and under of the user input vs gls line
def count_gls_time(value):
  gls_under_time = df.loc[(df["time"] == input_time) & (df["season"] >= input_ssns) & (df["goals"] < input_gls), "goals"].count()
  gls_over_time = df.loc[(df["time"] == input_time) & (df["season"] >= input_ssns) & (df["goals"] > input_gls), "goals"].count()
  return gls_under_time, gls_over_time

#define the function for user input day of week to count over and under of the user input vs gls line
def count_gls_day(value):
  gls_under_day = df.loc[(df["dayofweek"] == input_day) & (df["season"] >= input_ssns) & (df["goals"] < input_gls), "goals"].count()
  gls_over_day = df.loc[(df["dayofweek"] == input_day) & (df["season"] >= input_ssns) & (df["goals"] > input_gls), "goals"].count()
  return gls_under_day, gls_over_day

#2 leg combos
#define function to count over and under of the user input vs combo of disposal & gl lines.
def count_di_gls(di, gls):
  di_over_gls_over = df.loc[(df["season"] >= input_ssns) & (df["name"] == input_name) & (df["goals"] > input_gls) & (df["disposals"] > input_di), "disposals"].count()
  di_over_gls_under = df.loc[(df["season"] >= input_ssns) & (df["name"] == input_name) & (df["goals"] < input_gls) & (df["disposals"] > input_di), "disposals"].count()
  di_under_gls_over = df.loc[(df["season"] >= input_ssns) & (df["name"] == input_name) & (df["goals"] > input_gls) & (df["disposals"] < input_di), "disposals"].count()
  di_under_gls_under = df.loc[(df["season"] >= input_ssns) & (df["name"] == input_name) & (df["goals"] < input_gls) & (df["disposals"] < input_di), "disposals"].count()
  return di_over_gls_over, di_over_gls_under, di_under_gls_over, di_under_gls_under

#define function for user input loc to count over and under of the user input vs disposal line
def count_di_gls_loc(di, gls):
  di_over_gls_over_loc = df.loc[ (df["season"] >= input_ssns) & (df["name"] == input_name) & (df["location"] == input_loc) & (df["goals"] > input_gls) & (df["disposals"] > input_di), "disposals"].count()
  di_over_gls_under_loc = df.loc[ (df["season"] >= input_ssns) & (df["name"] == input_name) & (df["location"] == input_loc) & (df["goals"] < input_gls) & (df["disposals"] > input_di), "disposals"].count()
  di_under_gls_over_loc = df.loc[ (df["season"] >= input_ssns) & (df["name"] == input_name) & (df["location"] == input_loc) & (df["goals"] > input_gls) & (df["disposals"] < input_di), "disposals"].count()
  di_under_gls_under_loc = df.loc[ (df["season"] >= input_ssns) & (df["name"] == input_name) & (df["location"] == input_loc) & (df["goals"] < input_gls) & (df["disposals"] < input_di), "disposals"].count()
  return di_over_gls_over_loc, di_over_gls_under_loc, di_under_gls_over_loc, di_under_gls_under_loc

#define the function for user input opp to count over and under of the user input vs di line
def count_di_gls_opp(di, gls):
  di_over_gls_over_opp = df.loc[ (df["season"] >= input_ssns) & (df["name"] == input_name) & (df["opposition"] == input_opp) & (df["goals"] > input_gls) & (df["disposals"] > input_di), "disposals"].count()
  di_over_gls_under_opp = df.loc[ (df["season"] >= input_ssns) & (df["name"] == input_name) & (df["opposition"] == input_opp) & (df["goals"] < input_gls) & (df["disposals"] > input_di), "disposals"].count()
  di_under_gls_over_opp = df.loc[ (df["season"] >= input_ssns) & (df["name"] == input_name) & (df["opposition"] == input_opp) & (df["goals"] > input_gls) & (df["disposals"] < input_di), "disposals"].count()
  di_under_gls_under_opp = df.loc[ (df["season"] >= input_ssns) & (df["name"] == input_name) & (df["opposition"] == input_opp) & (df["goals"] < input_gls) & (df["disposals"] < input_di), "disposals"].count()
  return di_over_gls_over_opp, di_over_gls_under_opp, di_under_gls_over_opp, di_under_gls_under_opp

#define the function for user input ven to count over and under of the user input vs di line
def count_di_gls_ven(di, gls):
  di_over_gls_over_ven = df.loc[ (df["season"] >= input_ssns) & (df["name"] == input_name) & (df["venue"] == input_ven) & (df["goals"] > input_gls) & (df["disposals"] > input_di), "disposals"].count()
  di_over_gls_under_ven = df.loc[ (df["season"] >= input_ssns) & (df["name"] == input_name) & (df["venue"] == input_ven) & (df["goals"] < input_gls) & (df["disposals"] > input_di), "disposals"].count()
  di_under_gls_over_ven = df.loc[ (df["season"] >= input_ssns) & (df["name"] == input_name) & (df["venue"] == input_ven) & (df["goals"] > input_gls) & (df["disposals"] < input_di), "disposals"].count()
  di_under_gls_under_ven = df.loc[(df["season"] >= input_ssns) & (df["name"] == input_name) & (df["venue"] == input_ven) & (df["goals"] < input_gls) & (df["disposals"] < input_di), "disposals"].count()
  return di_over_gls_over_ven, di_over_gls_under_ven, di_under_gls_over_ven, di_under_gls_under_ven

#define the function for user input 2023 ssns to count over and under of the user input vs di line
def count_di_gls_2023(di, gls):
  di_over_gls_over_2023 = df.loc[ (df["season"] >= input_ssns) & (df["name"] == input_name) & (df["season"] == 2023) & (df["goals"] > input_gls) & (df["disposals"] > input_di), "disposals"].count()
  di_over_gls_under_2023 = df.loc[ (df["season"] >= input_ssns) & (df["name"] == input_name) & (df["season"] == 2023) & (df["goals"] < input_gls) & (df["disposals"] > input_di), "disposals"].count()
  di_under_gls_over_2023 = df.loc[ (df["season"] >= input_ssns) & (df["name"] == input_name) & (df["season"] == 2023) & (df["goals"] > input_gls) & (df["disposals"] < input_di), "disposals"].count()
  di_under_gls_under_2023 = df.loc[(df["season"] >= input_ssns) &(df["name"] == input_name) &(df["season"] == 2023) &(df["goals"] < input_gls) &(df["disposals"] < input_di),"disposals"].count()
  return di_over_gls_over_2023, di_over_gls_under_2023, di_under_gls_over_2023, di_under_gls_under_2023

#define the function for user input time to count over and under of the user input vs di line
def count_di_gls_time(di, gls):
  di_over_gls_over_time = df.loc[ (df["season"] >= input_ssns) & (df["name"] == input_name) & (df["time"] == input_time) & (df["goals"] > input_gls) & (df["disposals"] > input_di), "disposals"].count()
  di_over_gls_under_time = df.loc[ (df["season"] >= input_ssns) & (df["name"] == input_name) & (df["time"] == input_time) & (df["goals"] < input_gls) & (df["disposals"] > input_di), "disposals"].count()
  di_under_gls_over_time = df.loc[ (df["season"] >= input_ssns) & (df["name"] == input_name) & (df["time"] == input_time) & (df["goals"] > input_gls) & (df["disposals"] < input_di), "disposals"].count()
  di_under_gls_under_time = df.loc[(df["season"] >= input_ssns) &(df["name"] == input_name) &(df["time"] == input_time) & (df["goals"] < input_gls) &(df["disposals"] < input_di),"disposals"].count()
  return di_over_gls_over_time, di_over_gls_under_time, di_under_gls_over_time, di_under_gls_under_time

#define the function for user input day of week to count over and under of the user input vs di line
def count_di_gls_day(di, gls):
  di_over_gls_over_day = df.loc[(df["season"] >= input_ssns) & (df["name"] == input_name) & (df["dayofweek"] == input_day) & (df["goals"] > input_gls) &(df["disposals"] > input_di), "disposals"].count()
  di_over_gls_under_day = df.loc[(df["season"] >= input_ssns) & (df["name"] == input_name) & (df["dayofweek"] == input_day) & (df["goals"] < input_gls) &(df["disposals"] > input_di), "disposals"].count()
  di_under_gls_over_day = df.loc[(df["season"] >= input_ssns) & (df["name"] == input_name) & (df["dayofweek"] == input_day) & (df["goals"] > input_gls) &(df["disposals"] < input_di), "disposals"].count()
  di_under_gls_under_day = df.loc[(df["season"] >= input_ssns) & (df["name"] == input_name) & (df["dayofweek"] == input_day) & (df["goals"] < input_gls) &(df["disposals"] < input_di), "disposals"].count()
  return di_over_gls_over_day, di_over_gls_under_day, di_under_gls_over_day, di_under_gls_under_day


#run the function with the user input vs the data frame of the test data
#di
def perform_analysis():
  di_under, di_over = count_di(input_di)
  di_under_loc, di_over_loc = count_di_loc(input_di)
  di_under_opp, di_over_opp = count_di_opp(input_di)
  di_under_ven, di_over_ven = count_di_ven(input_di)
  di_under_2023, di_over_2023 = count_di_2023(input_di)
  di_under_time, di_over_time = count_di_time(input_di)
  di_under_day, di_over_day = count_di_day(input_di)
  
  #gls
  gls_under, gls_over = count_gls(input_gls)
  gls_under_loc, gls_over_loc = count_gls_loc(input_gls)
  gls_under_opp, gls_over_opp = count_gls_opp(input_gls)
  gls_under_ven, gls_over_ven = count_gls_ven(input_gls)
  gls_under_2023, gls_over_2023 = count_gls_2023(input_gls)
  gls_under_time, gls_over_time = count_gls_time(input_gls)
  gls_under_day, gls_over_day = count_gls_day(input_gls)
  
  #2 LEG COMBOS
  di_over_gls_over, di_over_gls_under, di_under_gls_over, di_under_gls_under = count_di_gls(input_di, input_gls)
  di_over_gls_over_loc, di_over_gls_under_loc, di_under_gls_over_loc, di_under_gls_under_loc = count_di_gls_loc(input_di, input_gls)
  di_over_gls_over_opp, di_over_gls_under_opp, di_under_gls_over_opp, di_under_gls_under_opp = count_di_gls_opp(input_di, input_gls)
  di_over_gls_over_ven, di_over_gls_under_ven, di_under_gls_over_ven, di_under_gls_under_ven = count_di_gls_ven(input_di, input_gls)
  di_over_gls_over_2023, di_over_gls_under_2023, di_under_gls_over_2023, di_under_gls_under_2023 = count_di_gls_2023(input_di, input_gls)
  di_over_gls_over_time, di_over_gls_under_time, di_under_gls_over_time, di_under_gls_under_time = count_di_gls_time(input_di, input_gls)
  di_over_gls_over_day, di_over_gls_under_day, di_under_gls_over_day, di_under_gls_under_day = count_di_gls_day(input_di, input_gls)
  
  
  #give the tot gms for each paramter a name
  #di
  tot_gms = di_under + di_over
  tot_gms_loc = di_under_loc + di_over_loc
  tot_gms_opp = di_under_opp + di_over_opp
  tot_gms_ven = di_under_ven + di_over_ven
  tot_gms_2023 = di_under_2023 + di_over_2023
  tot_gms_time = di_under_time + di_over_time
  tot_gms_day = di_under_day + di_over_day
  
  #gls
  tot_gms = gls_under + gls_over
  tot_gms_loc = gls_under_loc + gls_over_loc
  tot_gms_opp = gls_under_opp + gls_over_opp
  tot_gms_ven = gls_under_ven + gls_over_ven
  tot_gms_2023 = gls_under_2023 + gls_over_2023
  tot_gms_time = gls_under_time + gls_over_time
  tot_gms_day = gls_under_day + gls_over_day
  
  #2 leg combos
  tot_gms_di_gls = di_over_gls_over + di_over_gls_under + di_under_gls_over + di_under_gls_under
  tot_gms_di_gls_loc = di_over_gls_over_loc + di_over_gls_under_loc + di_under_gls_over_loc + di_under_gls_under_loc
  tot_gms_di_gls_opp = di_over_gls_over_opp + di_over_gls_under_opp + di_under_gls_over_opp + di_under_gls_under_opp
  tot_gms_di_gls_ven = di_over_gls_over_ven + di_over_gls_under_ven + di_under_gls_over_ven + di_under_gls_under_ven
  tot_gms_di_gls_2023 = di_over_gls_over_2023 + di_over_gls_under_2023 + di_under_gls_over_2023 + di_under_gls_under_2023
  tot_gms_di_gls_time = di_over_gls_over_time + di_over_gls_under_time + di_under_gls_over_time + di_under_gls_under_time
  tot_gms_di_gls_day = di_over_gls_over_day + di_over_gls_under_day + di_under_gls_over_day + di_under_gls_under_day
  
  
  #create variables for the pcs of each parameter
  #di
  pc_di_under = di_under / tot_gms
  pc_di_over = di_over / tot_gms
  pc_di_under_loc = di_under_loc / tot_gms_loc
  pc_di_over_loc = di_over_loc / tot_gms_loc
  pc_di_under_opp = di_under_opp / tot_gms_opp
  pc_di_over_opp = di_over_opp / tot_gms_opp
  pc_di_under_ven = di_under_ven / tot_gms_ven
  pc_di_over_ven = di_over_ven / tot_gms_ven
  pc_di_under_2023 = di_under_2023 / tot_gms_2023
  pc_di_over_2023 = di_over_2023 / tot_gms_2023
  pc_di_under_time = di_under_time / tot_gms_time
  pc_di_over_time = di_over_time / tot_gms_time
  pc_di_under_day = di_under_day / tot_gms_day
  pc_di_over_day = di_over_day / tot_gms_day
  
  #gls
  pc_gls_under = gls_under / tot_gms
  pc_gls_over = gls_over / tot_gms
  pc_gls_under_loc = gls_under_loc / tot_gms_loc
  pc_gls_over_loc = gls_over_loc / tot_gms_loc
  pc_gls_under_opp = gls_under_opp / tot_gms_opp
  pc_gls_over_opp = gls_over_opp / tot_gms_opp
  pc_gls_under_ven = gls_under_ven / tot_gms_ven
  pc_gls_over_ven = gls_over_ven / tot_gms_ven
  pc_gls_under_2023 = gls_under_2023 / tot_gms_2023
  pc_gls_over_2023 = gls_over_2023 / tot_gms_2023
  pc_gls_under_time = gls_under_time / tot_gms_time
  pc_gls_over_time = gls_over_time / tot_gms_time
  pc_gls_under_day = gls_under_day / tot_gms_day
  pc_gls_over_day = gls_over_day / tot_gms_day
  
  #2 leg combos
  pc_di_over_gls_over = (di_over_gls_over / tot_gms_di_gls)
  pc_di_over_gls_under = (di_over_gls_under / tot_gms_di_gls)
  pc_di_under_gls_over = (di_under_gls_over / tot_gms_di_gls)
  pc_di_under_gls_under = (di_under_gls_under / tot_gms_di_gls)
  pc_di_over_gls_over_loc = ( di_over_gls_over_loc / tot_gms_di_gls_loc)
  pc_di_over_gls_under_loc = (di_over_gls_under_loc / tot_gms_di_gls_loc)
  pc_di_under_gls_over_loc = (di_under_gls_over_loc / tot_gms_di_gls_loc)
  pc_di_under_gls_under_loc = (di_under_gls_under_loc / tot_gms_di_gls_loc)
  pc_di_over_gls_over_opp = (di_over_gls_over_opp / tot_gms_di_gls_opp)
  pc_di_over_gls_under_opp = (di_over_gls_under_opp / tot_gms_di_gls_opp)
  pc_di_under_gls_over_opp = (di_under_gls_over_opp / tot_gms_di_gls_opp)
  pc_di_under_gls_under_opp = (di_under_gls_under_opp /tot_gms_di_gls_opp)
  pc_di_over_gls_over_ven = (di_over_gls_over_ven / tot_gms_di_gls_ven)
  pc_di_over_gls_under_ven = (di_over_gls_under_ven / tot_gms_di_gls_ven)
  pc_di_under_gls_over_ven = (di_under_gls_over_ven / tot_gms_di_gls_ven)
  pc_di_under_gls_under_ven = (di_under_gls_under_ven / tot_gms_di_gls_ven)
  pc_di_over_gls_over_2023 = (di_over_gls_over_2023 / tot_gms_di_gls_2023)
  pc_di_over_gls_under_2023 = (di_over_gls_under_2023 / tot_gms_di_gls_2023)
  pc_di_under_gls_over_2023 = (di_under_gls_over_2023 / tot_gms_di_gls_2023)
  pc_di_under_gls_under_2023 = (di_under_gls_under_2023 / tot_gms_di_gls_2023)
  pc_di_over_gls_over_time = (di_over_gls_over_time / tot_gms_di_gls_time)
  pc_di_over_gls_under_time = (di_over_gls_under_time / tot_gms_di_gls_time)
  pc_di_under_gls_over_time = (di_under_gls_over_time / tot_gms_di_gls_time)
  pc_di_under_gls_under_time = (di_under_gls_under_time / tot_gms_di_gls_time)
  pc_di_over_gls_over_day = (di_over_gls_over_day / tot_gms_di_gls_day)
  pc_di_over_gls_under_day = (di_over_gls_under_day / tot_gms_di_gls_day)
  pc_di_under_gls_over_day = (di_under_gls_over_day / tot_gms_di_gls_day)
  pc_di_under_gls_under_day = (di_under_gls_under_day / tot_gms_di_gls_day)


# return the variables that appear in print in main.py and also appear in def perform_analysis()  

# Instead of a temporary response, pass the results to a template
# return render_template('results.html', ...)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=8080)

