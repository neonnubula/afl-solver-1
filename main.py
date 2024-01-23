# next major task is to add name selecton

# required libraries
import pandas as pd

# get the input from the user
# player name
input_name = input("Enter the player name: (john/david) ")
print()
# disposal line
input_disposals = float(input("What is the disposal line?: "))
print()
# goal line
input_goals = float(input("What is the goal line?: "))
print()
# location
input_location = input("Is the player at home or away?: (home/away) ")
print()
# opposition
input_opposition = input("Who is the opposition? ")
print()
# venue
input_venue = input("What stadium is the game at? ")
print()
# seasons for all results to be based off
# games since and including seasons
input_seasons = int(input("From what season do you want results? (ex: 2021) "))
print()
# input for day or night game
input_time = input("Is the game night or day? (night/day) ")
print()
# input for day of week
input_dayofweek = input("What day of the week is the game on? (ex: monday) ")
print()

# read the CSV data into a Dataframe
df = pd.read_csv('test-data.csv')

# print the dataframe, during testing to see
print(df)
print()


# functions to analyze the csv
# DISPOSALS
# define function to count greater than and less than of the user input vs disposal line
def count_disposals(value):
  disposals_less = df.loc[(df["season"] >= input_seasons) &
                          (df["name"] == input_name) &
                          (df["disposals"] < input_disposals),
                          "disposals"].count()
  disposals_greater = df.loc[(df["season"] >= input_seasons) &
                             (df["name"] == input_name) &
                             (df["disposals"] > input_disposals),
                             "disposals"].count()
  return disposals_less, disposals_greater


# define function for user input location to count greater and less than of the user input vs disposal line
def count_disposals_location(value):
  disposals_less_location = df.loc[(df["location"] == input_location) &
                                   (df["name"] == input_name) &
                                   (df["season"] >= input_seasons) &
                                   (df["disposals"] < input_disposals),
                                   "disposals"].count()
  disposals_greater_location = df.loc[(df["location"] == input_location) &
                                      (df["name"] == input_name) &
                                      (df["season"] >= input_seasons) &
                                      (df["disposals"] > input_disposals),
                                      "disposals"].count()
  return disposals_less_location, disposals_greater_location


# define the function for user input opposition to count greater than and less than of the user input vs disposals line
def count_disposals_opposition(value):
  disposals_less_opposition = df.loc[(df["opposition"] == input_opposition) &
                                     (df["name"] == input_name) &
                                     (df["season"] >= input_seasons) &
                                     (df["disposals"] < input_disposals),
                                     "disposals"].count()
  disposals_greater_opposition = df.loc[(df["opposition"] == input_opposition)
                                        & (df["name"] == input_name) &
                                        (df["season"] >= input_seasons) &
                                        (df["disposals"] > input_disposals),
                                        "disposals"].count()
  return disposals_less_opposition, disposals_greater_opposition


# define the function for user input venue to count greater than and less than of the user input vs disposals line
def count_disposals_venue(value):
  disposals_less_venue = df.loc[(df["venue"] == input_venue) &
                                (df["name"] == input_name) &
                                (df["season"] >= input_seasons) &
                                (df["disposals"] < input_disposals),
                                "disposals"].count()
  disposals_greater_venue = df.loc[(df["venue"] == input_venue) &
                                   (df["name"] == input_name) &
                                   (df["season"] >= input_seasons) &
                                   (df["disposals"] > input_disposals),
                                   "disposals"].count()
  return disposals_less_venue, disposals_greater_venue


# define the function for user input 2023 season to count greater than and less than of the user input vs disposals line
def count_disposals_2023(value):
  disposals_less_2023 = df.loc[(df["season"] == 2023) &
                               (df["name"] == input_name) &
                               (df["disposals"] < input_disposals),
                               "disposals"].count()
  disposals_greater_2023 = df.loc[(df["season"] == 2023) &
                                  (df["name"] == input_name) &
                                  (df["disposals"] > input_disposals),
                                  "disposals"].count()
  return disposals_less_2023, disposals_greater_2023


# define the function for user input time to count greater than and less than of the user input vs disposals line
def count_disposals_time(value):
  disposals_less_time = df.loc[(df["time"] == input_time) &
                               (df["name"] == input_name) &
                               (df["season"] >= input_seasons) &
                               (df["disposals"] < input_disposals),
                               "disposals"].count()
  disposals_greater_time = df.loc[(df["time"] == input_time) &
                                  (df["name"] == input_name) &
                                  (df["season"] >= input_seasons) &
                                  (df["disposals"] > input_disposals),
                                  "disposals"].count()
  return disposals_less_time, disposals_greater_time


# define the function for user input day of week to count greater than and less than of the user input vs disposals line
def count_disposals_dayofweek(value):
  disposals_less_dayofweek = df.loc[(df["dayofweek"] == input_dayofweek) &
                                    (df["name"] == input_name) &
                                    (df["season"] >= input_seasons) &
                                    (df["disposals"] < input_disposals),
                                    "disposals"].count()
  disposals_greater_dayofweek = df.loc[(df["dayofweek"] == input_dayofweek) &
                                       (df["name"] == input_name) &
                                       (df["season"] >= input_seasons) &
                                       (df["disposals"] > input_disposals),
                                       "disposals"].count()
  return disposals_less_dayofweek, disposals_greater_dayofweek


# GOALS
# define function to count greater than and less than of the user input vs goal line
def count_goals(value):
  goals_less = df.loc[(df["season"] >= input_seasons) &
                      (df["goals"] < input_goals), "goals"].count()
  goals_greater = df.loc[(df["season"] >= input_seasons) &
                         (df["goals"] > input_goals), "goals"].count()
  return goals_less, goals_greater


# define function for user input location to count greater and less than of the user input vs goal line
def count_goals_location(value):
  goals_less_location = df.loc[(df["location"] == input_location) &
                               (df["season"] >= input_seasons) &
                               (df["goals"] < input_goals), "goals"].count()
  goals_greater_location = df.loc[(df["location"] == input_location) &
                                  (df["season"] >= input_seasons) &
                                  (df["goals"] > input_goals),
                                  "goals"].count()
  return goals_less_location, goals_greater_location


# define the function for user input opposition to count greater than and less than of the user input vs goals line
def count_goals_opposition(value):
  goals_less_opposition = df.loc[(df["opposition"] == input_opposition) &
                                 (df["season"] >= input_seasons) &
                                 (df["goals"] < input_goals), "goals"].count()
  goals_greater_opposition = df.loc[(df["opposition"] == input_opposition) &
                                    (df["season"] >= input_seasons) &
                                    (df["goals"] > input_goals),
                                    "goals"].count()
  return goals_less_opposition, goals_greater_opposition


# define the function for user input venue to count greater than and less than of the user input vs goals line
def count_goals_venue(value):
  goals_less_venue = df.loc[(df["venue"] == input_venue) &
                            (df["season"] >= input_seasons) &
                            (df["goals"] < input_goals), "goals"].count()
  goals_greater_venue = df.loc[(df["venue"] == input_venue) &
                               (df["season"] >= input_seasons) &
                               (df["goals"] > input_goals), "goals"].count()
  return goals_less_venue, goals_greater_venue


# define the function for user input 2023 season to count greater than and less than of the user input vs goals line
def count_goals_2023(value):
  goals_less_2023 = df.loc[(df["season"] == 2023) &
                           (df["goals"] < input_goals), "goals"].count()
  goals_greater_2023 = df.loc[(df["season"] == 2023) &
                              (df["goals"] > input_goals), "goals"].count()
  return goals_less_2023, goals_greater_2023


# define the function for user input time to count greater than and less than of the user input vs goals line
def count_goals_time(value):
  goals_less_time = df.loc[(df["time"] == input_time) &
                           (df["season"] >= input_seasons) &
                           (df["goals"] < input_goals), "goals"].count()
  goals_greater_time = df.loc[(df["time"] == input_time) &
                              (df["season"] >= input_seasons) &
                              (df["goals"] > input_goals), "goals"].count()
  return goals_less_time, goals_greater_time


# define the function for user input day of week to count greater than and less than of the user input vs goals line
def count_goals_dayofweek(value):
  goals_less_dayofweek = df.loc[(df["dayofweek"] == input_dayofweek) &
                                (df["season"] >= input_seasons) &
                                (df["goals"] < input_goals), "goals"].count()
  goals_greater_dayofweek = df.loc[(df["dayofweek"] == input_dayofweek) &
                                   (df["season"] >= input_seasons) &
                                   (df["goals"] > input_goals),
                                   "goals"].count()
  return goals_less_dayofweek, goals_greater_dayofweek


# COMBOS - 2 LEGS
# define function to count greater than and less than of the user input vs combo of disposal & goal lines.

# run the function with the user input vs the data frame of the test data
# DISPOSALS
# all games
disposals_less, disposals_greater = count_disposals(input_disposals)
# location
disposals_less_location, disposals_greater_location = count_disposals_location(
    input_disposals)
# opposition
disposals_less_opposition, disposals_greater_opposition = count_disposals_opposition(
    input_disposals)
# venue
disposals_less_venue, disposals_greater_venue = count_disposals_venue(
    input_disposals)
# 2023 season
disposals_less_2023, disposals_greater_2023 = count_disposals_2023(
    input_disposals)
#  time
disposals_less_time, disposals_greater_time = count_disposals_time(
    input_disposals)
# dayofweek
disposals_less_dayofweek, disposals_greater_dayofweek = count_disposals_dayofweek(
    input_disposals)

# GOALS
# all games
goals_less, goals_greater = count_goals(input_goals)
# location
goals_less_location, goals_greater_location = count_goals_location(input_goals)
# opposition
goals_less_opposition, goals_greater_opposition = count_goals_opposition(
    input_goals)
# venue
goals_less_venue, goals_greater_venue = count_goals_venue(input_goals)
# 2023 season
goals_less_2023, goals_greater_2023 = count_goals_2023(input_goals)
#  time
goals_less_time, goals_greater_time = count_goals_time(input_goals)
# dayofweek
goals_less_dayofweek, goals_greater_dayofweek = count_goals_dayofweek(
    input_goals)

# COMBOS - 2 LEGS

# give the total games for each paramter a name
# DISPOSALS
# all games
total_games = disposals_less + disposals_greater
# location
total_games_location = disposals_less_location + disposals_greater_location
# opposition
total_games_opposition = disposals_less_opposition + disposals_greater_opposition
# venue
total_games_venue = disposals_less_venue + disposals_greater_venue
# 2023 season
total_games_2023 = disposals_less_2023 + disposals_greater_2023
# time games
total_games_time = disposals_less_time + disposals_greater_time
# dayofweek
total_games_dayofweek = disposals_less_dayofweek + disposals_greater_dayofweek

# GOALS
# all games
total_games = goals_less + goals_greater
# location
total_games_location = goals_less_location + goals_greater_location
# opposition
total_games_opposition = goals_less_opposition + goals_greater_opposition
# venue
total_games_venue = goals_less_venue + goals_greater_venue
# 2023 season
total_games_2023 = goals_less_2023 + goals_greater_2023
# time games
total_games_time = goals_less_time + goals_greater_time
# dayofweek
total_games_dayofweek = goals_less_dayofweek + goals_greater_dayofweek

# create variables for the percentages of each parameter
# DISPOSALS
# all games
percentage_disposals_less = disposals_less / total_games
percentage_disposals_greater = disposals_greater / total_games
# location
percentage_disposals_less_location = disposals_less_location / total_games_location
percentage_disposals_greater_location = disposals_greater_location / total_games_location
# opposition
percentage_disposals_less_opposition = disposals_less_opposition / total_games_opposition
percentage_disposals_greater_opposition = disposals_greater_opposition / total_games_opposition
# venue
percentage_disposals_less_venue = disposals_less_venue / total_games_venue
percentage_disposals_greater_venue = disposals_greater_venue / total_games_venue
# 2023 season
percentage_disposals_less_2023 = disposals_less_2023 / total_games_2023
percentage_disposals_greater_2023 = disposals_greater_2023 / total_games_2023
# time
percentage_disposals_less_time = disposals_less_time / total_games_time
percentage_disposals_greater_time = disposals_greater_time / total_games_time
# dayofweek
percentage_disposals_less_dayofweek = disposals_less_dayofweek / total_games_dayofweek
percentage_disposals_greater_dayofweek = disposals_greater_dayofweek / total_games_dayofweek

# GOALS
# all games
percentage_goals_less = goals_less / total_games
percentage_goals_greater = goals_greater / total_games
# location
percentage_goals_less_location = goals_less_location / total_games_location
percentage_goals_greater_location = goals_greater_location / total_games_location
# opposition
percentage_goals_less_opposition = goals_less_opposition / total_games_opposition
percentage_goals_greater_opposition = goals_greater_opposition / total_games_opposition
# venue
percentage_goals_less_venue = goals_less_venue / total_games_venue
percentage_goals_greater_venue = goals_greater_venue / total_games_venue
# 2023 season
percentage_goals_less_2023 = goals_less_2023 / total_games_2023
percentage_goals_greater_2023 = goals_greater_2023 / total_games_2023
# time
percentage_goals_less_time = goals_less_time / total_games_time
percentage_goals_greater_time = goals_greater_time / total_games_time
# dayofweek
percentage_goals_less_dayofweek = goals_less_dayofweek / total_games_dayofweek
percentage_goals_greater_dayofweek = goals_greater_dayofweek / total_games_dayofweek

print()
print()
print(
    f"{input_name} results for disposal line of {input_disposals} and goals line of {input_goals}"
)
print()
# print results for DISPOSALS
print("DISPOSALS")
# print the all games results, rounded to 2 decimal points (:.2f)
# IMPORATNT - UPDATE PERCETNAGE VARIABLES
print("All Games Results")
print(
    f"Number of games less than {input_disposals} disposals: {disposals_less}")
print()
print(
    f"Number of games greater than {input_disposals} disposals: {disposals_greater}"
)
print()
print(
    f"Percentage of games less than {input_disposals} disposals: {goal_less_perc *100:.2f}%"
)
print()
print(
    f"Percentage of games greater than {input_disposals} disposals: {goal_greater_perc *100:.2f}%"
)
print()
print(
    f"True odds for under {input_disposals} disposals based on past performance: ${1/disp_less_perc:.2f}"
)
print()
print(
    f"True odds for over {input_disposals} disposals based on past performance: ${1/disp_greater_perc:.2f}"
)
print()
print()

# print the results, based on location input
# IMPORATNT - UPDATE PERCETNAGE VARIABLES

print(f"{input_location} Games Results")
print(
    f"Number of {input_location} games less than {input_disposals} disposals: {disposals_less_location}"
)
print()
print(
    f"Number of {input_location} games greater than {input_disposals} disposals: {disposals_greater_location}"
)
print()
print(
    f"Percentage of {input_location} games less than {input_disposals} disposals: {disp_less_perc_location *100:.2f}%"
)
print()
print(
    f"Percentage of {input_location} games greater than {input_disposals} disposals: {disp_greater_perc_location *100:.2f}%"
)
print()
print(
    f"True odds for under {input_disposals} disposals based on past {input_location} performance: ${1/disp_less_perc_location:.2f}"
)
print()
print(
    f"True odds for over {input_disposals} disposals based on past {input_location} performance: ${1/disp_greater_perc_location:.2f}"
)
print()
print()

# print the results, based on opposition
# IMPORATNT - UPDATE PERCETNAGE VARIABLES

print(f"Against {input_opposition} Games Results")
print(
    f"Number of against {input_opposition} games less than {input_disposals} disposals: {disposals_less_opposition}"
)
print()
print(
    f"Number of against {input_opposition} games greater than {input_disposals} disposals: {disposals_greater_opposition}"
)
print()
print(
    f"Percentage of against {input_opposition} games less than {input_disposals} disposals: {disp_less_perc_opposition *100:.2f}%"
)
print()
print(
    f"Percentage of against {input_opposition} games greater than {input_disposals} disposals: {disp_greater_perc_opposition *100:.2f}%"
)
print()
print(
    f"True odds for under {input_disposals} disposals based on past against {input_opposition} performance: ${1/disp_less_perc_opposition:.2f}"
)
print()
print(
    f"True odds for over {input_disposals} disposals based on past against {input_opposition} performance: ${1/disp_greater_perc_opposition:.2f}"
)
print()
print()

# print the results, based on venue
# IMPORATNT - UPDATE PERCETNAGE VARIABLES

print(f"At {input_venue} Games Results")
print(
    f"Number of at {input_venue} games less than {input_disposals} disposals: {disposals_less_venue}"
)
print()
print(
    f"Number of at {input_venue} games greater than {input_disposals} disposals: {disposals_greater_venue}"
)
print()
print(
    f"Percentage of at {input_venue} games less than {input_disposals} disposals: {disp_less_perc_venue *100:.2f}%"
)
print()
print(
    f"Percentage of at {input_venue} games greater than {input_disposals} disposals: {disp_greater_perc_venue *100:.2f}%"
)
print()
print(
    f"True odds for under {input_disposals} disposals based on past at {input_venue} performance: ${1/disp_less_perc_venue:.2f}"
)
print()
print(
    f"True odds for over {input_disposals} disposals based on past at {input_venue} performance: ${1/disp_greater_perc_venue:.2f}"
)
print()
print()

# print the results, based on 2023 season
# IMPORATNT - UPDATE PERCETNAGE VARIABLES

print(f"2023 Season Games Results")
print(
    f"Number of 2023 games less than {input_disposals} disposals: {disposals_less_2023}"
)
print()
print(
    f"Number of 2023 games greater than {input_disposals} disposals: {disposals_greater_2023}"
)
print()
print(
    f"Percentage of 2023 games less than {input_disposals} disposals: {disp_less_perc_2023 *100:.2f}%"
)
print()
print(
    f"Percentage of 2023 games greater than {input_disposals} disposals: {disp_greater_perc_2023 *100:.2f}%"
)
print()
print(
    f"True odds for under {input_disposals} disposals based 2023 performance: ${1/disp_less_perc_2023:.2f}"
)
print()
print(
    f"True odds for over {input_disposals} disposals based on 2023 performance: ${1/disp_greater_perc_2023:.2f}"
)
print()
print()

# print the results, based on time
# IMPORATNT - UPDATE PERCETNAGE VARIABLES

print(f"{input_time} Games Results")
print(
    f"Number of {input_time} games less than {input_disposals} disposals: {disposals_less_time}"
)
print()
print(
    f"Number of {input_time} games greater than {input_disposals} disposals: {disposals_greater_time}"
)
print()
print(
    f"Percentage of {input_time} games less than {input_disposals} disposals: {disp_less_perc_time *100:.2f}%"
)
print()
print(
    f"Percentage of {input_time} games greater than {input_disposals} disposals: {disp_greater_perc_time *100:.2f}%"
)
print()
print(
    f"True odds for under {input_disposals} disposals based {input_time} performance: ${1/disp_less_perc_time:.2f}"
)
print()
print(
    f"True odds for over {input_disposals} disposals based on {input_time} performance: ${1/disp_greater_perc_time:.2f}"
)
print()
print()

# print the results, based on day of week
# IMPORATNT - UPDATE PERCETNAGE VARIABLES

print(f"{input_dayofweek} Games Results")
print(
    f"Number of {input_dayofweek} games less than {input_disposals} disposals: {disposals_less_dayofweek}"
)
print()
print(
    f"Number of {input_dayofweek} games greater than {input_disposals} disposals: {disposals_greater_dayofweek}"
)
print()
print(
    f"Percentage of {input_dayofweek} games less than {input_disposals} disposals: {disp_less_perc_dayofweek *100:.2f}%"
)
print()
print(
    f"Percentage of {input_dayofweek} games greater than {input_disposals} disposals: {disp_greater_perc_dayofweek *100:.2f}%"
)
print()
print(
    f"True odds for under {input_disposals} disposals based {input_dayofweek} performance: ${1/disp_less_perc_dayofweek:.2f}"
)
print()
print(
    f"True odds for over {input_disposals} disposals based on {input_dayofweek} performance: ${1/disp_greater_perc_dayofweek:.2f}"
)
print()
print()

# print results for GOALS
print("GOALS")
# print the full results, rounded to 2 decimal points (:.2f)
# IMPORATNT - UPDATE PERCETNAGE VARIABLES

print("All Games Results")
print(f"Number of games less than {input_goals} goals: {goals_less}")
print()
print(f"Number of games greater than {input_goals} goals: {goals_greater}")
print()
print(
    f"Percentage of games less than {input_goals} goals: {goal_less_perc *100:.2f}%"
)
print()
print(
    f"Percentage of games greater than {input_goals} goals: {goal_greater_perc *100:.2f}%"
)
print()
print(
    f"True odds for under {input_goals} goals based on past performance: ${1/goal_less_perc:.2f}"
)
print()
print(
    f"True odds for over {input_goals} goals based on past performance: ${1/goal_greater_perc:.2f}"
)
print()
print()

# print the results, based on location input
# IMPORATNT - UPDATE PERCETNAGE VARIABLES

print(f"{input_location} Games Results")
print(
    f"Number of {input_location} games less than {input_goals} goals: {goals_less_location}"
)
print()
print(
    f"Number of {input_location} games greater than {input_goals} goals: {goals_greater_location}"
)
print()
print(
    f"Percentage of {input_location} games less than {input_goals} goals: {goal_less_perc_location *100:.2f}%"
)
print()
print(
    f"Percentage of {input_location} games greater than {input_goals} goals: {goal_greater_perc_location *100:.2f}%"
)
print()
print(
    f"True odds for under {input_goals} goals based on past {input_location} performance: ${1/goal_less_perc_location:.2f}"
)
print()
print(
    f"True odds for over {input_goals} goals based on past {input_location} performance: ${1/goal_greater_perc_location:.2f}"
)
print()
print()

# print the results, based on opposition
# IMPORATNT - UPDATE PERCETNAGE VARIABLES

print(f"Against {input_opposition} Games Results")
print(
    f"Number of against {input_opposition} games less than {input_goals} goals: {goals_less_opposition}"
)
print()
print(
    f"Number of against {input_opposition} games greater than {input_goals} goals: {goals_greater_opposition}"
)
print()
print(
    f"Percentage of against {input_opposition} games less than {input_goals} goals: {goal_less_perc_opposition *100:.2f}%"
)
print()
print(
    f"Percentage of against {input_opposition} games greater than {input_goals} goals: {goal_greater_perc_opposition *100:.2f}%"
)
print()
print(
    f"True odds for under {input_goals} goals based on past against {input_opposition} performance: ${1/goal_less_perc_opposition:.2f}"
)
print()
print(
    f"True odds for over {input_goals} goals based on past against {input_opposition} performance: ${1/goal_greater_perc_opposition:.2f}"
)
print()
print()

# print the results, based on venue
# IMPORATNT - UPDATE PERCETNAGE VARIABLES

print(f"At {input_venue} Games Results")
print(
    f"Number of at {input_venue} games less than {input_goals} goals: {goals_less_venue}"
)
print()
print(
    f"Number of at {input_venue} games greater than {input_goals} goals: {goals_greater_venue}"
)
print()
print(
    f"Percentage of at {input_venue} games less than {input_goals} goals: {goal_less_perc_venue *100:.2f}%"
)
print()
print(
    f"Percentage of at {input_venue} games greater than {input_goals} goals: {goal_greater_perc_venue *100:.2f}%"
)
print()
print(
    f"True odds for under {input_goals} goals based on past at {input_venue} performance: ${1/goal_less_perc_venue:.2f}"
)
print()
print(
    f"True odds for over {input_goals} goals based on past at {input_venue} performance: ${1/goal_greater_perc_venue:.2f}"
)
print()
print()

# print the results, based on 2023 season
# IMPORATNT - UPDATE PERCETNAGE VARIABLES

print(f"2023 Season Games Results")
print(f"Number of 2023 games less than {input_goals} goals: {goals_less_2023}")
print()
print(
    f"Number of 2023 games greater than {input_goals} goals: {goals_greater_2023}"
)
print()
print(
    f"Percentage of 2023 games less than {input_goals} goals: {goal_less_perc_2023 *100:.2f}%"
)
print()
print(
    f"Percentage of 2023 games greater than {input_goals} goals: {goal_greater_perc_2023 *100:.2f}%"
)
print()
print(
    f"True odds for under {input_goals} goals based 2023 performance: ${1/goal_less_perc_2023:.2f}"
)
print()
print(
    f"True odds for over {input_goals} goals based on 2023 performance: ${1/goal_greater_perc_2023:.2f}"
)
print()
print()

# print the results, based on time
# IMPORATNT - UPDATE PERCETNAGE VARIABLES

print(f"{input_time} Games Results")
print(
    f"Number of {input_time} games less than {input_goals} goals: {goals_less_time}"
)
print()
print(
    f"Number of {input_time} games greater than {input_goals} goals: {goals_greater_time}"
)
print()
print(
    f"Percentage of {input_time} games less than {input_goals} goals: {goal_less_perc_time *100:.2f}%"
)
print()
print(
    f"Percentage of {input_time} games greater than {input_goals} goals: {goal_greater_perc_time *100:.2f}%"
)
print()
print(
    f"True odds for under {input_goals} goals based {input_time} performance: ${1/goal_less_perc_time:.2f}"
)
print()
print(
    f"True odds for over {input_goals} goals based on {input_time} performance: ${1/goal_greater_perc_time:.2f}"
)
print()
print()

# print the results, based on day of week
# IMPORATNT - UPDATE PERCETNAGE VARIABLES

print(f"{input_dayofweek} Games Results")
print(
    f"Number of {input_dayofweek} games less than {input_goals} goals: {goals_less_dayofweek}"
)
print()
print(
    f"Number of {input_dayofweek} games greater than {input_goals} goals: {goals_greater_dayofweek}"
)
print()
print(
    f"Percentage of {input_dayofweek} games less than {input_goals} goals: {goal_less_perc_dayofweek *100:.2f}%"
)
print()
print(
    f"Percentage of {input_dayofweek} games greater than {input_goals} goals: {goal_greater_perc_dayofweek *100:.2f}%"
)
print()
print(
    f"True odds for under {input_goals} goals based {input_dayofweek} performance: ${1/goal_less_perc_dayofweek:.2f}"
)
print()
print(
    f"True odds for over {input_goals} goals based on {input_dayofweek} performance: ${1/goal_greater_perc_dayofweek:.2f}"
)
print()
print()
