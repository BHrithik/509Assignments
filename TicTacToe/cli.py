# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.
from logic import TicTacToe
from easy import Easy
import dataCollector

if __name__ == '__main__':
    winner = None #There is no winner before the game starts
    flag = 1 #Flag for forcing user to choose only X and O :P
    multiplayer = 0
    nameflag = True
    while True:
        while nameflag:
            name1 = input("Please enter your name - ")
            if ( name1 != "bot"):
                nameflag=False
            else:
                print("Enter a name other than bot")
        print("Player 1 is ",name1)
        multiplayer = int(input("Do you want to play against a computer? 1- Yes 2- No"))-1;
        if(multiplayer==0 or multiplayer==1):
            break
    if multiplayer == 1:
        nameflag = True
        while nameflag:
            name2 = input("Enter the name of player 2 - ")
            if ( name2 != "bot"):
                nameflag=False
            else:
                print("Enter a name other than bot")
        print("Player 2 is ",name2)
        easyMove = Easy()
        game = TicTacToe(easyMove)
        game.name1 = name1
        game.name2 = name2
        while flag == 1 :
            print(name1," please pick") #Letting user pick X or O 
            s1 = input("X or O -")
            if( s1 == "X" or s1 == "x"): #Automatically Assigning the second player the other symbol
                s2 = "O" 
                flag = 0
            elif( s1 == "o" or s1 == "O"):
                s2 = "X"
                flag = 0
            else:
                print("Please enter a valid symbol")  #Asking user to pick X or O and not anything else   
        print(name1," is",s1)
        print(name2," is",s2)
        print("Start")
        while winner == None:
            print(name1,s1," your turn ") #Printing the board and asking player 1 to pick the position
            game.print_board()
            game.input1(s1) # Funtion to input positions for player 1
            winner = game.get_winner(s1) # Checking if there is a winner after each move
            if(winner!=None): # While winner is not found the game goes on
                game.print_board()
                print(name1,s1," has won the game! Congratulations")
                dataCollector.enterGame(game.id,name1,name2,name1)
                break
            print(name2,s2," your turn ") #Printing the board and asking player 2 to pick the position
            game.print_board()
            if(game.count >=9):
                print("Game over, It is a draw")
                dataCollector.enterGame(game.id,name1,name2,"-")
                break
            game.input2(s2) # Funtion to input positions for player 2
            game.print_board() # Printing the board after each move
            winner = game.get_winner(s2)
            if(winner!=None):
                game.print_board()
                print(name2,s2," has won the game! Congratulations")
                dataCollector.enterGame(game.id,name1,name2,name2)
                break
    elif multiplayer==0: # playing against a bot
        while flag == 1 : 
            print(name1,"Please pick")
            s1 = input("X or O -") #Letting user pick X or O
            if( s1 == "X" or s1 == "x"): #Automatically Assigning the second player the other symbol
                s2 = "O" 
                d = int(input("Please pick the level of difficulty 1- Easy 2- Hard"))
                if d == 1 or d==2:
                    name2 = "bot"
                    flag = 0
            elif( s1 == "o" or s1 == "O"):
                s2 = "X"
                d = int(input("Please pick the level of difficulty 1- Easy 2- Hard"))
                if d == 1 or d==2:
                    name2 = "bot" #Can change the name of the bot depending on difficulty in the future
                    flag = 0
            else:
                print("Please enter a valid input")  #Asking user to pick X or O and not anything else
        if d==1:
            easyMove = Easy()
            game = TicTacToe(easyMove) #Dependency injection to make computer move
        elif d==2:
            hardMove = Easy() # Currently ther is no hard difficulty but can be implemented later
            game = TicTacToe(hardMove)  #Dependency injection to make computer move
        print(name1," is ",s1)
        print(name2," is ",s2)
        game.name1 = name1
        game.name2 = name2
        print("Start")
        while winner == None:
            print(name1," you are ",s1," please enter the position") #Printing the board and asking player 1 to pick the position
            game.print_board()
            game.input1(s1) # Funtion to input positions for player 1
            winner = game.get_winner(s1) # Checking if there is a winner after each move
            if(winner!=None): # While winner is not found the game goes on
                game.print_board()
                print(name1," won the game! Congratulations")
                dataCollector.enterGame(game.id,name1,name2,name1)
                break
            print("Computers turn")
            game.print_board()
            if(game.count >=9):
                print("Game over, It is a draw")
                dataCollector.enterGame(game.id,name1,name2,"-")
                break
            # Funtion to input positions for player 2
            game.computerMove(s2)
            game.print_board() # Printing the board after each move
            winner = game.get_winner(s2)
            if(winner!=None):
                game.print_board()
                print(name2," has won the game, You lost :(")
                dataCollector.enterGame(game.id,name1,name2,name2)
                break
