#右手法
import random

maze=[
[9]*9,
[9,0,0,0,9,9,0,9,9],
[9,0,9,9,0,0,0,0,9],
[9,0,0,0,0,9,9,9,9],
[9,9,0,9,0,9,0,1,9],
[9,0,0,9,0,0,0,9,9],
[9]*9
]

d=[[0,-1],[-1,0],[0,1],[1,0]]

x,y=1,1
dir=0

while maze[x][y]!=1:

    move=d[(dir+1)%4]
    if maze[x+move[0]][y+move[1]]!=9:
        dir=(dir+1)%4
        x+=move[0]
        y+=move[1]
        print([x,y])
    else:
        dir=(dir+3)%4
