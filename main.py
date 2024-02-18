import pandas as pd

#User input
input_name = input("Enter the player name: (john/david) ")
print()
input_di = float(input("What is the disposal line?: "))
print()
input_gls = float(input("What is the goal line?: "))
print()
input_loc = input("Is the player at home or away?: (home/away) ")
print()
input_opp = input("Who is the opposition? ")
print()
input_ven = input("What stadium is the game at? ")
print()
input_ssns = int(input("From what season do you want results? (ex: 2021) "))
print()
input_time = input("Is the game night or day? (night/day) ")
print()
input_day = input("What day of the week is the game on? (ex: monday) ")
print()


#read the CSV data into a Dataframe
df = pd.read_csv('test-data-real.csv')

#print dataframe, during testing to see
print(df)
print()


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


#output
print()
print(f"{input_name} results for disposal line of {input_di} and goals line of {input_gls}")
print()

#print results for di
print("Disposals")
print()
print("All gms Results")
print(f"Number of games under {input_di} disposals: {di_under}")
print(f"Number of games over {input_di} disposals: {di_over}")
print(f"percentage of games under {input_di} disposals: {pc_gls_under *100:.2f}%")
print(f"percentage of games over {input_di} disposals: {pc_gls_over *100:.2f}%")
print(f"True odds for under {input_di} disposals on past performance: ${1/pc_di_under:.2f}")
print(f"True odds for over {input_di} disposals on past performance: ${1/pc_di_over:.2f}")
print()

print(f"{input_loc} games Results")
print(f"Number of {input_loc} games under {input_di} disposals: {di_under_loc}")
print(f"Number of {input_loc} games over {input_di} disposals: {di_over_loc}")
print(f"percentage of {input_loc} games under {input_di} disposals: {pc_di_under_loc *100:.2f}%")
print(f"percentage of {input_loc} games over {input_di} disposals: {pc_di_over_loc *100:.2f}%")
print(f"True odds for under {input_di} disposals on past {input_loc} performance: ${1/pc_di_under_loc:.2f}")
print(f"True odds for over {input_di} disposals on past {input_loc} performance: ${1/pc_di_over_loc:.2f}")
print()

print(f"Against {input_opp} games Results")
print(f"Number of games against {input_opp} under {input_di} disposals: {di_under_opp}")
print(f"Number of games against {input_opp} over {input_di} disposals: {di_over_opp}")
print(f"percentage of games against {input_opp} under {input_di} disposals: {pc_di_under_opp * 100:.2f}%")
print(f"percentage of games against {input_opp} over {input_di} disposals: {pc_di_over_opp * 100:.2f}%")
print(f"True odds for under {input_di} disposals on past against {input_opp} performance: ${1 / pc_di_under_opp:.2f}")
print(f"True odds for over {input_di} disposals on past against {input_opp} performance: ${1 / pc_di_over_opp:.2f}")
print()

print(f"At {input_ven} games Results")
print(f"Number of at {input_ven} games under {input_di} disposals: {di_under_ven}")
print(f"Number of at {input_ven} games over {input_di} disposals: {di_over_ven}")
print(f"percentage of at {input_ven} games under {input_di} disposals: {pc_di_under_ven * 100:.2f}%")
print(f"percentage of at {input_ven} games over {input_di} disposals: {pc_di_over_ven * 100:.2f}%")
print(f"True odds for under {input_di} disposals on past at {input_ven} performance: ${1 / pc_di_under_ven:.2f}")
print(f"True odds for over {input_di} disposals on past at {input_ven} performance: ${1 / pc_di_over_ven:.2f}")
print()

print(f"2023 Season games Results")
print(f"Number of 2023 games under {input_di} disposals: {di_under_2023}")
print(f"Number of 2023 games over {input_di} disposals: {di_over_2023}")
print(f"percentage of 2023 games under {input_di} disposals: {pc_di_under_2023 * 100:.2f}%")
print(f"percentage of 2023 games over {input_di} disposals: {pc_di_over_2023 * 100:.2f}%")
print(f"True odds for under {input_di} disposals on 2023 performance: ${1 / pc_di_under_2023:.2f}")
print(f"True odds for over {input_di} disposals on 2023 performance: ${1 / pc_di_over_2023:.2f}")
print()

print(f"{input_time} games Results")
print(f"Number of {input_time} games under {input_di} disposals: {di_under_time}")
print(f"Number of {input_time} games over {input_di} disposals: {di_over_time}")
print(f"percentage of {input_time} games under {input_di} disposals: {pc_di_under_time * 100:.2f}%")
print(f"percentage of {input_time} games over {input_di} disposals: {pc_di_over_time * 100:.2f}%")
print(f"True odds for under {input_di} disposals {input_time} performance: ${1 / pc_di_under_time:.2f}")
print(f"True odds for over {input_di} disposals on {input_time} performance: ${1 / pc_di_over_time:.2f}")
print()

print(f"{input_day} games Results")
print(f"Number of {input_day} games under {input_di} disposals: {di_under_day}")
print(f"Number of {input_day} games over {input_di} disposals: {di_over_day}")
print(f"percentage of {input_day} games under {input_di} disposals: {pc_di_under_day * 100:.2f}%")
print(f"percentage of {input_day} games over {input_di} disposals: {pc_di_over_day * 100:.2f}%")
print(f"True odds for under {input_di} disposals on {input_day} performance: ${1 / pc_di_under_day:.2f}")
print(f"True odds for over {input_di} disposals on {input_day} performance: ${1 / pc_di_over_day:.2f}")
print()
print()

# print results for gls
print("Goals")
print()
print("All games Results")
print(f"Number of games under {input_gls} goals: {gls_under}")
print(f"Number of games over {input_gls} goals: {gls_over}")
print(f"percentage of games under {input_gls} goals: {pc_gls_under *100:.2f}%")
print(f"percentage of games over {input_gls} goals: {pc_gls_over *100:.2f}%")
print(f"True odds for under {input_gls} goals on past performance: ${1/pc_gls_under:.2f}")
print(f"True odds for over {input_gls} goals on past performance: ${1/pc_gls_over:.2f}")
print()

print(f"{input_loc} games Results")
print(f"Number of {input_loc} games under {input_gls} goals: {gls_under_loc}")
print(f"Number of {input_loc} games over {input_gls} goals: {gls_over_loc}")
print(f"percentage of {input_loc} games under {input_gls} goals: {pc_gls_under_loc *100:.2f}%")
print(f"percentage of {input_loc} games over {input_gls} goals: {pc_gls_over_loc *100:.2f}%")
print(f"True odds for under {input_gls} goals on past {input_loc} performance: ${1/pc_gls_under_loc:.2f}")
print(f"True odds for over {input_gls} goals on past {input_loc} performance: ${1/pc_gls_over_loc:.2f}")
print()

print(f"Against {input_opp} games Results")
print(f"Number of games against {input_opp} under {input_gls} goals: {gls_under_opp}")
print(f"Number of games against {input_opp} over {input_gls} goals: {gls_over_opp}")
print(f"percentage of games against {input_opp} under {input_gls} goals: {pc_gls_under_opp * 100:.2f}%")
print(f"percentage of games against {input_opp} over {input_gls} goals: {pc_gls_over_opp * 100:.2f}%")
print(f"True odds for under {input_gls} goals on past against {input_opp} performance: ${1 / pc_gls_under_opp:.2f}")
print(f"True odds for over {input_gls} goals on past against {input_opp} performance: ${1 / pc_gls_over_opp:.2f}")
print()

print(f"At {input_ven} games Results")
print(f"Number of at {input_ven} games under {input_gls} goals: {gls_under_ven}")
print(f"Number of at {input_ven} games over {input_gls} goals: {gls_over_ven}")
print(f"percentage of at {input_ven} games under {input_gls} goals: {pc_gls_under_ven * 100:.2f}%")
print(f"percentage of at {input_ven} games over {input_gls} goals: {pc_gls_over_ven * 100:.2f}%")
print(f"True odds for under {input_gls} goals on past at {input_ven} performance: ${1 / pc_gls_under_ven:.2f}")
print(f"True odds for over {input_gls} goals on past at {input_ven} performance: ${1 / pc_gls_over_ven:.2f}")
print()

print(f"2023 Season games Results")
print(f"Number of 2023 games under {input_gls} goals: {gls_under_2023}")
print(f"Number of 2023 games over {input_gls} goals: {gls_over_2023}")
print(f"percentage of 2023 games under {input_gls} goals: {pc_gls_under_2023 * 100:.2f}%")
print(f"percentage of 2023 games over {input_gls} goals: {pc_gls_over_2023 * 100:.2f}%")
print(f"True odds for under {input_gls} goals on 2023 performance: ${1 / pc_gls_under_2023:.2f}")
print(f"True odds for over {input_gls} goals on 2023 performance: ${1 / pc_gls_over_2023:.2f}")
print()

print(f"{input_time} games Results")
print(f"Number of {input_time} games under {input_gls} goals: {gls_under_time}")
print(f"Number of {input_time} games over {input_gls} goals: {gls_over_time}")
print(f"percentage of {input_time} games under {input_gls} goals: {pc_gls_under_time * 100:.2f}%")
print(f"percentage of {input_time} games over {input_gls} goals: {pc_gls_over_time * 100:.2f}%")
print(f"True odds for under {input_gls} goals on past at night performance: ${1 / pc_gls_under_time:.2f}")
print(f"True odds for over {input_gls} goals on past at night performance: ${1 / pc_gls_over_time:.2f}")
print()

print(f"{input_day} games Results")
print(f"Number of {input_day} games under {input_gls} goals: {gls_under_day}")
print(f"Number of {input_day} games over {input_gls} goals: {gls_over_day}")
print(f"percentage of {input_day} games under {input_gls} goals: {pc_gls_under_day * 100:.2f}%")
print(f"percentage of {input_day} games over {input_gls} goals: {pc_gls_over_day * 100:.2f}%")
print(f"True odds for under {input_gls} goals on past at night performance: ${1 / pc_gls_under_day:.2f}")
print(f"True odds for over {input_gls} goals on past at night performance: ${1 / pc_gls_over_day:.2f}")
print()
print()

# print results for 2 leg combos
print("2 LEG COMBO RESULTS")
print()
print("All games Results")
print(f"Number of games with disposals over {input_di} and goals over {input_gls}: {di_over_gls_over}")
print(f"Number of games with disposals over {input_di} and goals under {input_gls}: {di_over_gls_under}")
print(f"Number of games with disposals under {input_di} and goals over {input_gls}: {di_under_gls_over}")
print(f"Number of games with disposals under {input_di} and goals under {input_gls}: {di_over_gls_under}")
print(f"percentage of games with disposals over {input_di} and goals over {input_gls}: {pc_di_over_gls_over *100:.2f}%")
print(f"percentage of games with disposals over {input_di} and goals under {input_gls}: {pc_di_over_gls_under *100:.2f}%")
print(f"percentage of games with disposals under {input_di} and goals over {input_gls}: {pc_di_under_gls_over *100:.2f}%")
print(f"percentage of games with disposals under {input_di} and goals under {input_gls}: {pc_di_under_gls_under *100:.2f}%")
print(f"True odds for games with disposals over {input_di} and goals over {input_gls} on past performance: ${1/pc_di_over_gls_over:.2f}")
print(f"True odds for games with disposals over {input_di} and goals under {input_gls} on past performance: ${1/pc_di_over_gls_under:.2f}")
print(f"True odds for games with disposals under {input_di} and goals over {input_gls} on past performance: ${1/pc_di_under_gls_over:.2f}")
print(f"True odds for games with disposals under {input_di} and goals under {input_gls} on past performance: ${1/pc_di_under_gls_under:.2f}")
print()

print(f"{input_loc} games Results")
print(f"Number of games with disposals over {input_di} and goals over {input_gls}: {di_over_gls_over_loc}")
print(f"Number of games with disposals over {input_di} and goals under {input_gls}: {di_over_gls_under_loc}")
print(f"Number of games with disposals under {input_di} and goals over {input_gls}: {di_under_gls_over_loc}")
print(f"Number of games with disposals under {input_di} and goals under {input_gls}: {di_under_gls_under_loc}")
print(f"percentage of games with disposals over {input_di} and goals over {input_gls}: {pc_di_over_gls_over_loc *100:.2f}%")
print(f"percentage of games with disposals over {input_di} and goals under {input_gls}: {pc_di_over_gls_under_loc *100:.2f}%")
print(f"percentage of games with disposals under {input_di} and goals over {input_gls}: {pc_di_under_gls_over_loc *100:.2f}%")
print(f"percentage of games with disposals under {input_di} and goals under {input_gls}: {pc_di_under_gls_under_loc *100:.2f}%")
print(f"True odds for games with disposals over {input_di} and goals over {input_gls} on past performance: ${1/pc_di_over_gls_over_loc:.2f}")
print(f"True odds for games with disposals over {input_di} and goals under {input_gls} on past performance: ${1/pc_di_over_gls_under_loc:.2f}")
print(f"True odds for games with disposals under {input_di} and goals over {input_gls} on past performance: ${1/pc_di_under_gls_over_loc:.2f}")
print(f"True odds for games with disposals under {input_di} and goals under {input_gls} on past performance: ${1/pc_di_under_gls_under_loc:.2f}")
print()

print(f"Against {input_opp} games Results")
print(f"Number of games with disposals over {input_di} and goals over {input_gls}: {di_over_gls_over_opp}")
print(f"Number of games with disposals over {input_di} and goals under {input_gls}: {di_over_gls_under_opp}")
print(f"Number of games with disposals under {input_di} and goals over {input_gls}: {di_under_gls_over_opp}")
print(f"Number of games with disposals under {input_di} and goals under {input_gls}: {di_under_gls_under_opp}")
print(f"percentage of games with disposals over {input_di} and goals over {input_gls}: {pc_di_over_gls_over_opp *100:.2f}%")
print(f"percentage of games with disposals over {input_di} and goals under {input_gls}: {pc_di_over_gls_under_opp *100:.2f}%")
print(f"percentage of games with disposals under {input_di} and goals over {input_gls}: {pc_di_under_gls_over_opp *100:.2f}%")
print(f"percentage of games with disposals under {input_di} and goals under {input_gls}: {pc_di_under_gls_under_opp *100:.2f}%")
print(f"True odds for games with disposals over {input_di} and goals over {input_gls} on past performance: ${1/pc_di_over_gls_over_opp:.2f}")
print(f"True odds for games with disposals over {input_di} and goals under {input_gls} on past performance: ${1/pc_di_over_gls_under_opp:.2f}")
print(f"True odds for games with disposals under {input_di} and goals over {input_gls} on past performance: ${1/pc_di_under_gls_over_opp:.2f}")
print(f"True odds for games with disposals under {input_di} and goals under {input_gls} on past performance: ${1/pc_di_under_gls_under_opp:.2f}")
print()

print(f"At {input_ven} games Results")
print(f"Number of games with disposals over {input_di} and goals over {input_gls}: {di_over_gls_over_ven}")
print(f"Number of games with disposals over {input_di} and goals under {input_gls}: {di_over_gls_under_ven}")
print(f"Number of games with disposals under {input_di} and goals over {input_gls}: {di_under_gls_over_ven}")
print(f"Number of games with disposals under {input_di} and goals under {input_gls}: {di_under_gls_under_ven}")
print(f"percentage of games with disposals over {input_di} and goals over {input_gls}: {pc_di_over_gls_over_ven *100:.2f}%")
print(f"percentage of games with disposals over {input_di} and goals under {input_gls}: {pc_di_over_gls_under_ven *100:.2f}%")
print(f"percentage of games with disposals under {input_di} and goals over {input_gls}: {pc_di_under_gls_over_ven *100:.2f}%")
print(f"percentage of games with disposals under {input_di} and goals under {input_gls}: {pc_di_under_gls_under_ven *100:.2f}%")
print(f"True odds for games with disposals over {input_di} and goals over {input_gls} on past performance: ${1/pc_di_over_gls_over_ven:.2f}")
print(f"True odds for games with disposals over {input_di} and goals under {input_gls} on past performance: ${1/pc_di_over_gls_under_ven:.2f}")
print(f"True odds for games with disposals under {input_di} and goals over {input_gls} on past performance: ${1/pc_di_under_gls_over_ven:.2f}")
print(f"True odds for games with disposals under {input_di} and goals under {input_gls} on past performance: ${1/pc_di_under_gls_under_ven:.2f}")
print()

print("2023 Season Results")
print(f"Number of games with disposals over {input_di} and goals over {input_gls}: {di_over_gls_over_2023}")
print(f"Number of games with disposals over {input_di} and goals under {input_gls}: {di_over_gls_under_2023}")
print(f"Number of games with disposals under {input_di} and goals over {input_gls}: {di_under_gls_over_2023}")
print(f"Number of games with disposals under {input_di} and goals under {input_gls}: {di_under_gls_under_2023}")
print(f"percentage of games with disposals over {input_di} and goals over {input_gls}: {pc_di_over_gls_over_2023 *100:.2f}%")
print(f"percentage of games with disposals over {input_di} and goals under {input_gls}: {pc_di_over_gls_under_2023 *100:.2f}%")
print(f"percentage of games with disposals under {input_di} and goals over {input_gls}: {pc_di_under_gls_over_2023 *100:.2f}%")
print(f"percentage of games with disposals under {input_di} and goals under {input_gls}: {pc_di_under_gls_under_2023 *100:.2f}%")
print(f"True odds for games with disposals over {input_di} and goals over {input_gls} on past performance: ${1/pc_di_over_gls_over_2023:.2f}")
print(f"True odds for games with disposals over {input_di} and goals under {input_gls} on past performance: ${1/pc_di_over_gls_under_2023:.2f}")
print(f"True odds for games with disposals under {input_di} and goals over {input_gls} on past performance: ${1/pc_di_under_gls_over_2023:.2f}")
print(f"True odds for games with disposals under {input_di} and goals under {input_gls} on past performance: ${1/pc_di_under_gls_under_2023:.2f}")
print()

print("Time Results")
print(f"Number of games with disposals over {input_di} and goals over {input_gls}: {di_over_gls_over_time}")
print(f"Number of games with disposals over {input_di} and goals under {input_gls}: {di_over_gls_under_time}")
print(f"Number of games with disposals under {input_di} and goals over {input_gls}: {di_under_gls_over_time}")
print(f"Number of games with disposals under {input_di} and goals under {input_gls}: {di_under_gls_under_time}")
print(f"percentage of games with disposals over {input_di} and goals over {input_gls}: {pc_di_over_gls_over_time *100:.2f}%")
print(f"percentage of games with disposals over {input_di} and goals under {input_gls}: {pc_di_over_gls_under_time *100:.2f}%")
print(f"percentage of games with disposals under {input_di} and goals over {input_gls}: {pc_di_under_gls_over_time *100:.2f}%")
print(f"percentage of games with disposals under {input_di} and goals under {input_gls}: {pc_di_under_gls_under_time *100:.2f}%")
print(f"True odds for gms with disposals over {input_di} and goals over {input_gls} on past performance: ${1/pc_di_over_gls_over_time:.2f}")
print(f"True odds for gms with disposals over {input_di} and goals under {input_gls} on past performance: ${1/pc_di_over_gls_under_time:.2f}")
print(f"True odds for gms with disposals under {input_di} and goals over {input_gls} on past performance: ${1/pc_di_under_gls_over_time:.2f}")
print(f"True odds for gms with disposals under {input_di} and goals under {input_gls} on past performance: ${1/pc_di_under_gls_under_time:.2f}")
print()

print("Day of Week Results")
print(f"Number of games with disposals over {input_di} and goals over {input_gls}: {di_over_gls_over_day}")
print(f"Number of games with disposals over {input_di} and goals under {input_gls}: {di_over_gls_under_day}")
print(f"Number of games with disposals under {input_di} and goals over {input_gls}: {di_under_gls_over_day}")
print(f"Number of games with disposals under {input_di} and goals under {input_gls}: {di_under_gls_under_day}")
print(f"percentage of games with disposals over {input_di} and goals over {input_gls}: {pc_di_over_gls_over_day *100:.2f}%")
print(f"percentage of games with disposals over {input_di} and goals under {input_gls}: {pc_di_over_gls_under_day *100:.2f}%")
print(f"percentage of games with disposals under {input_di} and goals over {input_gls}: {pc_di_under_gls_over_day *100:.2f}%")
print(f"percentage of games with disposals under {input_di} and goals under {input_gls}: {pc_di_under_gls_under_day *100:.2f}%")
print(f"True odds for games with disposals over {input_di} and goals over {input_gls} on past performance: ${1/pc_di_over_gls_over_day:.2f}")
print(f"True odds for games with disposals over {input_di} and goals under {input_gls} on past performance: ${1/pc_di_over_gls_under_day:.2f}")
print(f"True odds for games with disposals under {input_di} and goals over {input_gls} on past performance: ${1/pc_di_under_gls_over_day:.2f}")
print(f"True odds for games with disposals under {input_di} and goals under {input_gls} on past performance: ${1/pc_di_under_gls_under_day:.2f}")
print()
print()