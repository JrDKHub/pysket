import pandas as pd


def score(home: str, away: str):
    data = pd.read_csv("assets/data.csv")
    data = data.drop(["Age", "W", "L", "PW", "PL", "MOV", "SOS", "SRS"], axis=1)

    home_line = data[data["Team"] == home]
    home_ortg = home_line["ORtg"]

    away_line = data[data["Team"] == away]
    away_ortg = away_line["ORtg"]

    phi1 = home_ortg.iloc[0] - data["ORtg"].median()
    phi2 = away_ortg.iloc[0] - data["DRtg"].median()

    phi3 = phi1 - phi2
    phi4 = phi3 + data["ORtg"].median()
    goal_home = phi4 * (data["Pace"].median() / 100)

    phi6 = phi2 - phi1
    phi7 = phi6 + data["ORtg"].median()
    goal_away = phi7 * (data["ORtg"].median() / 100)

    return goal_home, goal_away
