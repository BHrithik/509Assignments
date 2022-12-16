# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.
import dataCollector
import uuid

class TicTacToe:

    def __init__(self,difficulty) -> None: # New board is created when a game starts
        self.board = [[" "," "," "],
                      [" "," "," "],
                      [" "," "," "],]
        self.count = 0
        self.difficulty = difficulty
        self.id = uuid.uuid1()
        self.name1 = "DefaultName1",
        self.name2 = "bot",
        self.s1 = "",
        self.s2 = "",
        self.isSinglePlayer = False

    def input(self,s, pos1, pos2):
        if self.board[pos1][pos2] == " ":
            self.board[pos1][pos2] = s
            self.count = self.count+1
        else:
            print("Position is already taken",pos1,pos2)


    def input1(self, s1):
        flag = 0
        while flag == 0:
            x = int(input("enter column "))
            y = int(input("enter row "))
            if x>-1 and x<3 and y>-1 and y<3 and self.board[x][y] == " ":
                self.board[x][y] = s1
                flag = 1
                self.count = self.count + 1
                dataCollector.enterMove(self.id,self.count,self.name1,(x,y))
            else:
                print("Command failed as the position is already taken or the position is out of bounds")

    def input2(self, s2):
        flag = 0
        while flag == 0:
            x = int(input("enter column "))
            y = int(input("enter row "))
            if x>-1 and x<3 and y>-1 and y<3 and self.board[x][y] == " " :
                self.board[x][y] = s2
                flag = 1
                self.count = self.count + 1
                dataCollector.enterMove(self.id,self.count,self.name2,(x,y))
            else:
                print("Command failed as the position is already taken or the position is out of bounds")

    def computerMove(self, s2):
        print("Are we here ? 2")
        mademove = 0
        print("Computer is making a move")
        while mademove == 0:
            pos = self.difficulty.computerMove()
            if (self.count != 9):
                if self.board[pos[0]][pos[1]] == " ":
                    self.board[pos[0]][pos[1]]=s2
                    x = int(pos[0])
                    y = int(pos[1])
                    dataCollector.enterMove(self.id,self.count,self.name2,(x,y))
                    self.count = self.count + 1
                    mademove = 1

    def print_board(self): # Printing the board with values
        print("\n")
        print("\t   0     1     2  - Rows")
        print("\t      |     |")
        print("\t0  {}  |  {}  |  {}".format(self.board[0][0], self.board[0][1], self.board[0][2]))
        print('\t _____|_____|_____')
        print("\t      |     |")
        print("\t1  {}  |  {}  |  {}".format(self.board[1][0], self.board[1][1], self.board[1][2]))
        print('\t _____|_____|_____')
        print("\t      |     |")
        print("\t2  {}  |  {}  |  {}".format(self.board[2][0], self.board[2][1], self.board[2][2]))
        print("\t      |     |")
        print("\n")

    def get_winner(self,k): #Function to find winner
        #Checking winner in Columns
        if self.board[0][0] == self.board[0][1] == self.board[0][2] == k:
            return k
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] == k:
            return k
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] == k:
            return k
        #Checking winner in Rows
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] == k:
            return k
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] == k:
            return k
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] == k:
            return k
        #Checking diagonals
        elif self.board[1][1] == self.board[2][2] == self.board[0][0] == k:
            return k
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] == k:
            return k
        else:
            return None