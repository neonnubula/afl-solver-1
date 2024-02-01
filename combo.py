# # # 2 LEG COMBOS
# # # define function to count greater than and less than of the user input vs combo of disposal & goal lines.
# # def count_disposals_goals(disposals, goals):
# #   disposals_greater_goals_greater = df.loc[(df["season"] >= input_seasons) &
# #                                            (df["name"] == input_name) &
# #                                            (df["goals"] > input_goals) &
# #                                            (df["disposals"] > input_disposals),
# #                                            "disposals"].count()
# #   disposals_greater_goals_less = df.loc[(df["season"] >= input_seasons) &
# #                                         (df["name"] == input_name) &
# #                                         (df["goals"] < input_goals) &
# #                                         (df["disposals"] > input_disposals),
# #                                         "disposals"].count()
# #   disposals_less_goals_greater = df.loc[(df["season"] >= input_seasons) &
# #                                         (df["name"] == input_name) &
# #                                         (df["goals"] > input_goals) &
# #                                         (df["disposals"] < input_disposals),
# #                                         "disposals"].count()
# #   disposals_less_goals_less = df.loc[(df["season"] >= input_seasons) &
# #                                      (df["name"] == input_name) &
# #                                      (df["goals"] < input_goals) &
# #                                      (df["disposals"] < input_disposals),
# #                                      "disposals"].count()
# #   return disposals_greater_goals_greater, disposals_greater_goals_less, disposals_less_goals_greater, disposals_less_goals_less


# # # define function for user input location to count greater and less than of the user input vs disposal line
# # def count_disposals_goals_location(disposals, goals):
# #   disposals_greater_goals_greater_location = df.loc[
# #       (df["season"] >= input_seasons) & (df["name"] == input_name) &
# #       (df["location"] == input_location) & (df["goals"] > input_goals) &
# #       (df["disposals"] > input_disposals), "disposals"].count()
# #   disposals_greater_goals_less_location = df.loc[
# #       (df["season"] >= input_seasons) & (df["name"] == input_name) &
# #       (df["location"] == input_location) & (df["goals"] < input_goals) &
# #       (df["disposals"] > input_disposals), "disposals"].count()
# #   disposals_less_goals_greater_location = df.loc[
# #       (df["season"] >= input_seasons) & (df["name"] == input_name) &
# #       (df["location"] == input_location) & (df["goals"] > input_goals) &
# #       (df["disposals"] < input_disposals), "disposals"].count()
# #   disposals_less_goals_less_location = df.loc[
# #       (df["season"] >= input_seasons) & (df["name"] == input_name) &
# #       (df["location"] == input_location) & (df["goals"] < input_goals) &
# #       (df["disposals"] < input_disposals), "disposals"].count()
# #   return disposals_greater_goals_greater_location, disposals_greater_goals_less_location, disposals_less_goals_greater_location, disposals_less_goals_less_location
# #   # disposals_less_location = df.loc[(df["location"] == input_location) & (df["name"] == input_name) & (df["season"] >= input_seasons) & (df["disposals"] < input_disposals), "disposals"].count()
# #   # disposals_greater_location = df.loc[(df["location"] == input_location) & (df["name"] == input_name) & (df["season"] >= input_seasons) & (df["disposals"] > input_disposals), "disposals"].count()
# #   # return disposals_less_location, disposals_greater_location


# # # define the function for user input opposition to count greater than and less than of the user input vs disposals line
# # def count_disposals_goals_opposition(disposals, goals):
# #   disposals_greater_goals_greater_opposition = df.loc[
# #       (df["season"] >= input_seasons) & (df["name"] == input_name) &
# #       (df["opposition"] == input_opposition) & (df["goals"] > input_goals) &
# #       (df["disposals"] > input_disposals), "disposals"].count()
# #   disposals_greater_goals_less_opposition = df.loc[
# #       (df["season"] >= input_seasons) & (df["name"] == input_name) &
# #       (df["opposition"] == input_opposition) & (df["goals"] < input_goals) &
# #       (df["disposals"] > input_disposals), "disposals"].count()
# #   disposals_less_goals_greater_opposition = df.loc[
# #       (df["season"] >= input_seasons) & (df["name"] == input_name) &
# #       (df["opposition"] == input_opposition) & (df["goals"] > input_goals) &
# #       (df["disposals"] < input_disposals), "disposals"].count()
# #   disposals_less_goals_less_opposition = df.loc[
# #       (df["season"] >= input_seasons) & (df["name"] == input_name) &
# #       (df["opposition"] == input_opposition) & (df["goals"] < input_goals) &
# #       (df["disposals"] < input_disposals), "disposals"].count()
# #   return disposals_greater_goals_greater_opposition, disposals_greater_goals_less_opposition, disposals_less_goals_greater_opposition, disposals_less_goals_less_opposition
# #   # disposals_less_opposition = df.loc[(df["opposition"] == input_opposition) & (df["name"] == input_name) & (df["season"] >= input_seasons) & (df["disposals"] < input_disposals), "disposals"].count()
# #   # disposals_greater_opposition = df.loc[(df["opposition"] == input_opposition) & (df["name"] == input_name) & (df["season"] >= input_seasons) & (df["disposals"] > input_disposals), "disposals"].count()
# #   # return disposals_less_opposition, disposals_greater_opposition


# # # define the function for user input venue to count greater than and less than of the user input vs disposals line
# # def count_disposals_goals_venue(disposals, goals):
# #   disposals_greater_goals_greater_venue = df.loc[
# #       (df["season"] >= input_seasons) & (df["name"] == input_name) &
# #       (df["venue"] == input_venue) & (df["goals"] > input_goals) &
# #       (df["disposals"] > input_disposals), "disposals"].count()
# #   disposals_greater_goals_less_venue = df.loc[
# #       (df["season"] >= input_seasons) & (df["name"] == input_name) &
# #       (df["venue"] == input_venue) & (df["goals"] < input_goals) &
# #       (df["disposals"] > input_disposals), "disposals"].count()
# #   disposals_less_goals_greater_venue = df.loc[
# #       (df["season"] >= input_seasons) & (df["name"] == input_name) &
# #       (df["venue"] == input_venue) & (df["goals"] > input_goals) &
# #       (df["disposals"] < input_disposals), "disposals"].count()
# #   disposals_less_goals_less_venue = df.loc[(df["season"] >= input_seasons) &
# #                                            (df["name"] == input_name) &
# #                                            (df["venue"] == input_venue) &
# #                                            (df["goals"] < input_goals) &
# #                                            (df["disposals"] < input_disposals),
# #                                            "disposals"].count()
# #   return disposals_greater_goals_greater_venue, disposals_greater_goals_less_venue, disposals_less_goals_greater_venue, disposals_less_goals_less_venue
# #   # disposals_less_venue = df.loc[(df["venue"] == input_venue) & (df["name"] == input_name) & (df["season"] >= input_seasons) & (df["disposals"] < input_disposals), "disposals"].count()
# #   # disposals_greater_venue = df.loc[(df["venue"] == input_venue) & (df["name"] == input_name) & (df["season"] >= input_seasons) & (df["disposals"] > input_disposals), "disposals"].count()
# #   # return disposals_less_venue, disposals_greater_venue


# # # define the function for user input 2023 season to count greater than and less than of the user input vs disposals line
# # def count_disposals_goals_2023(disposals, goals):
# #   disposals_greater_goals_greater_2023 = df.loc[
# #       (df["season"] >= input_seasons) & (df["name"] == input_name) &
# #       (df["season"] == 2023) & (df["goals"] > input_goals) &
# #       (df["disposals"] > input_disposals), "disposals"].count()
# #   disposals_greater_goals_less_2023 = df.loc[
# #       (df["season"] >= input_seasons) & (df["name"] == input_name) &
# #       (df["season"] == 2023) & (df["goals"] < input_goals) &
# #       (df["disposals"] > input_disposals), "disposals"].count()
# #   disposals_less_goals_greater_2023 = df.loc[
# #       (df["season"] >= input_seasons) & (df["name"] == input_name) &
# #       (df["season"] == 2023) & (df["goals"] > input_goals) &
# #       (df["disposals"] < input_disposals), "disposals"].count()
# #   disposals_less_goals_less_2023 = df.loc[(df["season"] >= input_seasons) &
# #                                           (df["name"] == input_name) &
# #                                           (df["season"] == 2023) &
# #                                           (df["goals"] < input_goals) &
# #                                           (df["disposals"] < input_disposals),
# #                                           "disposals"].count()
# #   return disposals_greater_goals_greater_2023, disposals_greater_goals_less_2023, disposals_less_goals_greater_2023, disposals_less_goals_less_2023
# #   # disposals_less_2023 = df.loc[(df["season"] == 2023) & (df["name"] == input_name) & (df["disposals"] < input_disposals), "disposals"].count()
# #   # disposals_greater_2023 = df.loc[(df["season"] == 2023) & (df["name"] == input_name) & (df["disposals"] > input_disposals), "disposals"].count()
# #   # return disposals_less_2023, disposals_greater_2023


# # # define the function for user input time to count greater than and less than of the user input vs disposals line
# # def count_disposals_goals_time(disposals, goals):
# #   disposals_greater_goals_greater_time = df.loc[
# #       (df["season"] >= input_seasons) & (df["name"] == input_name) &
# #       (df["time"] == input_time) & (df["goals"] > input_goals) &
# #       (df["disposals"] > input_disposals), "disposals"].count()
# #   disposals_greater_goals_less_time = df.loc[
# #       (df["season"] >= input_seasons) & (df["name"] == input_name) &
# #       (df["time"] == input_time) & (df["goals"] < input_goals) &
# #       (df["disposals"] > input_disposals), "disposals"].count()
# #   disposals_less_goals_greater_time = df.loc[
# #       (df["season"] >= input_seasons) & (df["name"] == input_name) &
# #       (df["time"] == input_time) & (df["goals"] > input_goals) &
# #       (df["disposals"] < input_disposals), "disposals"].count()
# #   disposals_less_goals_less_time = df.loc[(df["season"] >= input_seasons) &
# #                                           (df["name"] == input_name) &
# #                                           (df["time"] == input_time) &
# #                                           (df["goals"] < input_goals) &
# #                                           (df["disposals"] < input_disposals),
# #                                           "disposals"].count()
# #   return disposals_greater_goals_greater_time, disposals_greater_goals_less_time, disposals_less_goals_greater_time, disposals_less_goals_less_time
# #   # disposals_less_time = df.loc[(df["time"] == input_time) & (df["name"] == input_name) & (df["season"] >= input_seasons) & (df["disposals"] < input_disposals), "disposals"].count()
# #   # disposals_greater_time = df.loc[(df["time"] == input_time) & (df["name"] == input_name) & (df["season"] >= input_seasons) & (df["disposals"] > input_disposals), "disposals"].count()
# #   # return disposals_less_time, disposals_greater_time


# # # define the function for user input day of week to count greater than and less than of the user input vs disposals line
# # def count_disposals_goals_dayofweek(disposals, goals):
# #   disposals_greater_goals_greater_dayofweek = df.loc[
# #       (df["season"] >= input_seasons) & (df["name"] == input_name) &
# #       (df["dayofweek"] == input_dayofweek) & (df["goals"] > input_goals) &
# #       (df["disposals"] > input_disposals), "disposals"].count()
# #   disposals_greater_goals_less_dayofweek = df.loc[
# #       (df["season"] >= input_seasons) & (df["name"] == input_name) &
# #       (df["dayofweek"] == input_dayofweek) & (df["goals"] < input_goals) &
# #       (df["disposals"] > input_disposals), "disposals"].count()
# #   disposals_less_goals_greater_dayofweek = df.loc[
# #       (df["season"] >= input_seasons) & (df["name"] == input_name) &
# #       (df["dayofweek"] == input_dayofweek) & (df["goals"] > input_goals) &
# #       (df["disposals"] < input_disposals), "disposals"].count()
# #   disposals_less_goals_less_dayofweek = df.loc[
# #       (df["season"] >= input_seasons) & (df["name"] == input_name) &
# #       (df["dayofweek"] == input_dayofweek) & (df["goals"] < input_goals) &
# #       (df["disposals"] < input_disposals), "disposals"].count()
# #   return disposals_greater_goals_greater_dayofweek, disposals_greater_goals_less_dayofweek, disposals_less_goals_greater_dayofweek, disposals_less_goals_less_dayofweek
# #   # disposals_less_dayofweek = df.loc[(df["dayofweek"] == input_dayofweek) & (df["name"] == input_name) & (df["season"] >= input_seasons) & (df["disposals"] < input_disposals), "disposals"].count()
# #   # disposals_greater_dayofweek = df.loc[(df["dayofweek"] == input_dayofweek) & (df["name"] == input_name) & (df["season"] >= input_seasons) & (df["disposals"] > input_disposals), "disposals"].count()
# #   # return disposals_less_dayofweek, disposals_greater_dayofweek


# # run the function with the user input vs the data frame of the test data
# # # 2 LEG COMBOS
# # # all games
# # disposals_greater_goals_greater, disposals_greater_goals_less, disposals_less_goals_greater, disposals_less_goals_less = count_disposals_goals(
# #     input_disposals, input_goals)
# # # location
# # disposals_greater_goals_greater_location, disposals_greater_goals_less_location, disposals_less_goals_greater_location, disposals_less_goals_less_location = count_disposals_goals_location(
# #     input_disposals, input_goals)
# # # opposition
# # disposals_greater_goals_greater_opposition, disposals_greater_goals_less_opposition, disposals_less_goals_greater_opposition, disposals_less_goals_less_opposition = count_disposals_goals_opposition(
# #     input_disposals, input_goals)
# # # venue
# # disposals_greater_goals_greater_venue, disposals_greater_goals_less_venue, disposals_less_goals_greater_venue, disposals_less_goals_less_venue = count_disposals_goals_venue(
# #     input_disposals, input_goals)
# # # 2023 season
# # disposals_greater_goals_greater_2023, disposals_greater_goals_less_2023, disposals_less_goals_greater_2023, disposals_less_goals_less_2023 = count_disposals_goals_2023(
# #     input_disposals, input_goals)
# # #  time
# # disposals_greater_goals_greater_time, disposals_greater_goals_less_time, disposals_less_goals_greater_time, disposals_less_goals_less_time = count_disposals_goals_time(
# #     input_disposals, input_goals)
# # # dayofweek
# # disposals_greater_goals_greater_dayofweek, disposals_greater_goals_less_dayofweek, disposals_less_goals_greater_dayofweek, disposals_less_goals_less_dayofweek = count_disposals_goals_dayofweek(
# #     input_disposals, input_goals)

# # create the total games
# #2 LEG COMBOS
# # all games
# # total_games_disposals_goals = disposals_greater_goals_greater + disposals_greater_goals_less + disposals_less_goals_greater + disposals_less_goals_less
# # # location
# # total_games_disposals_goals_location = disposals_greater_goals_greater_location + disposals_greater_goals_less_location + disposals_less_goals_greater_location + disposals_less_goals_less_location
# # # opposition
# # total_games_disposals_goals_opposition = disposals_greater_goals_greater_opposition + disposals_greater_goals_less_opposition + disposals_less_goals_greater_opposition + disposals_less_goals_less_opposition
# # # venue
# # total_games_disposals_goals_venue = disposals_greater_goals_greater_venue + disposals_greater_goals_less_venue + disposals_less_goals_greater_venue + disposals_less_goals_less_venue
# # # 2023 season
# # total_games_disposals_goals_2023 = disposals_greater_goals_greater_2023 + disposals_greater_goals_less_2023 + disposals_less_goals_greater_2023 + disposals_less_goals_less_2023
# # #  time
# # total_games_disposals_goals_time = disposals_greater_goals_greater_time + disposals_greater_goals_less_time + disposals_less_goals_greater_time + disposals_less_goals_less_time
# # # dayofweek
# # total_games_disposals_goals_dayofweek = disposals_greater_goals_greater_dayofweek + disposals_greater_goals_less_dayofweek + disposals_less_goals_greater_dayofweek + disposals_less_goals_less_dayofweek

# # create the pcs
# #2 LEG COMBOS
# # # all games
# # pc_disposals_greater_goals_greater = (disposals_greater_goals_greater /
# #                                               total_games_disposals_goals)
# # pc_disposals_greater_goals_less = (disposals_greater_goals_less /
# #                                            total_games_disposals_goals)
# # pc_disposals_less_goals_greater = (disposals_less_goals_greater /
# #                                            total_games_disposals_goals)
# # pc_disposals_less_goals_less = (disposals_less_goals_less /
# #                                         total_games_disposals_goals)
# # # location
# # pc_disposals_greater_goals_greater_location = (
# #     disposals_greater_goals_greater_location /
# #     total_games_disposals_goals_location)
# # pc_disposals_greater_goals_less_location = (
# #     disposals_greater_goals_less_location /
# #     total_games_disposals_goals_location)
# # pc_disposals_less_goals_greater_location = (
# #     disposals_less_goals_greater_location /
# #     total_games_disposals_goals_location)
# # pc_disposals_less_goals_less_location = (
# #     disposals_less_goals_less_location / total_games_disposals_goals_location)
# # # opposition
# # pc_disposals_greater_goals_greater_opposition = (
# #     disposals_greater_goals_greater_opposition /
# #     total_games_disposals_goals_opposition)
# # pc_disposals_greater_goals_less_opposition = (
# #     disposals_greater_goals_less_opposition /
# #     total_games_disposals_goals_opposition)
# # pc_disposals_less_goals_greater_opposition = (
# #     disposals_less_goals_greater_opposition /
# #     total_games_disposals_goals_opposition)
# # pc_disposals_less_goals_less_opposition = (
# #     disposals_less_goals_less_opposition /
# #     total_games_disposals_goals_opposition)
# # # venue
# # pc_disposals_greater_goals_greater_venue = (
# #     disposals_greater_goals_greater_venue / total_games_disposals_goals_venue)
# # pc_disposals_greater_goals_less_venue = (
# #     disposals_greater_goals_less_venue / total_games_disposals_goals_venue)
# # pc_disposals_less_goals_greater_venue = (
# #     disposals_less_goals_greater_venue / total_games_disposals_goals_venue)
# # pc_disposals_less_goals_less_venue = (
# #     disposals_less_goals_less_venue / total_games_disposals_goals_venue)
# # # 2023 season
# # pc_disposals_greater_goals_greater_2023 = (
# #     disposals_greater_goals_greater_2023 / total_games_disposals_goals_2023)
# # pc_disposals_greater_goals_less_2023 = (
# #     disposals_greater_goals_less_2023 / total_games_disposals_goals_2023)
# # pc_disposals_less_goals_greater_2023 = (
# #     disposals_less_goals_greater_2023 / total_games_disposals_goals_2023)
# # pc_disposals_less_goals_less_2023 = (disposals_less_goals_less_2023 /
# #                                              total_games_disposals_goals_2023)
# # # time
# # pc_disposals_greater_goals_greater_time = (
# #     disposals_greater_goals_greater_time / total_games_disposals_goals_time)
# # pc_disposals_greater_goals_less_time = (
# #     disposals_greater_goals_less_time / total_games_disposals_goals_time)
# # pc_disposals_less_goals_greater_time = (
# #     disposals_less_goals_greater_time / total_games_disposals_goals_time)
# # pc_disposals_less_goals_less_time = (disposals_less_goals_less_time /
# #                                              total_games_disposals_goals_time)
# # # dayofweek
# # pc_disposals_greater_goals_greater_dayofweek = (
# #     disposals_greater_goals_greater_dayofweek /
# #     total_games_disposals_goals_dayofweek)
# # pc_disposals_greater_goals_less_dayofweek = (
# #     disposals_greater_goals_less_dayofweek /
# #     total_games_disposals_goals_dayofweek)
# # pc_disposals_less_goals_greater_dayofweek = (
# #     disposals_less_goals_greater_dayofweek /
# #     total_games_disposals_goals_dayofweek)
# # pc_disposals_less_goals_less_dayofweek = (
# #     disposals_less_goals_less_dayofweek /
# #     total_games_disposals_goals_dayofweek)

# # print results based on 2 LEG COMBOS
# print("2 LEG COMBO RESULTS")
# # print the all games results
# print("All Games Results")
# print(f"Number of games with disposals greater than {input_disposals} and goals greater than {input_goals}: {disposals_greater_goals_greater}")
# print(f"Number of games with disposals greater than {input_disposals} and goals less than {input_goals}: {disposals_greater_goals_less}")
# print(f"Number of games with disposals less than {input_disposals} and goals greater than {input_goals}: {disposals_less_goals_greater}")
# print(f"Number of games with disposals less than {input_disposals} and goals less than {input_goals}: {disposals_greater_goals_less}")
# print(f"pc of games with disposals greater than {input_disposals} and goals greater than {input_goals}: {pc_disposals_greater_goals_greater *100:.2f}%")
# print(f"pc of games with disposals greater than {input_disposals} and goals less than {input_goals}: {pc_disposals_greater_goals_less *100:.2f}%")
# print(f"pc of games with disposals less than {input_disposals} and goals greater than {input_goals}: {pc_disposals_less_goals_greater *100:.2f}%")
# print(f"pc of games with disposals less than {input_disposals} and goals less than {input_goals}: {pc_disposals_less_goals_less *100:.2f}%")
# print(f"True odds for games with disposals greater than {input_disposals} and goals greater than {input_goals} based on past performance: ${1/pc_disposals_greater_goals_greater:.2f}")
# print(f"True odds for games with disposals greater than {input_disposals} and goals less than {input_goals} based on past performance: ${1/pc_disposals_greater_goals_less:.2f}")
# print(f"True odds for games with disposals less than {input_disposals} and goals greater than {input_goals} based on past performance: ${1/pc_disposals_less_goals_greater.2f}")
# print(f"True odds for games with disposals less than {input_disposals} and goals less than {input_goals} based on past performance: ${1/pc_disposals_less_goals_less:.2f}")
# print()
# print()
# # print the location results
# print("Location Results")
# print(f"Number of games with disposals greater than {input_disposals} and goals greater than {input_goals}: {disposals_greater_goals_greater_location}")
# print(f"Number of games with disposals greater than {input_disposals} and goals less than {input_goals}: {disposals_greater_goals_less_location}")
# print(f"Number of games with disposals less than {input_disposals} and goals greater than {input_goals}: {disposals_less_goals_greater_location}")
# print(f"Number of games with disposals less than {input_disposals} and goals less than {input_goals}: {disposals_less_goals_less_location}")
# print(f"pc of games with disposals greater than {input_disposals} and goals greater than {input_goals}: {pc_disposals_greater_goals_greater_location *100:.2f}%")
# print(f"pc of games with disposals greater than {input_disposals} and goals less than {input_goals}: {pc_disposals_greater_goals_less_location *100:.2f}%")
# print(f"pc of games with disposals less than {input_disposals} and goals greater than {input_goals}: {pc_disposals_less_goals_greater_location *100:.2f}%")
# print(f"pc of games with disposals less than {input_disposals} and goals less than {input_goals}: {pc_disposals_less_goals_less_location *100:.2f}%")
# print(f"True odds for games with disposals greater than {input_disposals} and goals greater than {input_goals} based on past performance: ${1/pc_disposals_greater_goals_greater_location:.2f}")
# print(f"True odds for games with disposals greater than {input_disposals} and goals less than {input_goals} based on past performance: ${1/pc_disposals_greater_goals_less_location:.2f}")
# print(f"True odds for games with disposals less than {input_disposals} and goals greater than {input_goals} based on past performance: ${1/pc_disposals_less_goals_greater_location:.2f}")
# print(f"True odds for games with disposals less than {input_disposals} and goals less than {input_goals} based on past performance: ${1/pc_disposals_less_goals_less_location:.2f}")
# print()
# print()
# # print the opposition results
# print("Opposition Results")
# print(f"Number of games with disposals greater than {input_disposals} and goals greater than {input_goals}: {disposals_greater_goals_greater_opposition}")
# print(f"Number of games with disposals greater than {input_disposals} and goals less than {input_goals}: {disposals_greater_goals_less_opposition}")
# print(f"Number of games with disposals less than {input_disposals} and goals greater than {input_goals}: {disposals_less_goals_greater_opposition}")
# print(f"Number of games with disposals less than {input_disposals} and goals less than {input_goals}: {disposals_less_goals_less_opposition}")
# print(f"pc of games with disposals greater than {input_disposals} and goals greater than {input_goals}: {pc_disposals_greater_goals_greater_opposition *100:.2f}%")
# print(f"pc of games with disposals greater than {input_disposals} and goals less than {input_goals}: {pc_disposals_greater_goals_less_opposition *100:.2f}%")
# print(f"pc of games with disposals less than {input_disposals} and goals greater than {input_goals}: {pc_disposals_less_goals_greater_opposition *100:.2f}%")
# print(f"pc of games with disposals less than {input_disposals} and goals less than {input_goals}: {pc_disposals_less_goals_less_opposition *100:.2f}%")
# print(f"True odds for games with disposals greater than {input_disposals} and goals greater than {input_goals} based on past performance: ${1/pc_disposals_greater_goals_greater_opposition:.2f}")
# print(f"True odds for games with disposals greater than {input_disposals} and goals less than {input_goals} based on past performance: ${1/pc_disposals_greater_goals_less_opposition:.2f}")
# print(f"True odds for games with disposals less than {input_disposals} and goals greater than {input_goals} based on past performance: ${1/pc_disposals_less_goals_greater_opposition:.2f}")
# print(f"True odds for games with disposals less than {input_disposals} and goals less than {input_goals} based on past performance: ${1/pc_disposals_less_goals_less_opposition:.2f}")
# print()
# print()
# # print the venue results
# print("Venue Results")
# print(f"Number of games with disposals greater than {input_disposals} and goals greater than {input_goals}: {disposals_greater_goals_greater_venue}")
# print(f"Number of games with disposals greater than {input_disposals} and goals less than {input_goals}: {disposals_greater_goals_less_venue}")
# print(f"Number of games with disposals less than {input_disposals} and goals greater than {input_goals}: {disposals_less_goals_greater_venue}")
# print(f"Number of games with disposals less than {input_disposals} and goals less than {input_goals}: {disposals_less_goals_less_venue}")
# print(f"pc of games with disposals greater than {input_disposals} and goals greater than {input_goals}: {pc_disposals_greater_goals_greater_venue *100:.2f}%")
# print(f"pc of games with disposals greater than {input_disposals} and goals less than {input_goals}: {pc_disposals_greater_goals_less_venue *100:.2f}%")
# print(f"pc of games with disposals less than {input_disposals} and goals greater than {input_goals}: {pc_disposals_less_goals_greater_venue *100:.2f}%")
# print(f"pc of games with disposals less than {input_disposals} and goals less than {input_goals}: {pc_disposals_less_goals_less_venue *100:.2f}%")
# print(f"True odds for games with disposals greater than {input_disposals} and goals greater than {input_goals} based on past performance: ${1/pc_disposals_greater_goals_greater_venue:.2f}")
# print(f"True odds for games with disposals greater than {input_disposals} and goals less than {input_goals} based on past performance: ${1/pc_disposals_greater_goals_less_venue:.2f}")
# print(f"True odds for games with disposals less than {input_disposals} and goals greater than {input_goals} based on past performance: ${1/pc_disposals_less_goals_greater_venue:.2f}")
# print(f"True odds for games with disposals less than {input_disposals} and goals less than {input_goals} based on past performance: ${1/pc_disposals_less_goals_less_venue:.2f}")
# print()
# print()
# # print the 2023 results
# print("2023 Results")
# print(f"Number of games with disposals greater than {input_disposals} and goals greater than {input_goals}: {disposals_greater_goals_greater_2023}")
# print(f"Number of games with disposals greater than {input_disposals} and goals less than {input_goals}: {disposals_greater_goals_less_2023}")
# print(f"Number of games with disposals less than {input_disposals} and goals greater than {input_goals}: {disposals_less_goals_greater_2023}")
# print(f"Number of games with disposals less than {input_disposals} and goals less than {input_goals}: {disposals_less_goals_less_2023}")
# print(f"pc of games with disposals greater than {input_disposals} and goals greater than {input_goals}: {pc_disposals_greater_goals_greater_2023 *100:.2f}%")
# print(f"pc of games with disposals greater than {input_disposals} and goals less than {input_goals}: {pc_disposals_greater_goals_less_2023 *100:.2f}%")
# print(f"pc of games with disposals less than {input_disposals} and goals greater than {input_goals}: {pc_disposals_less_goals_greater_2023 *100:.2f}%")
# print(f"pc of games with disposals less than {input_disposals} and goals less than {input_goals}: {pc_disposals_less_goals_less_2023 *100:.2f}%")
# print(f"True odds for games with disposals greater than {input_disposals} and goals greater than {input_goals} based on past performance: ${1/pc_disposals_greater_goals_greater_2023:.2f}")
# print(f"True odds for games with disposals greater than {input_disposals} and goals less than {input_goals} based on past performance: ${1/pc_disposals_greater_goals_less_2023:.2f}")
# print(f"True odds for games with disposals less than {input_disposals} and goals greater than {input_goals} based on past performance: ${1/pc_disposals_less_goals_greater_2023:.2f}")
# print(f"True odds for games with disposals less than {input_disposals} and goals less than {input_goals} based on past performance: ${1/pc_disposals_less_goals_less_2023:.2f}")
# print()
# print()
# # print the time results
# print("Time Results")
# print(f"Number of games with disposals greater than {input_disposals} and goals greater than {input_goals}: {disposals_greater_goals_greater_time}")
# print(f"Number of games with disposals greater than {input_disposals} and goals less than {input_goals}: {disposals_greater_goals_less_time}")
# print(f"Number of games with disposals less than {input_disposals} and goals greater than {input_goals}: {disposals_less_goals_greater_time}")
# print(f"Number of games with disposals less than {input_disposals} and goals less than {input_goals}: {disposals_less_goals_less_time}")
# print(f"pc of games with disposals greater than {input_disposals} and goals greater than {input_goals}: {pc_disposals_greater_goals_greater_time *100:.2f}%")
# print(f"pc of games with disposals greater than {input_disposals} and goals less than {input_goals}: {pc_disposals_greater_goals_less_time *100:.2f}%")
# print(f"pc of games with disposals less than {input_disposals} and goals greater than {input_goals}: {pc_disposals_less_goals_greater_time *100:.2f}%")
# print(f"pc of games with disposals less than {input_disposals} and goals less than {input_goals}: {pc_disposals_less_goals_less_time *100:.2f}%")
# print(f"True odds for games with disposals greater than {input_disposals} and goals greater than {input_goals} based on past performance: ${1/pc_disposals_greater_goals_greater_time:.2f}")
# print(f"True odds for games with disposals greater than {input_disposals} and goals less than {input_goals} based on past performance: ${1/pc_disposals_greater_goals_less_time:.2f}")
# print(f"True odds for games with disposals less than {input_disposals} and goals greater than {input_goals} based on past performance: ${1/pc_disposals_less_goals_greater_time:.2f}")
# print(f"True odds for games with disposals less than {input_disposals} and goals less than {input_goals} based on past performance: ${1/pc_disposals_less_goals_less_time:.2f}")
# print()
# print()
# # print the dayofweek results
# print("Day of Week Results")
# print(f"Number of games with disposals greater than {input_disposals} and goals greater than {input_goals}: {disposals_greater_goals_greater_dayofweek}")
# print(f"Number of games with disposals greater than {input_disposals} and goals less than {input_goals}: {disposals_greater_goals_less_dayofweek}")
# print(f"Number of games with disposals less than {input_disposals} and goals greater than {input_goals}: {disposals_less_goals_greater_dayofweek}")
# print(f"Number of games with disposals less than {input_disposals} and goals less than {input_goals}: {disposals_less_goals_less_dayofweek}")
# print(f"pc of games with disposals greater than {input_disposals} and goals greater than {input_goals}: {pc_disposals_greater_goals_greater_dayofweek *100:.2f}%")
# print(f"pc of games with disposals greater than {input_disposals} and goals less than {input_goals}: {pc_disposals_greater_goals_less_dayofweek *100:.2f}%")
# print(f"pc of games with disposals less than {input_disposals} and goals greater than {input_goals}: {pc_disposals_less_goals_greater_dayofweek *100:.2f}%")
# print(f"pc of games with disposals less than {input_disposals} and goals less than {input_goals}: {pc_disposals_less_goals_less_dayofweek *100:.2f}%")
# print(f"True odds for games with disposals greater than {input_disposals} and goals greater than {input_goals} based on past performance: ${1/pc_disposals_greater_goals_greater_dayofweek:.2f}")
# print(f"True odds for games with disposals greater than {input_disposals} and goals less than {input_goals} based on past performance: ${1/pc_disposals_greater_goals_less_dayofweek:.2f}")
# print(f"True odds for games with disposals less than {input_disposals} and goals greater than {input_goals} based on past performance: ${1/pc_disposals_less_goals_greater_dayofweek:.2f}")
# print(f"True odds for games with disposals less than {input_disposals} and goals less than {input_goals} based on past performance: ${1/pc_disposals_less_goals_less_dayofweek:.2f}")
# print()
# print()
