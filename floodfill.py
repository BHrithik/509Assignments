from typing import List
import sys
board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

def flood_fill(input_board, old, new, x, y):
    if input_board[x][y] == "#" or input_board[x][y] == new: #Checking if position is a wall or a tile which has already been changed
        return;
    if input_board[x][y] != old:
        return;
    column = list(input_board[x]) #Converting to list because strings are immutable and then assigning the value
    column[y] = new #Chaning the value of the position to new
    input_board[x] = ''.join(column)
    flood_fill(input_board,old,new,x+1,y); #Going North
    flood_fill(input_board,old,new,x-1,y); #Going South
    flood_fill(input_board,old,new,x,y+1); #Going East
    flood_fill(input_board,old,new,x,y-1); #Going West
    return;

flood_fill(board,".","~",5,12)

for a in board:
    print(a)