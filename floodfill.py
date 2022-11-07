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
max1 = len(board)
max2 = len(board[0])
##function for Flood_Fill
def flood_fill(input_board, old, new, x, y):
    if input_board[x][y] == "#" or input_board[x][y] == new: #Checking if position is a wall or a tile which has already been changed
        return;
    if input_board[x][y] != old:
        return;
    column = list(input_board[x]) #Converting to list because strings are immutable and then assigning the value
    column[y] = new #Chaning the value of the position to new
    input_board[x] = ''.join(column)
    if x+1<=max1-1:
        flood_fill(input_board,old,new,x+1,y); #Going North
    if x-1>=0 :
        flood_fill(input_board,old,new,x-1,y); #Going South
    if y+1<=max2-1:
        flood_fill(input_board,old,new,x,y+1); #Going East
    if y-1>=0 :
        flood_fill(input_board,old,new,x,y-1); #Going West
    return;

# use 4,12 for testing
flood_fill(board,".","~",0,0)

for a in board:
    print(a)
