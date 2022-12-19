import pandas as pd
import plotly.express as px

def makeGraphTicTacToe():
    df1 = pd.read_csv("gamesHrithik.csv", sep=',',
                            names=['gameid', 'player1', 'player2', 'winner'])
    df2 = pd.read_csv("Moves.csv", sep=',', 
                            names=['gameid','count','playerName','position'])
    new_winner_list=[]
    for player in df1['winner']:
        if(player == "-"):
            player = "Draw" 
        new_winner_list.append(player.lower())
    df1['winner']=new_winner_list
    df1_ee = df1['winner'].value_counts()
    first_moves=[]
    for index, row in df2.iterrows():
        if(row['count']==1):
            first_moves.append([row['gameid'],row['position']])
    new_last = pd.DataFrame(first_moves, columns =['gameid', 'first_move']) 
    new_last1 = new_last['first_move'].value_counts()
    fig2 = px.bar(new_last1, title="First move count")
    df1_ee
    fig3 = px.bar(df1_ee,title="Top Players")
    return fig2,fig3