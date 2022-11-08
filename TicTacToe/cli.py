# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board
from logic import print_board
from logic import get_winner

def input1():
    flag = 0
    while(flag == 0):
        x = int(input("enter column "))
        y = int(input("enter row "))
        if( x>-1 and x<3 and y>-1 and y<3 and board[x][y] != s1 and board[x][y] != s2):
            board[x][y] = s1
            flag = 1
        else:
            print("Command failed as the position is already taken or the position is out of bounds")

def input2():
    flag = 0
    while(flag == 0):
        x = int(input("enter column "))
        y = int(input("enter row "))
        if( x>-1 and x<3 and y>-1 and y<3 and board[x][y] != s1 and board[x][y] != s2):
            board[x][y] = s2
            flag = 1
        else:
            print("Command failed as the position is already taken or the position is out of bounds")

if __name__ == '__main__':
    board = make_empty_board() #Making empty board
    winner = None #There is no winner before the game starts
    flag = 1 #Flag for forcing user to choose only X and O :P
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
    count = 0
    while winner == None:
        print("Player 1",s1," please enter the position") #Printing the board and asking player 1 to pick the position
        print_board(board)
        input1() # Funtion to input positions for player 1
        count = count + 1 # Counting the number of moves made in the game max is 9 as there are only 9 boxes
        winner = get_winner(board,s1) # Checking if there is a winner after each move
        if(winner!=None): # While winner is not found the game goes on
            print_board(board)
            print("Player1",s1," has won the game! Congratulations")
            break;
        print("Player 2",s2," please enter the position") # We check the same thing when the second player takes turn
        print_board(board)
        if(count >=9):
            print("Game over, It is a draw")
            break;
        input2() # Funtion to input positions for player 2
        count = count + 1
        print("The count is ",count)
        print_board(board) # Printing the board after each move
        winner = get_winner(board,s2)
        if(winner!=None):
            print_board(board)
            print("Player2",s2," has won the game! Congratulations")
            break;
