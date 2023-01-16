from pyexpat.errors import messages
from flask import Flask, render_template, request, url_for, flash, redirect
from logic import TicTacToe
from easy import Easy
import dataCollector
import uuid
import graphmaker
import json 
import plotly
import plotly.express as px

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'your secret key'
app = Flask(__name__)
app.config['SECRET_KEY'] = 'd96eeaee39a7aaf82d02dc9e3dc10407b2d9b97883b5c8b5'

easyMove = Easy() # Difficulty is left as improvement
game = TicTacToe(easyMove)



@app.route('/', methods=('POST','GET')) # Link to home page
def index():
    game.board = [[" "," "," "],[" "," "," "],[" "," "," "],]
    game.count = 0
    game.name1 = "DefaultName1",
    game.name2 = "bot",
    game.s1 = "",
    game.s2 = "",
    game.isSinglePlayer = False
    game.id = ""
    game.id = uuid.uuid4()
    print(game.id)
    return render_template('index.html')

@app.route('/multiplayer', methods=('POST','GET'))
def multiplayer():
    if request.method == 'POST':
        name1 = request.form['name1']
        S1 = request.form['options1']
        name2 = request.form['name2']
        if(S1 == "X"):
            S2 = "O"
        else :
            S2 = "X"
        if not name1:
            flash('Name1 is required!')
        elif not name2:
            flash('Name2 is required for multy player')
        else:
            print("Player 1 is ",name1)
            print("Symbol 1 is ", S1)
            print("Player 2 is ",name2)
            print("Symbol 2 is ", S2)
            game.name1 = name1
            game.name2 = name2
            game.s1 = S1
            game.s2 = S2
            return redirect(url_for('play'))
    return render_template('multi.html')

@app.route('/singleplayer', methods=('POST','GET'))
def singleplayer():
    if request.method == 'POST':
        name1 = request.form['name11']
        S1 = request.form['options11']
        if not name1:
            flash('Name of the player is required!')
        else:
            game.isSinglePlayer = True
            game.name2 = "bot"
            game.name1 = name1
            if(S1 == "X"):
                S2 = "O"
            else :
                S2 = "X"
            game.s1 = S1
            game.s2 = S2
            name2 = game.name2
            print("Player 1 is ",name1)
            print("Symbol 1 is ", S1)
            print("Player 2 is ",name2)
            print("Symbol 2 is ", S2)
            return redirect(url_for('play'))
        print("Player 1 is ",name1)
    return render_template('single.html')

@app.get('/aboutme')
def aboutme():
    return render_template('about.html')

@app.get('/play')
def play():
    game.print_board()
    details = ("Game Details:- Name1 {} {}, Name2 {} {}".format(game.name1,game.s1,game.name2,game.s2))
    if(game.isSinglePlayer == True and game.name1[0] == "DefaultName1"):
        print("deen thalli")
        return redirect(url_for('index'))
    if(game.isSinglePlayer == False and game.name1[0] == "DefaultName1" and game.name2[0] == "bot"):
        return redirect(url_for('index'))
    message = ""
    if(game.count%2 == 0):
        player = game.name1 + "'s turn"
    else:
        player = game.name2 + "'s turn"
    print("s1 ",game.get_winner(game.s1))
    print("s2 ",game.get_winner(game.s2))
    style = "";
    if(game.get_winner(game.s1) == None and game.get_winner(game.s2)== None):
        message = " "
        if(game.count >= 9):
            message = "It is a draw!"
            dataCollector.enterGame(game.id,game.name1,game.name2,"-")
            player = ""
            style = "none"
            details = ""
    if(game.get_winner(game.s1) == game.s1):
        print(message, "should change and show s1 won")
        message = "Congratulations " + game.name1 + " you have won the game!"
        dataCollector.enterGame(game.id,game.name1,game.name2,game.name1)
        player = ""
        style = "none"
        details = ""
    if(game.get_winner(game.s2) == game.s2):
        print(message, "should change and show s2 won")
        if( game.name2 != "bot"):
            message = "Congratulations " + game.name2 + " you have won the game!"
            dataCollector.enterGame(game.id,game.name1,game.name2,game.name2)
        else:
            message = "You lost!"
        player = ""
        style = "none"
        details = ""
    data = {
        "board": game.board,
        "details": details,
        "message": message,
        "turn": player,
        "style": style
    }
    return render_template('play.html',data=data)

@app.get('/playing/<int:pos1>/<int:pos2>')
def playing(pos1,pos2):
    if(game.board[pos1][pos2] == " " and game.get_winner(game.s1) == None and game.get_winner(game.s2) == None):
        if(game.count%2 == 0):
            game.input(game.s1[0],pos1,pos2)
            print("Move no.",game.count)
            print("symbol",game.s1,"in",pos1,pos2)
            if(game.isSinglePlayer):
                if(game.get_winner(game.s1) == None and game.get_winner(game.s2) == None and game.count != 9):
                    game.computerMove(game.s2[0])
        else:
            game.input(game.s2[0],pos1,pos2)
            print("Player 2 move")
            print("symbol",game.s2,"in",pos1,pos2)
    return redirect(url_for('play'))

@app.get('/stats')
def stats():
    graphs = graphmaker.makeGraphTicTacToe()
    graphJSON1 = json.dumps(graphs[0], cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON2 = json.dumps(graphs[1], cls=plotly.utils.PlotlyJSONEncoder)
    graphs = {
        "graph1": graphJSON1,
        "graph2": graphJSON2
    }
    return render_template("statistics.html", graphs = graphs)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)