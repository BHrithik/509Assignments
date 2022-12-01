import pandas as pd


gamesCSV = "gamesHrithik.csv"
finalCSV = "Final509.csv"
movesCSV = "Moves.csv"
moves = pd.DataFrame(columns=[
    "Game ID",
    "Turn",
    "Player",
    "Position"
])

def readGames():
    try:
        return pd.read_csv(gamesCSV)
    except FileNotFoundError:
        return pd.DataFrame(columns=[
            "Game ID",
            "Player1",
            "Player2",
            "Winner"
        ])

games = readGames()

def enterGame(id, name1,name2,winner):
    games.loc[len(games)] = {
        "Game ID":id,
        "Player1":name1,
        "Player2":name2,
        "Winner":winner
    }
    games.to_csv(gamesCSV, mode='a',index=False, header=False)
    moves.to_csv(movesCSV, mode='a', index=False, header=False)
    final = pd.merge(games,moves)
    final.to_csv(finalCSV, mode='a', index=False, header=False)

def enterMove(id,turn,name,position):
    moves.loc[len(moves)]={
        "Game ID":id,
        "Turn": turn,
        "Player": name,
        "Position": position
    }