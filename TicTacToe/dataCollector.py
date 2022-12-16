import pandas as pd


gamesCSV = "gamesHrithik.csv"
movesCSV = "Moves.csv"
moves = pd.DataFrame(columns=[
    "Game ID",
    "Turn",
    "Player",
    "Position"
])

games = pd.DataFrame(columns=[
            "Game ID",
            "Player1",
            "Player2",
            "Winner"
        ])

def enterGame(id, name1,name2,winner):
    games.loc[len(games)] = {
        "Game ID":id,
        "Player1":name1,
        "Player2":name2,
        "Winner":winner
    }
    games.to_csv(gamesCSV, mode='a',index=False, header=False)
    moves.to_csv(movesCSV, mode='a', index=False, header=False)

def enterMove(id,turn,name,position):
    moves.loc[len(moves)]={
        "Game ID":id,
        "Turn": turn,
        "Player": name,
        "Position": position
    }