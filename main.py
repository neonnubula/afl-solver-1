# next major task is to add name selecton

# required libraries
import pandas as pd

#User input
#name
input_name = input("Enter the player name: (john/david) ")
print()
#disposals
input_di = float(input("What is the disposal line?: "))
print()
#goal line
input_gls = float(input("What is the gl line?: "))
print()
#location
input_loc = input("Is the player at home or away?: (home/away) ")
print()
#opposition
input_opp = input("Who is the opp? ")
print()
#ven
input_ven = input("What stadium is the game at? ")
print()
#ssns since
input_ssns = int(input("From what ssns do you want results? (ex: 2021) "))
print()
#time
input_time = input("Is the game night or day? (night/day) ")
print()
#day
input_day = input("What day of the week is the game on? (ex: monday) ")
print()

# read the CSV data into a Dataframe
df = pd.read_csv('test-data.csv')

# print the dataframe, during testing to see
print(df)
print()


# functions to analyze the csv
# di
# define function to count grtr than and less than of the user input vs disposal line
def count_di(value):
  di_less = df.loc[(df["ssns"] >= input_ssns) &
                          (df["name"] == input_name) &
                          (df["di"] < input_di),
                          "di"].count()
  di_grtr = df.loc[(df["ssns"] >= input_ssns) &
                             (df["name"] == input_name) &
                             (df["di"] > input_di),
                             "di"].count()
  return di_less, di_grtr


# define function for user input loc to count grtr and less than of the user input vs disposal line
def count_di_loc(value):
  di_less_loc = df.loc[(df["loc"] == input_loc) &
                                   (df["name"] == input_name) &
                                   (df["ssns"] >= input_ssns) &
                                   (df["di"] < input_di),
                                   "di"].count()
  di_grtr_loc = df.loc[(df["loc"] == input_loc) &
                                      (df["name"] == input_name) &
                                      (df["ssns"] >= input_ssns) &
                                      (df["di"] > input_di),
                                      "di"].count()
  return di_less_loc, di_grtr_loc


# define the function for user input opp to count grtr than and less than of the user input vs di line
def count_di_opp(value):
  di_less_opp = df.loc[(df["opp"] == input_opp) &
                                     (df["name"] == input_name) &
                                     (df["ssns"] >= input_ssns) &
                                     (df["di"] < input_di),
                                     "di"].count()
  di_grtr_opp = df.loc[(df["opp"] == input_opp)
                                        & (df["name"] == input_name) &
                                        (df["ssns"] >= input_ssns) &
                                        (df["di"] > input_di),
                                        "di"].count()
  return di_less_opp, di_grtr_opp


# define the function for user input ven to count grtr than and less than of the user input vs di line
def count_di_ven(value):
  di_less_ven = df.loc[(df["ven"] == input_ven) &
                                (df["name"] == input_name) &
                                (df["ssns"] >= input_ssns) &
                                (df["di"] < input_di),
                                "di"].count()
  di_grtr_ven = df.loc[(df["ven"] == input_ven) &
                                   (df["name"] == input_name) &
                                   (df["ssns"] >= input_ssns) &
                                   (df["di"] > input_di),
                                   "di"].count()
  return di_less_ven, di_grtr_ven


# define the function for user input 2023 ssns to count grtr than and less than of the user input vs di line
def count_di_2023(value):
  di_less_2023 = df.loc[(df["ssns"] == 2023) &
                               (df["name"] == input_name) &
                               (df["di"] < input_di),
                               "di"].count()
  di_grtr_2023 = df.loc[(df["ssns"] == 2023) &
                                  (df["name"] == input_name) &
                                  (df["di"] > input_di),
                                  "di"].count()
  return di_less_2023, di_grtr_2023


# define the function for user input time to count grtr than and less than of the user input vs di line
def count_di_time(value):
  di_less_time = df.loc[(df["time"] == input_time) &
                               (df["name"] == input_name) &
                               (df["ssns"] >= input_ssns) &
                               (df["di"] < input_di),
                               "di"].count()
  di_grtr_time = df.loc[(df["time"] == input_time) &
                                  (df["name"] == input_name) &
                                  (df["ssns"] >= input_ssns) &
                                  (df["di"] > input_di),
                                  "di"].count()
  return di_less_time, di_grtr_time


# define the function for user input day of week to count grtr than and less than of the user input vs di line
def count_di_day(value):
  di_less_day = df.loc[(df["day"] == input_day) &
                                    (df["name"] == input_name) &
                                    (df["ssns"] >= input_ssns) &
                                    (df["di"] < input_di),
                                    "di"].count()
  di_grtr_day = df.loc[(df["day"] == input_day) &
                                       (df["name"] == input_name) &
                                       (df["ssns"] >= input_ssns) &
                                       (df["di"] > input_di),
                                       "di"].count()
  return di_less_day, di_grtr_day


# glS
# define function to count grtr than and less than of the user input vs gl line
def count_gls(value):
  gls_less = df.loc[(df["ssns"] >= input_ssns) &
                      (df["gls"] < input_gls), "gls"].count()
  gls_grtr = df.loc[(df["ssns"] >= input_ssns) &
                         (df["gls"] > input_gls), "gls"].count()
  return gls_less, gls_grtr


# define function for user input loc to count grtr and less than of the user input vs gl line
def count_gls_loc(value):
  gls_less_loc = df.loc[(df["loc"] == input_loc) &
                               (df["ssns"] >= input_ssns) &
                               (df["gls"] < input_gls), "gls"].count()
  gls_grtr_loc = df.loc[(df["loc"] == input_loc) &
                                  (df["ssns"] >= input_ssns) &
                                  (df["gls"] > input_gls),
                                  "gls"].count()
  return gls_less_loc, gls_grtr_loc


# define the function for user input opp to count grtr than and less than of the user input vs gls line
def count_gls_opp(value):
  gls_less_opp = df.loc[(df["opp"] == input_opp) &
                                 (df["ssns"] >= input_ssns) &
                                 (df["gls"] < input_gls), "gls"].count()
  gls_grtr_opp = df.loc[(df["opp"] == input_opp) &
                                    (df["ssns"] >= input_ssns) &
                                    (df["gls"] > input_gls),
                                    "gls"].count()
  return gls_less_opp, gls_grtr_opp


# define the function for user input ven to count grtr than and less than of the user input vs gls line
def count_gls_ven(value):
  gls_less_ven = df.loc[(df["ven"] == input_ven) &
                            (df["ssns"] >= input_ssns) &
                            (df["gls"] < input_gls), "gls"].count()
  gls_grtr_ven = df.loc[(df["ven"] == input_ven) &
                               (df["ssns"] >= input_ssns) &
                               (df["gls"] > input_gls), "gls"].count()
  return gls_less_ven, gls_grtr_ven


# define the function for user input 2023 ssns to count grtr than and less than of the user input vs gls line
def count_gls_2023(value):
  gls_less_2023 = df.loc[(df["ssns"] == 2023) &
                           (df["gls"] < input_gls), "gls"].count()
  gls_grtr_2023 = df.loc[(df["ssns"] == 2023) &
                              (df["gls"] > input_gls), "gls"].count()
  return gls_less_2023, gls_grtr_2023


# define the function for user input time to count grtr than and less than of the user input vs gls line
def count_gls_time(value):
  gls_less_time = df.loc[(df["time"] == input_time) &
                           (df["ssns"] >= input_ssns) &
                           (df["gls"] < input_gls), "gls"].count()
  gls_grtr_time = df.loc[(df["time"] == input_time) &
                              (df["ssns"] >= input_ssns) &
                              (df["gls"] > input_gls), "gls"].count()
  return gls_less_time, gls_grtr_time


# define the function for user input day of week to count grtr than and less than of the user input vs gls line
def count_gls_day(value):
  gls_less_day = df.loc[(df["day"] == input_day) &
                                (df["ssns"] >= input_ssns) &
                                (df["gls"] < input_gls), "gls"].count()
  gls_grtr_day = df.loc[(df["day"] == input_day) &
                                   (df["ssns"] >= input_ssns) &
                                   (df["gls"] > input_gls),
                                   "gls"].count()
  return gls_less_day, gls_grtr_day


# 2 LEG COMBOS
# define function to count grtr than and less than of the user input vs combo of disposal & gl lines.
def count_di_gls(di, gls):
  di_grtr_gls_grtr = df.loc[(df["ssns"] >= input_ssns) &
                                           (df["name"] == input_name) &
                                           (df["gls"] > input_gls) &
                                           (df["di"] > input_di),
                                           "di"].count()
  di_grtr_gls_less = df.loc[(df["ssns"] >= input_ssns) &
                                        (df["name"] == input_name) &
                                        (df["gls"] < input_gls) &
                                        (df["di"] > input_di),
                                        "di"].count()
  di_less_gls_grtr = df.loc[(df["ssns"] >= input_ssns) &
                                        (df["name"] == input_name) &
                                        (df["gls"] > input_gls) &
                                        (df["di"] < input_di),
                                        "di"].count()
  di_less_gls_less = df.loc[(df["ssns"] >= input_ssns) &
                                     (df["name"] == input_name) &
                                     (df["gls"] < input_gls) &
                                     (df["di"] < input_di),
                                     "di"].count()
  return di_grtr_gls_grtr, di_grtr_gls_less, di_less_gls_grtr, di_less_gls_less


# define function for user input loc to count grtr and less than of the user input vs disposal line
def count_di_gls_loc(di, gls):
  di_grtr_gls_grtr_loc = df.loc[
      (df["ssns"] >= input_ssns) & (df["name"] == input_name) &
      (df["loc"] == input_loc) & (df["gls"] > input_gls) &
      (df["di"] > input_di), "di"].count()
  di_grtr_gls_less_loc = df.loc[
      (df["ssns"] >= input_ssns) & (df["name"] == input_name) &
      (df["loc"] == input_loc) & (df["gls"] < input_gls) &
      (df["di"] > input_di), "di"].count()
  di_less_gls_grtr_loc = df.loc[
      (df["ssns"] >= input_ssns) & (df["name"] == input_name) &
      (df["loc"] == input_loc) & (df["gls"] > input_gls) &
      (df["di"] < input_di), "di"].count()
  di_less_gls_less_loc = df.loc[
      (df["ssns"] >= input_ssns) & (df["name"] == input_name) &
      (df["loc"] == input_loc) & (df["gls"] < input_gls) &
      (df["di"] < input_di), "di"].count()
  return di_grtr_gls_grtr_loc, di_grtr_gls_less_loc, di_less_gls_grtr_loc, di_less_gls_less_loc
  # di_less_loc = df.loc[(df["loc"] == input_loc) & (df["name"] == input_name) & (df["ssns"] >= input_ssns) & (df["di"] < input_di), "di"].count()
  # di_grtr_loc = df.loc[(df["loc"] == input_loc) & (df["name"] == input_name) & (df["ssns"] >= input_ssns) & (df["di"] > input_di), "di"].count()
  # return di_less_loc, di_grtr_loc


# define the function for user input opp to count grtr than and less than of the user input vs di line
def count_di_gls_opp(di, gls):
  di_grtr_gls_grtr_opp = df.loc[
      (df["ssns"] >= input_ssns) & (df["name"] == input_name) &
      (df["opp"] == input_opp) & (df["gls"] > input_gls) &
      (df["di"] > input_di), "di"].count()
  di_grtr_gls_less_opp = df.loc[
      (df["ssns"] >= input_ssns) & (df["name"] == input_name) &
      (df["opp"] == input_opp) & (df["gls"] < input_gls) &
      (df["di"] > input_di), "di"].count()
  di_less_gls_grtr_opp = df.loc[
      (df["ssns"] >= input_ssns) & (df["name"] == input_name) &
      (df["opp"] == input_opp) & (df["gls"] > input_gls) &
      (df["di"] < input_di), "di"].count()
  di_less_gls_less_opp = df.loc[
      (df["ssns"] >= input_ssns) & (df["name"] == input_name) &
      (df["opp"] == input_opp) & (df["gls"] < input_gls) &
      (df["di"] < input_di), "di"].count()
  return di_grtr_gls_grtr_opp, di_grtr_gls_less_opp, di_less_gls_grtr_opp, di_less_gls_less_opp
  # di_less_opp = df.loc[(df["opp"] == input_opp) & (df["name"] == input_name) & (df["ssns"] >= input_ssns) & (df["di"] < input_di), "di"].count()
  # di_grtr_opp = df.loc[(df["opp"] == input_opp) & (df["name"] == input_name) & (df["ssns"] >= input_ssns) & (df["di"] > input_di), "di"].count()
  # return di_less_opp, di_grtr_opp


# define the function for user input ven to count grtr than and less than of the user input vs di line
def count_di_gls_ven(di, gls):
  di_grtr_gls_grtr_ven = df.loc[
      (df["ssns"] >= input_ssns) & (df["name"] == input_name) &
      (df["ven"] == input_ven) & (df["gls"] > input_gls) &
      (df["di"] > input_di), "di"].count()
  di_grtr_gls_less_ven = df.loc[
      (df["ssns"] >= input_ssns) & (df["name"] == input_name) &
      (df["ven"] == input_ven) & (df["gls"] < input_gls) &
      (df["di"] > input_di), "di"].count()
  di_less_gls_grtr_ven = df.loc[
      (df["ssns"] >= input_ssns) & (df["name"] == input_name) &
      (df["ven"] == input_ven) & (df["gls"] > input_gls) &
      (df["di"] < input_di), "di"].count()
  di_less_gls_less_ven = df.loc[(df["ssns"] >= input_ssns) &
                                           (df["name"] == input_name) &
                                           (df["ven"] == input_ven) &
                                           (df["gls"] < input_gls) &
                                           (df["di"] < input_di),
                                           "di"].count()
  return di_grtr_gls_grtr_ven, di_grtr_gls_less_ven, di_less_gls_grtr_ven, di_less_gls_less_ven
  # di_less_ven = df.loc[(df["ven"] == input_ven) & (df["name"] == input_name) & (df["ssns"] >= input_ssns) & (df["di"] < input_di), "di"].count()
  # di_grtr_ven = df.loc[(df["ven"] == input_ven) & (df["name"] == input_name) & (df["ssns"] >= input_ssns) & (df["di"] > input_di), "di"].count()
  # return di_less_ven, di_grtr_ven


# define the function for user input 2023 ssns to count grtr than and less than of the user input vs di line
def count_di_gls_2023(di, gls):
  di_grtr_gls_grtr_2023 = df.loc[
      (df["ssns"] >= input_ssns) & (df["name"] == input_name) &
      (df["ssns"] == 2023) & (df["gls"] > input_gls) &
      (df["di"] > input_di), "di"].count()
  di_grtr_gls_less_2023 = df.loc[
      (df["ssns"] >= input_ssns) & (df["name"] == input_name) &
      (df["ssns"] == 2023) & (df["gls"] < input_gls) &
      (df["di"] > input_di), "di"].count()
  di_less_gls_grtr_2023 = df.loc[
      (df["ssns"] >= input_ssns) & (df["name"] == input_name) &
      (df["ssns"] == 2023) & (df["gls"] > input_gls) &
      (df["di"] < input_di), "di"].count()
  di_less_gls_less_2023 = df.loc[(df["ssns"] >= input_ssns) &
                                          (df["name"] == input_name) &
                                          (df["ssns"] == 2023) &
                                          (df["gls"] < input_gls) &
                                          (df["di"] < input_di),
                                          "di"].count()
  return di_grtr_gls_grtr_2023, di_grtr_gls_less_2023, di_less_gls_grtr_2023, di_less_gls_less_2023
  # di_less_2023 = df.loc[(df["ssns"] == 2023) & (df["name"] == input_name) & (df["di"] < input_di), "di"].count()
  # di_grtr_2023 = df.loc[(df["ssns"] == 2023) & (df["name"] == input_name) & (df["di"] > input_di), "di"].count()
  # return di_less_2023, di_grtr_2023


# define the function for user input time to count grtr than and less than of the user input vs di line
def count_di_gls_time(di, gls):
  di_grtr_gls_grtr_time = df.loc[
      (df["ssns"] >= input_ssns) & (df["name"] == input_name) &
      (df["time"] == input_time) & (df["gls"] > input_gls) &
      (df["di"] > input_di), "di"].count()
  di_grtr_gls_less_time = df.loc[
      (df["ssns"] >= input_ssns) & (df["name"] == input_name) &
      (df["time"] == input_time) & (df["gls"] < input_gls) &
      (df["di"] > input_di), "di"].count()
  di_less_gls_grtr_time = df.loc[
      (df["ssns"] >= input_ssns) & (df["name"] == input_name) &
      (df["time"] == input_time) & (df["gls"] > input_gls) &
      (df["di"] < input_di), "di"].count()
  di_less_gls_less_time = df.loc[(df["ssns"] >= input_ssns) &
                                          (df["name"] == input_name) &
                                          (df["time"] == input_time) &
                                          (df["gls"] < input_gls) &
                                          (df["di"] < input_di),
                                          "di"].count()
  return di_grtr_gls_grtr_time, di_grtr_gls_less_time, di_less_gls_grtr_time, di_less_gls_less_time
  # di_less_time = df.loc[(df["time"] == input_time) & (df["name"] == input_name) & (df["ssns"] >= input_ssns) & (df["di"] < input_di), "di"].count()
  # di_grtr_time = df.loc[(df["time"] == input_time) & (df["name"] == input_name) & (df["ssns"] >= input_ssns) & (df["di"] > input_di), "di"].count()
  # return di_less_time, di_grtr_time


# define the function for user input day of week to count grtr than and less than of the user input vs di line
def count_di_gls_day(di, gls):
  di_grtr_gls_grtr_day = df.loc[
      (df["ssns"] >= input_ssns) & (df["name"] == input_name) &
      (df["day"] == input_day) & (df["gls"] > input_gls) &
      (df["di"] > input_di), "di"].count()
  di_grtr_gls_less_day = df.loc[
      (df["ssns"] >= input_ssns) & (df["name"] == input_name) &
      (df["day"] == input_day) & (df["gls"] < input_gls) &
      (df["di"] > input_di), "di"].count()
  di_less_gls_grtr_day = df.loc[
      (df["ssns"] >= input_ssns) & (df["name"] == input_name) &
      (df["day"] == input_day) & (df["gls"] > input_gls) &
      (df["di"] < input_di), "di"].count()
  di_less_gls_less_day = df.loc[
      (df["ssns"] >= input_ssns) & (df["name"] == input_name) &
      (df["day"] == input_day) & (df["gls"] < input_gls) &
      (df["di"] < input_di), "di"].count()
  return di_grtr_gls_grtr_day, di_grtr_gls_less_day, di_less_gls_grtr_day, di_less_gls_less_day
  # di_less_day = df.loc[(df["day"] == input_day) & (df["name"] == input_name) & (df["ssns"] >= input_ssns) & (df["di"] < input_di), "di"].count()
  # di_grtr_day = df.loc[(df["day"] == input_day) & (df["name"] == input_name) & (df["ssns"] >= input_ssns) & (df["di"] > input_di), "di"].count()
  # return di_less_day, di_grtr_day


# run the function with the user input vs the data frame of the test data
# di
# all gms
di_less, di_grtr = count_di(input_di)
# loc
di_less_loc, di_grtr_loc = count_di_loc(
    input_di)
# opp
di_less_opp, di_grtr_opp = count_di_opp(
    input_di)
# ven
di_less_ven, di_grtr_ven = count_di_ven(
    input_di)
# 2023 ssns
di_less_2023, di_grtr_2023 = count_di_2023(
    input_di)
#  time
di_less_time, di_grtr_time = count_di_time(
    input_di)
# day
di_less_day, di_grtr_day = count_di_day(
    input_di)

# glS
# all gms
gls_less, gls_grtr = count_gls(input_gls)
# loc
gls_less_loc, gls_grtr_loc = count_gls_loc(input_gls)
# opp
gls_less_opp, gls_grtr_opp = count_gls_opp(
    input_gls)
# ven
gls_less_ven, gls_grtr_ven = count_gls_ven(input_gls)
# 2023 ssns
gls_less_2023, gls_grtr_2023 = count_gls_2023(input_gls)
#  time
gls_less_time, gls_grtr_time = count_gls_time(input_gls)
# day
gls_less_day, gls_grtr_day = count_gls_day(
    input_gls)

# 2 LEG COMBOS
# all gms
di_grtr_gls_grtr, di_grtr_gls_less, di_less_gls_grtr, di_less_gls_less = count_di_gls(
    input_di, input_gls)
# loc
di_grtr_gls_grtr_loc, di_grtr_gls_less_loc, di_less_gls_grtr_loc, di_less_gls_less_loc = count_di_gls_loc(
    input_di, input_gls)
# opp
di_grtr_gls_grtr_opp, di_grtr_gls_less_opp, di_less_gls_grtr_opp, di_less_gls_less_opp = count_di_gls_opp(
    input_di, input_gls)
# ven
di_grtr_gls_grtr_ven, di_grtr_gls_less_ven, di_less_gls_grtr_ven, di_less_gls_less_ven = count_di_gls_ven(
    input_di, input_gls)
# 2023 ssns
di_grtr_gls_grtr_2023, di_grtr_gls_less_2023, di_less_gls_grtr_2023, di_less_gls_less_2023 = count_di_gls_2023(
    input_di, input_gls)
#  time
di_grtr_gls_grtr_time, di_grtr_gls_less_time, di_less_gls_grtr_time, di_less_gls_less_time = count_di_gls_time(
    input_di, input_gls)
# day
di_grtr_gls_grtr_day, di_grtr_gls_less_day, di_less_gls_grtr_day, di_less_gls_less_day = count_di_gls_day(
    input_di, input_gls)

# give the tot gms for each paramter a name
# di
# all gms
tot_gms = di_less + di_grtr
# loc
tot_gms_loc = di_less_loc + di_grtr_loc
# opp
tot_gms_opp = di_less_opp + di_grtr_opp
# ven
tot_gms_ven = di_less_ven + di_grtr_ven
# 2023 ssns
tot_gms_2023 = di_less_2023 + di_grtr_2023
# time gms
tot_gms_time = di_less_time + di_grtr_time
# day
tot_gms_day = di_less_day + di_grtr_day

# glS
# all gms
tot_gms = gls_less + gls_grtr
# loc
tot_gms_loc = gls_less_loc + gls_grtr_loc
# opp
tot_gms_opp = gls_less_opp + gls_grtr_opp
# ven
tot_gms_ven = gls_less_ven + gls_grtr_ven
# 2023 ssns
tot_gms_2023 = gls_less_2023 + gls_grtr_2023
# time gms
tot_gms_time = gls_less_time + gls_grtr_time
# day
tot_gms_day = gls_less_day + gls_grtr_day

#2 LEG COMBOS
# all gms
tot_gms_di_gls = di_grtr_gls_grtr + di_grtr_gls_less + di_less_gls_grtr + di_less_gls_less
# loc
tot_gms_di_gls_loc = di_grtr_gls_grtr_loc + di_grtr_gls_less_loc + di_less_gls_grtr_loc + di_less_gls_less_loc
# opp
tot_gms_di_gls_opp = di_grtr_gls_grtr_opp + di_grtr_gls_less_opp + di_less_gls_grtr_opp + di_less_gls_less_opp
# ven
tot_gms_di_gls_ven = di_grtr_gls_grtr_ven + di_grtr_gls_less_ven + di_less_gls_grtr_ven + di_less_gls_less_ven
# 2023 ssns
tot_gms_di_gls_2023 = di_grtr_gls_grtr_2023 + di_grtr_gls_less_2023 + di_less_gls_grtr_2023 + di_less_gls_less_2023
#  time
tot_gms_di_gls_time = di_grtr_gls_grtr_time + di_grtr_gls_less_time + di_less_gls_grtr_time + di_less_gls_less_time
# day
tot_gms_di_gls_day = di_grtr_gls_grtr_day + di_grtr_gls_less_day + di_less_gls_grtr_day + di_less_gls_less_day

# create variables for the pcs of each parameter
# di
# all gms
pc_di_less = di_less / tot_gms
pc_di_grtr = di_grtr / tot_gms
# loc
pc_di_less_loc = di_less_loc / tot_gms_loc
pc_di_grtr_loc = di_grtr_loc / tot_gms_loc
# opp
pc_di_less_opp = di_less_opp / tot_gms_opp
pc_di_grtr_opp = di_grtr_opp / tot_gms_opp
# ven
pc_di_less_ven = di_less_ven / tot_gms_ven
pc_di_grtr_ven = di_grtr_ven / tot_gms_ven
# 2023 ssns
pc_di_less_2023 = di_less_2023 / tot_gms_2023
pc_di_grtr_2023 = di_grtr_2023 / tot_gms_2023
# time
pc_di_less_time = di_less_time / tot_gms_time
pc_di_grtr_time = di_grtr_time / tot_gms_time
# day
pc_di_less_day = di_less_day / tot_gms_day
pc_di_grtr_day = di_grtr_day / tot_gms_day

# glS
# all gms
pc_gls_less = gls_less / tot_gms
pc_gls_grtr = gls_grtr / tot_gms
# loc
pc_gls_less_loc = gls_less_loc / tot_gms_loc
pc_gls_grtr_loc = gls_grtr_loc / tot_gms_loc
# opp
pc_gls_less_opp = gls_less_opp / tot_gms_opp
pc_gls_grtr_opp = gls_grtr_opp / tot_gms_opp
# ven
pc_gls_less_ven = gls_less_ven / tot_gms_ven
pc_gls_grtr_ven = gls_grtr_ven / tot_gms_ven
# 2023 ssns
pc_gls_less_2023 = gls_less_2023 / tot_gms_2023
pc_gls_grtr_2023 = gls_grtr_2023 / tot_gms_2023
# time
pc_gls_less_time = gls_less_time / tot_gms_time
pc_gls_grtr_time = gls_grtr_time / tot_gms_time
# day
pc_gls_less_day = gls_less_day / tot_gms_day
pc_gls_grtr_day = gls_grtr_day / tot_gms_day

#2 LEG COMBOS
# all gms
pc_di_grtr_gls_grtr = (di_grtr_gls_grtr /
                                              tot_gms_di_gls)
pc_di_grtr_gls_less = (di_grtr_gls_less /
                                           tot_gms_di_gls)
pc_di_less_gls_grtr = (di_less_gls_grtr /
                                           tot_gms_di_gls)
pc_di_less_gls_less = (di_less_gls_less /
                                        tot_gms_di_gls)
# loc
pc_di_grtr_gls_grtr_loc = (
    di_grtr_gls_grtr_loc /
    tot_gms_di_gls_loc)
pc_di_grtr_gls_less_loc = (
    di_grtr_gls_less_loc /
    tot_gms_di_gls_loc)
pc_di_less_gls_grtr_loc = (
    di_less_gls_grtr_loc /
    tot_gms_di_gls_loc)
pc_di_less_gls_less_loc = (
    di_less_gls_less_loc / tot_gms_di_gls_loc)
# opp
pc_di_grtr_gls_grtr_opp = (
    di_grtr_gls_grtr_opp /
    tot_gms_di_gls_opp)
pc_di_grtr_gls_less_opp = (
    di_grtr_gls_less_opp /
    tot_gms_di_gls_opp)
pc_di_less_gls_grtr_opp = (
    di_less_gls_grtr_opp /
    tot_gms_di_gls_opp)
pc_di_less_gls_less_opp = (
    di_less_gls_less_opp /
    tot_gms_di_gls_opp)
# ven
pc_di_grtr_gls_grtr_ven = (
    di_grtr_gls_grtr_ven / tot_gms_di_gls_ven)
pc_di_grtr_gls_less_ven = (
    di_grtr_gls_less_ven / tot_gms_di_gls_ven)
pc_di_less_gls_grtr_ven = (
    di_less_gls_grtr_ven / tot_gms_di_gls_ven)
pc_di_less_gls_less_ven = (
    di_less_gls_less_ven / tot_gms_di_gls_ven)
# 2023 ssns
pc_di_grtr_gls_grtr_2023 = (
    di_grtr_gls_grtr_2023 / tot_gms_di_gls_2023)
pc_di_grtr_gls_less_2023 = (
    di_grtr_gls_less_2023 / tot_gms_di_gls_2023)
pc_di_less_gls_grtr_2023 = (
    di_less_gls_grtr_2023 / tot_gms_di_gls_2023)
pc_di_less_gls_less_2023 = (di_less_gls_less_2023 /
                                             tot_gms_di_gls_2023)
# time
pc_di_grtr_gls_grtr_time = (
    di_grtr_gls_grtr_time / tot_gms_di_gls_time)
pc_di_grtr_gls_less_time = (
    di_grtr_gls_less_time / tot_gms_di_gls_time)
pc_di_less_gls_grtr_time = (
    di_less_gls_grtr_time / tot_gms_di_gls_time)
pc_di_less_gls_less_time = (di_less_gls_less_time /
                                             tot_gms_di_gls_time)
# day
pc_di_grtr_gls_grtr_day = (
    di_grtr_gls_grtr_day /
    tot_gms_di_gls_day)
pc_di_grtr_gls_less_day = (
    di_grtr_gls_less_day /
    tot_gms_di_gls_day)
pc_di_less_gls_grtr_day = (
    di_less_gls_grtr_day /
    tot_gms_di_gls_day)
pc_di_less_gls_less_day = (
    di_less_gls_less_day /
    tot_gms_di_gls_day)

print()
print()
print(f"{input_name} results for disposal line of {input_di} and gls line of {input_gls}")
print()

# print results for di
print("di")

# print the all gms results, rounded to 2 decimal points (:.2f)
print("All gms Results")
print(f"Number of gms less than {input_di} di: {di_less}")
print(f"Number of gms grtr than {input_di} di: {di_grtr}")
print(f"pc of gms less than {input_di} di: {pc_gls_less *100:.2f}%")
print(f"pc of gms grtr than {input_di} di: {pc_gls_grtr *100:.2f}%")
print(f"True odds for under {input_di} di based on past performance: ${1/pc_di_less:.2f}")
print(f"True odds for over {input_di} di based on past performance: ${1/pc_di_grtr:.2f}")
print()
print()

# print the results, based on loc input
print(f"{input_loc} gms Results")
print(f"Number of {input_loc} gms less than {input_di} di: {di_less_loc}")
print(f"Number of {input_loc} gms grtr than {input_di} di: {di_grtr_loc}")
print(f"pc of {input_loc} gms less than {input_di} di: {disp_less_perc_loc *100:.2f}%")
print(f"pc of {input_loc} gms grtr than {input_di} di: {disp_grtr_perc_loc *100:.2f}%")
print(f"True odds for under {input_di} di based on past {input_loc} performance: ${1/disp_less_perc_loc:.2f}")
print(f"True odds for over {input_di} di based on past {input_loc} performance: ${1/disp_grtr_perc_loc:.2f}")
print()
print()

# print the results, based on opp
print(f"Against {input_opp} gms Results")
print(f"Number of gms against {input_opp} less than {input_di} di: {di_less_opp}")
print(f"Number of gms against {input_opp} grtr than {input_di} di: {di_grtr_opp}")
print(f"pc of gms against {input_opp} less than {input_di} di: {pc_di_less_opp * 100:.2f}%")
print(f"pc of gms against {input_opp} grtr than {input_di} di: {pc_di_grtr_opp * 100:.2f}%")
print(f"True odds for under {input_di} di based on past against {input_opp} performance: ${1 / pc_di_less_opp:.2f}")
print(f"True odds for over {input_di} di based on past against {input_opp} performance: ${1 / pc_di_grtr_opp:.2f}")
print()
print()

# print the results, based on ven
print(f"At {input_ven} gms Results")
print(f"Number of at {input_ven} gms less than {input_di} di: {di_less_ven}")
print(f"Number of at {input_ven} gms grtr than {input_di} di: {di_grtr_ven}")
print(f"pc of at {input_ven} gms less than {input_di} di: {pc_di_less_ven * 100:.2f}%")
print(f"pc of at {input_ven} gms grtr than {input_di} di: {pc_di_grtr_ven * 100:.2f}%")
print(f"True odds for under {input_di} di based on past at {input_ven} performance: ${1 / pc_di_less_ven:.2f}")
print(f"True odds for over {input_di} di based on past at {input_ven} performance: ${1 / pc_di_grtr_ven:.2f}")
print()
print()

# print the results, based on 2023 ssns
print(f"2023 ssns gms Results")
print(f"Number of 2023 gms less than {input_di} di: {di_less_2023}")
print(f"Number of 2023 gms grtr than {input_di} di: {di_grtr_2023}")
print(f"pc of 2023 gms less than {input_di} di: {pc_di_less_2023 * 100:.2f}%")
print(f"pc of 2023 gms grtr than {input_di} di: {pc_di_grtr_2023 * 100:.2f}%")
print(f"True odds for under {input_di} di based on 2023 performance: ${1 / pc_di_less_2023:.2f}")
print(f"True odds for over {input_di} di based on 2023 performance: ${1 / pc_di_grtr_2023:.2f}")
print()
print()

# print the results, based on time
print(f"{input_time} gms Results")
print(f"Number of {input_time} gms less than {input_di} di: {di_less_time}")
print(f"Number of {input_time} gms grtr than {input_di} di: {di_grtr_time}")
print(f"pc of {input_time} gms less than {input_di} di: {pc_di_less_time * 100:.2f}%")
print(f"pc of {input_time} gms grtr than {input_di} di: {pc_di_grtr_time * 100:.2f}%")
print(f"True odds for under {input_di} di based {input_time} performance: ${1 / pc_di_less_time:.2f}")
print(f"True odds for over {input_di} di based on {input_time} performance: ${1 / pc_di_grtr_time:.2f}")
print()
print()

# print the results, based on day of week
print(f"{input_day} gms Results")
print(f"Number of {input_day} gms less than {input_di} di: {di_less_day}")
print(f"Number of {input_day} gms grtr than {input_di} di: {di_grtr_day}")
print(f"pc of {input_day} gms less than {input_di} di: {pc_di_less_day * 100:.2f}%")
print(f"pc of {input_day} gms grtr than {input_di} di: {pc_di_grtr_day * 100:.2f}%")
print(f"True odds for under {input_di} di based on {input_day} performance: ${1 / pc_di_less_day:.2f}")
print(f"True odds for over {input_di} di based on {input_day} performance: ${1 / pc_di_grtr_day:.2f}")
print()
print()


# print results for glS
print("glS")
# print the full gms results, rounded to 2 decimal points (:.2f)
print("All gms Results")
print(f"Number of gms less than {input_gls} gls: {gls_less}")
print(f"Number of gms grtr than {input_gls} gls: {gls_grtr}")
print(f"pc of gms less than {input_gls} gls: {pc_gls_less *100:.2f}%")
print(f"pc of gms grtr than {input_gls} gls: {pc_gls_grtr *100:.2f}%")
print(f"True odds for under {input_gls} gls based on past performance: ${1/pc_gls_less:.2f}")
print(f"True odds for over {input_gls} gls based on past performance: ${1/pc_gls_grtr:.2f}")
print()
print()

# print the results, based on loc input
print(f"{input_loc} gms Results")
print(f"Number of {input_loc} gms less than {input_gls} gls: {gls_less_loc}")
print(f"Number of {input_loc} gms grtr than {input_gls} gls: {gls_grtr_loc}")
print(f"pc of {input_loc} gms less than {input_gls} gls: {pc_gls_less_loc *100:.2f}%")
print(f"pc of {input_loc} gms grtr than {input_gls} gls: {pc_gls_grtr_loc *100:.2f}%")
print(f"True odds for under {input_gls} gls based on past {input_loc} performance: ${1/pc_gls_less_loc:.2f}")
print(f"True odds for over {input_gls} gls based on past {input_loc} performance: ${1/pc_gls_grtr_loc:.2f}")
print()
print()

# print the results, based on opp
print(f"Against {input_opp} gms Results")
print(f"Number of gms against {input_opp} less than {input_gls} gls: {gls_less_opp}")
print(f"Number of gms against {input_opp} grtr than {input_gls} gls: {gls_grtr_opp}")
print(f"pc of gms against {input_opp} less than {input_gls} gls: {pc_gls_less_opp * 100:.2f}%")
print(f"pc of gms against {input_opp} grtr than {input_gls} gls: {pc_gls_grtr_opp * 100:.2f}%")
print(f"True odds for under {input_gls} gls based on past against {input_opp} performance: ${1 / pc_gls_less_opp:.2f}")
print(f"True odds for over {input_gls} gls based on past against {input_opp} performance: ${1 / pc_gls_grtr_opp:.2f}")
print()
print()

# print the results, based on ven
print(f"At {input_ven} gms Results")
print(f"Number of at {input_ven} gms less than {input_gls} gls: {gls_less_ven}")
print(f"Number of at {input_ven} gms grtr than {input_gls} gls: {gls_grtr_ven}")
print(f"pc of at {input_ven} gms less than {input_gls} gls: {pc_gls_less_ven * 100:.2f}%")
print(f"pc of at {input_ven} gms grtr than {input_gls} gls: {pc_gls_grtr_ven * 100:.2f}%")
print(f"True odds for under {input_gls} gls based on past at {input_ven} performance: ${1 / pc_gls_less_ven:.2f}")
print(f"True odds for over {input_gls} gls based on past at {input_ven} performance: ${1 / pc_gls_grtr_ven:.2f}")
print()
print()

# print the results, based on 2023 ssns
print(f"2023 ssns gms Results")
print(f"Number of 2023 gms less than {input_gls} gls: {gls_less_2023}")
print(f"Number of 2023 gms grtr than {input_gls} gls: {gls_grtr_2023}")
print(f"pc of 2023 gms less than {input_gls} gls: {pc_gls_less_2023 * 100:.2f}%")
print(f"pc of 2023 gms grtr than {input_gls} gls: {pc_gls_grtr_2023 * 100:.2f}%")
print(f"True odds for under {input_gls} gls based on 2023 performance: ${1 / pc_gls_less_2023:.2f}")
print(f"True odds for over {input_gls} gls based on 2023 performance: ${1 / pc_gls_grtr_2023:.2f}")
print()
print()

# print the results, based on time
print(f"{input_time} gms Results")
print(f"Number of {input_time} gms less than {input_gls} gls: {gls_less_time}")
print(f"Number of {input_time} gms grtr than {input_gls} gls: {gls_grtr_time}")
print(f"pc of {input_time} gms less than {input_gls} gls: {pc_gls_less_time * 100:.2f}%")
print(f"pc of {input_time} gms grtr than {input_gls} gls: {pc_gls_grtr_time * 100:.2f}%")
print(f"True odds for under {input_gls} gls based on past at night performance: ${1 / pc_gls_less_time:.2f}")
print(f"True odds for over {input_gls} gls based on past at night performance: ${1 / pc_gls_grtr_time:.2f}")
print()
print()

# print the results, based on day of week
print(f"{input_day} gms Results")
print(f"Number of {input_day} gms less than {input_gls} gls: {gls_less_day}")
print(f"Number of {input_day} gms grtr than {input_gls} gls: {gls_grtr_day}")
print(f"pc of {input_day} gms less than {input_gls} gls: {pc_gls_less_day * 100:.2f}%")
print(f"pc of {input_day} gms grtr than {input_gls} gls: {pc_gls_grtr_day * 100:.2f}%")
print(f"True odds for under {input_gls} gls based on past at night performance: ${1 / pc_gls_less_day:.2f}")
print(f"True odds for over {input_gls} gls based on past at night performance: ${1 / pc_gls_grtr_day:.2f}")
print()
print()

# print results based on 2 LEG COMBOS
print("2 LEG COMBO RESULTS")
# print the all gms results
print("All gms Results")
print(f"Number of gms with di grtr than {input_di} and gls grtr than {input_gls}: {di_grtr_gls_grtr}")
print(f"Number of gms with di grtr than {input_di} and gls less than {input_gls}: {di_grtr_gls_less}")
print(f"Number of gms with di less than {input_di} and gls grtr than {input_gls}: {di_less_gls_grtr}")
print(f"Number of gms with di less than {input_di} and gls less than {input_gls}: {di_grtr_gls_less}")
print(f"pc of gms with di grtr than {input_di} and gls grtr than {input_gls}: {pc_di_grtr_gls_grtr *100:.2f}%")
print(f"pc of gms with di grtr than {input_di} and gls less than {input_gls}: {pc_di_grtr_gls_less *100:.2f}%")
print(f"pc of gms with di less than {input_di} and gls grtr than {input_gls}: {pc_di_less_gls_grtr *100:.2f}%")
print(f"pc of gms with di less than {input_di} and gls less than {input_gls}: {pc_di_less_gls_less *100:.2f}%")
print(f"True odds for gms with di grtr than {input_di} and gls grtr than {input_gls} based on past performance: ${1/pc_di_grtr_gls_grtr:.2f}")
print(f"True odds for gms with di grtr than {input_di} and gls less than {input_gls} based on past performance: ${1/pc_di_grtr_gls_less:.2f}")
print(f"True odds for gms with di less than {input_di} and gls grtr than {input_gls} based on past performance: ${1/pc_di_less_gls_grtr.2f}")
print(f"True odds for gms with di less than {input_di} and gls less than {input_gls} based on past performance: ${1/pc_di_less_gls_less:.2f}")
print()
print()
# print the loc results
print("loc Results")
print(f"Number of gms with di grtr than {input_di} and gls grtr than {input_gls}: {di_grtr_gls_grtr_loc}")
print(f"Number of gms with di grtr than {input_di} and gls less than {input_gls}: {di_grtr_gls_less_loc}")
print(f"Number of gms with di less than {input_di} and gls grtr than {input_gls}: {di_less_gls_grtr_loc}")
print(f"Number of gms with di less than {input_di} and gls less than {input_gls}: {di_less_gls_less_loc}")
print(f"pc of gms with di grtr than {input_di} and gls grtr than {input_gls}: {pc_di_grtr_gls_grtr_loc *100:.2f}%")
print(f"pc of gms with di grtr than {input_di} and gls less than {input_gls}: {pc_di_grtr_gls_less_loc *100:.2f}%")
print(f"pc of gms with di less than {input_di} and gls grtr than {input_gls}: {pc_di_less_gls_grtr_loc *100:.2f}%")
print(f"pc of gms with di less than {input_di} and gls less than {input_gls}: {pc_di_less_gls_less_loc *100:.2f}%")
print(f"True odds for gms with di grtr than {input_di} and gls grtr than {input_gls} based on past performance: ${1/pc_di_grtr_gls_grtr_loc:.2f}")
print(f"True odds for gms with di grtr than {input_di} and gls less than {input_gls} based on past performance: ${1/pc_di_grtr_gls_less_loc:.2f}")
print(f"True odds for gms with di less than {input_di} and gls grtr than {input_gls} based on past performance: ${1/pc_di_less_gls_grtr_loc:.2f}")
print(f"True odds for gms with di less than {input_di} and gls less than {input_gls} based on past performance: ${1/pc_di_less_gls_less_loc:.2f}")
print()
print()
# print the opp results
print("opp Results")
print(f"Number of gms with di grtr than {input_di} and gls grtr than {input_gls}: {di_grtr_gls_grtr_opp}")
print(f"Number of gms with di grtr than {input_di} and gls less than {input_gls}: {di_grtr_gls_less_opp}")
print(f"Number of gms with di less than {input_di} and gls grtr than {input_gls}: {di_less_gls_grtr_opp}")
print(f"Number of gms with di less than {input_di} and gls less than {input_gls}: {di_less_gls_less_opp}")
print(f"pc of gms with di grtr than {input_di} and gls grtr than {input_gls}: {pc_di_grtr_gls_grtr_opp *100:.2f}%")
print(f"pc of gms with di grtr than {input_di} and gls less than {input_gls}: {pc_di_grtr_gls_less_opp *100:.2f}%")
print(f"pc of gms with di less than {input_di} and gls grtr than {input_gls}: {pc_di_less_gls_grtr_opp *100:.2f}%")
print(f"pc of gms with di less than {input_di} and gls less than {input_gls}: {pc_di_less_gls_less_opp *100:.2f}%")
print(f"True odds for gms with di grtr than {input_di} and gls grtr than {input_gls} based on past performance: ${1/pc_di_grtr_gls_grtr_opp:.2f}")
print(f"True odds for gms with di grtr than {input_di} and gls less than {input_gls} based on past performance: ${1/pc_di_grtr_gls_less_opp:.2f}")
print(f"True odds for gms with di less than {input_di} and gls grtr than {input_gls} based on past performance: ${1/pc_di_less_gls_grtr_opp:.2f}")
print(f"True odds for gms with di less than {input_di} and gls less than {input_gls} based on past performance: ${1/pc_di_less_gls_less_opp:.2f}")
print()
print()

# print the ven results
print("ven Results")
print(f"Number of gms with di grtr than {input_di} and gls grtr than {input_gls}: {di_grtr_gls_grtr_ven}")
print(f"Number of gms with di grtr than {input_di} and gls less than {input_gls}: {di_grtr_gls_less_ven}")
print(f"Number of gms with di less than {input_di} and gls grtr than {input_gls}: {di_less_gls_grtr_ven}")
print(f"Number of gms with di less than {input_di} and gls less than {input_gls}: {di_less_gls_less_ven}")
print(f"pc of gms with di grtr than {input_di} and gls grtr than {input_gls}: {pc_di_grtr_gls_grtr_ven *100:.2f}%")
print(f"pc of gms with di grtr than {input_di} and gls less than {input_gls}: {pc_di_grtr_gls_less_ven *100:.2f}%")
print(f"pc of gms with di less than {input_di} and gls grtr than {input_gls}: {pc_di_less_gls_grtr_ven *100:.2f}%")
print(f"pc of gms with di less than {input_di} and gls less than {input_gls}: {pc_di_less_gls_less_ven *100:.2f}%")
print(f"True odds for gms with di grtr than {input_di} and gls grtr than {input_gls} based on past performance: ${1/pc_di_grtr_gls_grtr_ven:.2f}")
print(f"True odds for gms with di grtr than {input_di} and gls less than {input_gls} based on past performance: ${1/pc_di_grtr_gls_less_ven:.2f}")
print(f"True odds for gms with di less than {input_di} and gls grtr than {input_gls} based on past performance: ${1/pc_di_less_gls_grtr_ven:.2f}")
print(f"True odds for gms with di less than {input_di} and gls less than {input_gls} based on past performance: ${1/pc_di_less_gls_less_ven:.2f}")
print()
print()

# print the 2023 results
print("2023 Results")
print(f"Number of gms with di grtr than {input_di} and gls grtr than {input_gls}: {di_grtr_gls_grtr_2023}")
print(f"Number of gms with di grtr than {input_di} and gls less than {input_gls}: {di_grtr_gls_less_2023}")
print(f"Number of gms with di less than {input_di} and gls grtr than {input_gls}: {di_less_gls_grtr_2023}")
print(f"Number of gms with di less than {input_di} and gls less than {input_gls}: {di_less_gls_less_2023}")
print(f"pc of gms with di grtr than {input_di} and gls grtr than {input_gls}: {pc_di_grtr_gls_grtr_2023 *100:.2f}%")
print(f"pc of gms with di grtr than {input_di} and gls less than {input_gls}: {pc_di_grtr_gls_less_2023 *100:.2f}%")
print(f"pc of gms with di less than {input_di} and gls grtr than {input_gls}: {pc_di_less_gls_grtr_2023 *100:.2f}%")
print(f"pc of gms with di less than {input_di} and gls less than {input_gls}: {pc_di_less_gls_less_2023 *100:.2f}%")
print(f"True odds for gms with di grtr than {input_di} and gls grtr than {input_gls} based on past performance: ${1/pc_di_grtr_gls_grtr_2023:.2f}")
print(f"True odds for gms with di grtr than {input_di} and gls less than {input_gls} based on past performance: ${1/pc_di_grtr_gls_less_2023:.2f}")
print(f"True odds for gms with di less than {input_di} and gls grtr than {input_gls} based on past performance: ${1/pc_di_less_gls_grtr_2023:.2f}")
print(f"True odds for gms with di less than {input_di} and gls less than {input_gls} based on past performance: ${1/pc_di_less_gls_less_2023:.2f}")
print()
print()

# print the time results
print("Time Results")
print(f"Number of gms with di grtr than {input_di} and gls grtr than {input_gls}: {di_grtr_gls_grtr_time}")
print(f"Number of gms with di grtr than {input_di} and gls less than {input_gls}: {di_grtr_gls_less_time}")
print(f"Number of gms with di less than {input_di} and gls grtr than {input_gls}: {di_less_gls_grtr_time}")
print(f"Number of gms with di less than {input_di} and gls less than {input_gls}: {di_less_gls_less_time}")
print(f"pc of gms with di grtr than {input_di} and gls grtr than {input_gls}: {pc_di_grtr_gls_grtr_time *100:.2f}%")
print(f"pc of gms with di grtr than {input_di} and gls less than {input_gls}: {pc_di_grtr_gls_less_time *100:.2f}%")
print(f"pc of gms with di less than {input_di} and gls grtr than {input_gls}: {pc_di_less_gls_grtr_time *100:.2f}%")
print(f"pc of gms with di less than {input_di} and gls less than {input_gls}: {pc_di_less_gls_less_time *100:.2f}%")
print(f"True odds for gms with di grtr than {input_di} and gls grtr than {input_gls} based on past performance: ${1/pc_di_grtr_gls_grtr_time:.2f}")
print(f"True odds for gms with di grtr than {input_di} and gls less than {input_gls} based on past performance: ${1/pc_di_grtr_gls_less_time:.2f}")
print(f"True odds for gms with di less than {input_di} and gls grtr than {input_gls} based on past performance: ${1/pc_di_less_gls_grtr_time:.2f}")
print(f"True odds for gms with di less than {input_di} and gls less than {input_gls} based on past performance: ${1/pc_di_less_gls_less_time:.2f}")
print()
print()

# print the day results
print("Day of Week Results")
print(f"Number of gms with di grtr than {input_di} and gls grtr than {input_gls}: {di_grtr_gls_grtr_day}")
print(f"Number of gms with di grtr than {input_di} and gls less than {input_gls}: {di_grtr_gls_less_day}")
print(f"Number of gms with di less than {input_di} and gls grtr than {input_gls}: {di_less_gls_grtr_day}")
print(f"Number of gms with di less than {input_di} and gls less than {input_gls}: {di_less_gls_less_day}")
print(f"pc of gms with di grtr than {input_di} and gls grtr than {input_gls}: {pc_di_grtr_gls_grtr_day *100:.2f}%")
print(f"pc of gms with di grtr than {input_di} and gls less than {input_gls}: {pc_di_grtr_gls_less_day *100:.2f}%")
print(f"pc of gms with di less than {input_di} and gls grtr than {input_gls}: {pc_di_less_gls_grtr_day *100:.2f}%")
print(f"pc of gms with di less than {input_di} and gls less than {input_gls}: {pc_di_less_gls_less_day *100:.2f}%")
print(f"True odds for gms with di grtr than {input_di} and gls grtr than {input_gls} based on past performance: ${1/pc_di_grtr_gls_grtr_day:.2f}")
print(f"True odds for gms with di grtr than {input_di} and gls less than {input_gls} based on past performance: ${1/pc_di_grtr_gls_less_day:.2f}")
print(f"True odds for gms with di less than {input_di} and gls grtr than {input_gls} based on past performance: ${1/pc_di_less_gls_grtr_day:.2f}")
print(f"True odds for gms with di less than {input_di} and gls less than {input_gls} based on past performance: ${1/pc_di_less_gls_less_day:.2f}")
print()
print()
