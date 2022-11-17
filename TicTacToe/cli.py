# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.
from logic import TicTacToe
from easy import Easy

if __name__ == '__main__':
    winner = None #There is no winner before the game starts
    flag = 1 #Flag for forcing user to choose only X and O :P
    multiplayer = 0
    while True:
        multilayer = int(input("Do you want to play against a computer? 1- Yes 2- No"))-1;
        print(multilayer)
        if(multiplayer==0 or multiplayer==1):
            break
    print("We are here")
    if multilayer == 1:
        easyMove = Easy()
        game = TicTacToe(easyMove)
        while flag == 1 : 
            s1 = input("Player 1 - Please pick X or O -") #Letting user pick X or O
            if( s1 == "X" or s1 == "x"): #Automatically Assigning the second player the other symbol
                s2 = "O" 
                flag = 0
            elif( s1 == "o" or s1 == "O"):
                s2 = "X"
                flag = 0
            else:
                print("Please enter a valid symbol")  #Asking user to pick X or O and not anything else   
        print("Player1 is",s1)
        print("Player2 is",s2)
        print("Start")
        while winner == None:
            print("Player 1 ",s1," please enter the position") #Printing the board and asking player 1 to pick the position
            game.print_board()
            game.input1(s1) # Funtion to input positions for player 1
            winner = game.get_winner(s1) # Checking if there is a winner after each move
            if(winner!=None): # While winner is not found the game goes on
                game.print_board()
                print("Player1",s1," has won the game! Congratulations")
                break
            print("Player 2",s2," please enter the position") # We check the same thing when the second player takes turn
            game.print_board()
            if(game.count >=9):
                print("Game over, It is a draw")
                break
            game.input2(s2) # Funtion to input positions for player 2
            game.print_board() # Printing the board after each move
            winner = game.get_winner(s2)
            if(winner!=None):
                game.print_board()
                print("Player2",s2," has won the game! Congratulations")
                break
    elif multilayer==0:
        while flag == 1 : 
            s1 = input("Please pick X or O -") #Letting user pick X or O
            if( s1 == "X" or s1 == "x"): #Automatically Assigning the second player the other symbol
                s2 = "O" 
                d = int(input("Please pick the level of difficulty 1- Easy 2- Hard"))
                if d == 1 or d==2:
                    flag = 0
            elif( s1 == "o" or s1 == "O"):
                s2 = "X"
                d = int(input("Please pick the level of difficulty 1- Easy 2- Hard"))
                if d == 1 or d==2:
                    flag = 0
            else:
                print("Please enter a valid input")  #Asking user to pick X or O and not anything else
        if d==1:
            easyMove = Easy()
            game = TicTacToe(easyMove) #Dependency injection to make computer move
        elif d==2:
            hardMove = Easy() # Currently ther is no hard difficulty but can be implemented later
            game = TicTacToe(hardMove)  #Dependency injection to make computer move
        print("You are ",s1)
        print("Computer is ",s2)
        print("Start")
        while winner == None:
            print("Please enter the position") #Printing the board and asking player 1 to pick the position
            game.print_board()
            game.input1(s1) # Funtion to input positions for player 1
            winner = game.get_winner(s1) # Checking if there is a winner after each move
            if(winner!=None): # While winner is not found the game goes on
                game.print_board()
                print(s1," You won the game! Congratulations")
                break
            print("Computers turn")
            game.print_board()
            if(game.count >=9):
                print("Game over, It is a draw")
                break
            # Funtion to input positions for player 2
            game.computerMove(s2)
            game.print_board() # Printing the board after each move
            winner = game.get_winner(s2)
            if(winner!=None):
                game.print_board()
                print("Computer has won the game, You lost :(")
                break
